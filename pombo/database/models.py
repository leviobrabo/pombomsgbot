# Pombo Correio Bot
# Copyright (C) 2023 leviobrabo
#
# This file is a part of < https://github.com/leviobrabo/pombomsgbot/ >
# PLease read the GNU v3.0 License Agreement in
# <https://github.com/leviobrabo/pombomsgbot/blob/main/LICENSE>.

import os
from datetime import datetime

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

DATABASE_TYPE = 'POSTGRESQL'

# PARA USAR SQLITE, DESCOMENTE ABAIXO
# DATABASE_TYPE = 'SQLITE'
# PARA USAR SQLITE, DESCOMENTE ACIMA

if DATABASE_TYPE == 'SQLITE':
    from playhouse.sqliteq import SqliteQueueDatabase

    db = SqliteQueueDatabase(
        'my_app.db',
        use_gevent=False,
        autostart=True,
        queue_max_size=64,
        results_timeout=5.0,
    )
else:
    db = connect(os.environ['DATABASE_URL'])


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
            result.refresh(user)
        except Exception as e:
            if str(e).startswith(
                (
                    'no such column: t1.has_sudo',
                    'column t1.has_sudo does not exist',
                )
            ):
                update_db()
            result = User.create(
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                language_code=user.language_code,
                has_dialog=False,
                inline_queries_count=0,
                first_interaction_time=datetime.utcnow(),
                last_interaction_time=datetime.utcnow(),
                has_sudo=False,
                has_banned=False,
            )
            logger.info(
                'novo usuário '
                + get_formatted_username_or_id(user)
                + ' foi salvo no banco de dados'
            )
        return result

    def refresh(self, user: types.User):
        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.language_code = user.language_code
        self.last_interaction_time = datetime.utcnow()
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

    def set_sudo(user_id, sudo_user=True):
        result = User.get_by_id(user_id)
        result.has_sudo = sudo_user
        result.save()

    def set_banned(user_id, ban_user=True):
        result = User.get_by_id(user_id)
        result.has_banned = ban_user
        result.save()

    def disable_user(user_id):
        result = User.get_by_id(user_id)
        result.has_dialog = False
        result.save()


class Post(BaseModel):
    author = ForeignKeyField(User)
    content = CharField()
    scope = CharField()
    creation_time = TimestampField()

    def get_scope_mentions(self):
        return str(self.scope).lower().split(' ')

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
                    or str(user.id) in self.scope
                )
        elif mode == PostMode.EXCEPT:
            if (
                user.username
                and user.username.lower() in self.get_scope_mentions()
            ):
                access_granted = False
                self.update_scope_mention(user.username, str(user.id))
            else:
                access_granted = str(user.id) not in self.scope
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
            result.refresh(group)
        except Exception as e:
            result = Group.create(
                group_id=group.id,
                type=group.type,
                title=group.title,
                username=group.username,
                has_dialog=False,
                first_interaction_time=datetime.utcnow(),
                last_interaction_time=datetime.utcnow(),
            )
            logger.info(
                'novo usuário '
                + get_formatted_username_or_id_chat(group)
                + ' foi salvo no banco de dados'
            )
        return result

    def refresh(self, group: types.Chat):
        self.username = group.username
        self.type = group.type
        self.title = group.title
        self.last_interaction_time = datetime.utcnow()
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

    def disable_user(user_id):
        result = Group.get_by_id(user_id)
        result.has_dialog = False
        result.save()


db.create_tables([User, Post, Group], safe=True)
