Pombo Correio

[Pombo Correio](https://t.me/pombomsgbot) send secret messages through this inline telegram bot.

[![](https://img.shields.io/badge/telegram-@pombomsgbot-blue)](https://t.me/pombomsgbot) 
[![](https://img.shields.io/badge/Official_Channel-Pombo_Correio-blue)](https://t.me/pombomsgbotchannel)
[![](https://i.imgur.com/wrrKuAn.png)](#)

### How do I host it? (VPS)

Here is a brief guide you can follow to host your own Pombo Correio in case you are afraid of data leaks or for any other reason.

1. Create a new bot via [Botfather](https://t.me/botfather).
2. Make your bot inline at Bot → Bot Settings → Inline Mode → Turn inline mode on.
3. Optionally set up your custom inline placeholder (e. g. <i>sample text @user</i>) at Bot → Bot Settings → Inline Mode → Edit inline placeholder.
4. [Fork](https://github.com/leviobrabo/pombomsgbot/fork) this repo.
5. In vps: git clone repo fork.
6. vi .env (Set up all required environment variables)
7. pip3 install -r requirements.txt
8. python pombo.py

### Environment variables

-   `API_TOKEN` – Telegram API bot token
-   `LOG_PATH` – path to the log-file (e. g. **logs/session\_{time}.log**)
-   `DATABASE_URL` – connection URL of the database (see [examples](https://www.prisma.io/docs/reference/database-reference/connection-urls))
-   `ADMINS` - ID of bot admin users (32400363 or 32400360, 52130333, 5122330)
-   `channelStatusId` - Channel ID
-   `GROUP_ID` - GROUP_ID LOG

### Telegram input template

> @pombomsgbot sample text @user1 @user2 @user3

-   `@pombomsgbot` – inline mention of the bot
-   `sample text` – text to be hidden
-   `@user1 @user2 @user3` – list of users in scope

### Available modes

-   `spoiler` – hidden content can be seen by everyone
-   `for` – hidden content can only be seen by the author and users in scope
-   `except` – hidden content can be seen by everyone except users in scope

### Placeholders

Can be used in messages to be replaced with user-related values. For instance, you can send the following message to a public chat to make everyone see his own `full_name` instead of `{name}` placeholder:

> @pombomsgbot I guess its time to kick {name} from this chat. cant stand this clown anymore

-   `{username}` – viewer's username (e. g. **@kylorensbot**)
-   `{uid}` – viewer's UID (e. g. **id837151456**)
-   `{lang}` – viewer's language code (e. g. **en** or **pt-br**)
-   `{pid}` – post (DB row) ID (e. g. **#32400360**)
-   `{created}` – post creation timestamp (e. g. **2077-07-05 19:53:17.864156**)
-   `{queries}` – total count of inline queries sent by viewer (e. g. **42**)
-   `{first_interaction}` – precise UTC timestamp of when viewer was saved to the database for the first time (e. g. **2077-07-05 19:53:17.864156**)
-   `{dialog}` – indicates whether viewer has ever written to the bot in private chat (e. g. **Yes**)
-   `{utc}` – precise UTC timestamp (e. g. **2077-07-05 19:53:17.864156**)
-   `{date}` – current UTC date (e. g. **2077-07-05**)
-   `{time}` – current UTC time (e. g. **19:53**)
-   `{name}` – viewer's full name (e. g. **Big Floppa**)
-   `{first_name}` – viewer's first name (e. g. **Big**)
-   `{last_name}` – viewer's last name (e. g. **Floppa**)

All datetime-related placeholders adhere to the UTC timezone with +00:00 shift.
