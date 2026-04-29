teste todos os recursos do bot, faça pytest e mock e procure por erros de implementação...


fale dos beneficios de alterar o banco de dados de postgresql para mongodb em texto curto, e como vc faria para alterar e converter os dados atuais para o novo banco de dados sem erros

/root/.pm2/logs/pombo-error.log last 15 lines:
9|pombo    | back for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:08,184 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:08,398 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:08,614 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:08,828 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:09,041 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:09,255 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:09,470 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:09,684 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:09,899 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:10,112 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:10,325 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo    | 2026-04-27 21:36:10,543 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"

9|pombo  | 2026-04-27 21:36:10,757 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo  | 2026-04-27 21:36:10,973 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo  | 2026-04-27 21:36:11,192 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo  | 2026-04-27 21:36:11,408 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
9|pombo  | 2026-04-27 21:36:11,623 (async_telebot.py:455 MainThread) ERROR - TeleBot: "Unhandled exception (full traceback for debug level): ChatBoost.__init__() missing 3 required positional arguments: 'boost_id', 'add_date', and 'expiration_date'"
