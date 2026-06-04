# Pombo Correio Bot
# Copyright (C) 2023 leviobrabo
#
# This file is a part of < https://github.com/leviobrabo/pombomsgbot/ >
# PLease read the GNU v3.0 License Agreement in
# <https://github.com/leviobrabo/pombomsgbot/blob/main/LICENSE>.

import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

from loguru import logger
from peewee import (
    BigIntegerField,
    BooleanField,
    CharField,
    ForeignKeyField,
    IntegerField,
    Model,
    TimestampField,
)
from playhouse.db_url import connect
from playhouse.migrate import PostgresqlMigrator, SqliteMigrator, migrate
from telebot import types, util

from pombo.utils.post_utils import (
    PostMode,
    get_formatted_username_or_id,
    get_formatted_username_or_id_chat,
)
load_dotenv()

_db_url = os.environ.get('DATABASE_URL') or 'sqlite:///my_app.db'
DATABASE_TYPE = 'SQLITE' if _db_url.startswith('sqlite') else 'POSTGRESQL'

if DATABASE_TYPE == 'SQLITE':
    from playhouse.sqliteq import SqliteQueueDatabase

    db = SqliteQueueDatabase(
        _db_url.split(':///', 1)[-1],
        use_gevent=False,
        autostart=True,
        queue_max_size=64,
        results_timeout=5.0,
    )
else:
    db = connect(_db_url)


def update_db():
    try:
        if DATABASE_TYPE == 'SQLITE':
            migrator = SqliteMigrator(db)  # PARA SQLITE
        else:
            migrator = PostgresqlMigrator(db)  # PARA POSTGRESQL
        migrate(
            migrator.add_column(
                'user', 'has_sudo', BooleanField(default=False)
            ),
            migrator.add_column(
                'user', 'has_banned', BooleanField(default=False)
            ),
        )
    except Exception as ex:
        logger.error(ex)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    username = CharField(null=True)
    first_name = CharField()
    last_name = CharField(null=True)
    language_code = CharField(null=True)
    has_dialog = BooleanField()
    inline_queries_count = IntegerField()
    first_interaction_time = TimestampField()
    last_interaction_time = TimestampField()
    has_sudo = BooleanField()
    has_banned = BooleanField()

    @staticmethod
    def get_or_create(user: types.User):
        try:
            result = User.get_by_id(user.id)
        except User.DoesNotExist:
            result = User.create(
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                language_code=user.language_code,
                has_dialog=False,
                inline_queries_count=0,
                first_interaction_time=datetime.now(timezone.utc),
                last_interaction_time=datetime.now(timezone.utc),
                has_sudo=False,
                has_banned=False,
            )
            logger.info(
                'novo usuário '
                + get_formatted_username_or_id(user)
                + ' foi salvo no banco de dados'
            )
            return result
        result.refresh(user)
        return result

    def refresh(self, user: types.User):
        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.language_code = user.language_code
        self.last_interaction_time = datetime.now(timezone.utc)
        self.has_dialog = True
        self.save()

    def get_values(self):
        return (
            self.user_id,
            self.username,
            self.language_code,
            self.has_dialog,
            self.inline_queries_count,
            self.first_interaction_time,
            self.last_interaction_time,
            self.has_sudo,
            self.has_banned,
        )

    @staticmethod
    def set_sudo(user_id, sudo_user=True):
        try:
            result = User.get_by_id(user_id)
        except User.DoesNotExist:
            raise ValueError(f'Usuário {user_id} não encontrado')
        result.has_sudo = sudo_user
        result.save()

    @staticmethod
    def set_banned(user_id, ban_user=True):
        try:
            result = User.get_by_id(user_id)
        except User.DoesNotExist:
            raise ValueError(f'Usuário {user_id} não encontrado')
        result.has_banned = ban_user
        result.save()

    @staticmethod
    def disable_user(user_id):
        try:
            result = User.get_by_id(user_id)
        except User.DoesNotExist:
            return
        result.has_dialog = False
        result.save()

    @staticmethod
    def count_active_since(days: int) -> int:
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        return User.select().where(User.last_interaction_time >= cutoff).count()

    @staticmethod
    def count_with_dialog() -> int:
        return User.select().where(User.has_dialog == True).count()

    @staticmethod
    def retention_rate(days: int) -> tuple:
        """Returns (retained, cohort_size): users created >= `days` ago who returned after `days` days."""
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        threshold_seconds = days * 86400
        total = 0
        retained = 0
        for row in User.select(User.first_interaction_time, User.last_interaction_time).where(
            User.first_interaction_time <= cutoff
        ):
            total += 1
            first = row.first_interaction_time
            last = row.last_interaction_time
            if first and last:
                diff = (
                    (last - first).total_seconds()
                    if isinstance(first, datetime)
                    else float(last) - float(first)
                )
                if diff >= threshold_seconds:
                    retained += 1
        return retained, total

    @staticmethod
    def top_users(n: int = 5):
        return (
            User.select(User.user_id, User.first_name, User.inline_queries_count)
            .order_by(User.inline_queries_count.desc())
            .limit(n)
        )


class Post(BaseModel):
    author = ForeignKeyField(User)
    content = CharField()
    scope = CharField()
    creation_time = TimestampField()

    def get_scope_mentions(self):
        s = str(self.scope).strip()
        return s.lower().split(' ') if s else []

    def set_scope_mentions(self, mentions: set):
        self.scope = ' '.join(mentions).replace('@', '')
        self.save()

    def update_scope_mention(self, old_mention: str, new_mention: str):
        mentions = self.get_scope_mentions()
        mentions.remove(old_mention.lower())
        mentions.append(new_mention.lower())
        self.set_scope_mentions(set(mentions))

    def can_be_accessed_by(self, user: types.User, mode: PostMode):
        access_granted = False
        if mode == PostMode.SPOILER:
            access_granted = True
        elif mode == PostMode.FOR:
            if (
                user.username
                and user.username.lower() in self.get_scope_mentions()
            ):
                access_granted = True
                self.update_scope_mention(user.username, str(user.id))
            else:
                access_granted = (
                    user.id == self.author.user_id
                    or str(user.id) in self.get_scope_mentions()
                )
        elif mode == PostMode.EXCEPT:
            if user.id == self.author.user_id:
                access_granted = True
            elif (
                user.username
                and user.username.lower() in self.get_scope_mentions()
            ):
                access_granted = False
                self.update_scope_mention(user.username, str(user.id))
            else:
                access_granted = str(user.id) not in self.get_scope_mentions()
        return access_granted


class Group(BaseModel):
    group_id = BigIntegerField(primary_key=True)
    type = CharField()
    title = CharField()
    username = CharField(null=True)
    has_dialog = BooleanField()
    first_interaction_time = TimestampField()
    last_interaction_time = TimestampField()

    @staticmethod
    def get_or_create(group: types.Chat):
        try:
            result = Group.get_by_id(group.id)
        except Group.DoesNotExist:
            result = Group.create(
                group_id=group.id,
                type=group.type,
                title=group.title,
                username=group.username,
                has_dialog=False,
                first_interaction_time=datetime.now(timezone.utc),
                last_interaction_time=datetime.now(timezone.utc),
            )
            logger.info(
                'novo grupo '
                + get_formatted_username_or_id_chat(group)
                + ' foi salvo no banco de dados'
            )
            return result
        result.refresh(group)
        return result

    def refresh(self, group: types.Chat):
        self.username = group.username
        self.type = group.type
        self.title = group.title
        self.last_interaction_time = datetime.now(timezone.utc)
        self.has_dialog = True
        self.save()

    def get_values(self):
        return (
            self.group_id,
            self.type,
            self.username,
            self.has_dialog,
            self.first_interaction_time,
            self.last_interaction_time,
        )

    @staticmethod
    def disable_user(user_id):
        result = Group.get_by_id(user_id)
        result.has_dialog = False
        result.save()


db.create_tables([User, Post, Group], safe=True)
