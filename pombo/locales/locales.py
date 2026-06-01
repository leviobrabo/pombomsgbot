# Pombo Correio Bot
# Copyright (C) 2023 leviobrabo
#
# This file is a part of < https://github.com/leviobrabo/pombomsgbot/ >
# PLease read the GNU v3.0 License Agreement in
# <https://github.com/leviobrabo/pombomsgbot/blob/main/LICENSE>.

from .locales_dict import Locale, LocalesDict

locale_pt = Locale()  # Portuguese
locale_en = Locale()  # English
locale_ru = Locale()  # Russian
locale_uk = Locale()  # Ukrainian
locale_de = Locale()  # German
locale_it = Locale()  # Italian
locale_fr = Locale()  # French
locale_es = Locale()  # Spanish
locale_ja = Locale()  # Japanese
locale_zh = Locale()  # Chinese
locale_hi = Locale()  # Hindi
locale_ar = Locale()  # Arabic
locale_tr = Locale()  # Turkish
locale_id = Locale()  # Indonesian
locale_fa = Locale()  # Persian/Farsi
locale_ko = Locale()  # Korean
locale_pl = Locale()  # Polish

locales = LocalesDict(
    {
        'pt': locale_pt,
        'en': locale_en,
        'ru': locale_ru,
        'uk': locale_uk,
        'de': locale_de,
        'it': locale_it,
        'fr': locale_fr,
        'es': locale_es,
        'ja': locale_ja,
        'zh': locale_zh,
        'hi': locale_hi,
        'ar': locale_ar,
        'tr': locale_tr,
        'id': locale_id,
        'fa': locale_fa,
        'ko': locale_ko,
        'pl': locale_pl,
    },
    locale_en,
)

# TOO_LONG_TITLE
locale_pt.too_long_title = '😮 Sua mensagem é muito longa'
locale_en.too_long_title = '😮 Your message is too long'
locale_ru.too_long_title = '😮 Слишком длинное сообщение'
locale_uk.too_long_title = '😮 Занадто довге повідомлення'
locale_de.too_long_title = '😮 Deine Nachricht ist zu lang'
locale_it.too_long_title = '😮 Il tuo messaggio è troppo lungo'
locale_fr.too_long_title = '😮 Votre message est trop long'
locale_es.too_long_title = '😮 Tu mensaje es demasiado largo'
locale_ja.too_long_title = '😮 メッセージが長すぎます'
locale_zh.too_long_title = '😮 你的信息太長了'
locale_hi.too_long_title = '😮 आपका संदेश बहुत लंबा है'
locale_ar.too_long_title = '😮 رسالتك طويلة جدًا'

# FOR_TITLE
locale_pt.for_title = '💬 Enviar mensagem para  %s'
locale_en.for_title = '💬 For %s'
locale_ru.for_title = '💬 Для %s'
locale_uk.for_title = '💬 Для %s'
locale_de.for_title = '💬 Für %s'
locale_it.for_title = '💬 Per %s'
locale_fr.for_title = '💬 Pour %s'
locale_es.for_title = '💬 Para %s'
locale_ja.for_title = '💬 %s へ'
locale_zh.for_title = '💬 发送消息给 %s'
locale_hi.for_title = '💬 %s के लिए'
locale_ar.for_title = '💬 لـ %s'

# EXCEPT_TITLE
locale_pt.except_title = '💬 Para todos, menos %s'
locale_en.except_title = '💬 Except %s'
locale_ru.except_title = '💬 Кроме %s'
locale_uk.except_title = '💬 Крім %s'
locale_de.except_title = '💬 Außer %s'
locale_it.except_title = '💬 Tranne %s'
locale_fr.except_title = '💬 Sauf %s'
locale_es.except_title = '💬 Excepto %s'
locale_ja.except_title = '💬 %s を除く'
locale_zh.except_title = '💬 除了 %s'
locale_hi.except_title = '💬 %s को छोड़कर'
locale_ar.except_title = '💬 باستثناء %s'

# SPOILER_TITLE
locale_pt.spoiler_title = '✅ Revelar mensagem para todos'
locale_en.spoiler_title = '✅ Spoiler'
locale_ru.spoiler_title = '✅ Спойлер'
locale_uk.spoiler_title = '✅ Спойлер'
locale_de.spoiler_title = '✅ Spoiler'
locale_it.spoiler_title = '✅ Spoiler'
locale_fr.spoiler_title = '✅ Spoiler'
locale_es.spoiler_title = '✅ Spoiler'
locale_ja.spoiler_title = '✅ スポイラー'
locale_zh.spoiler_title = '✅ 劇透'
locale_hi.spoiler_title = '✅ स्पॉइलर'
locale_ar.spoiler_title = '✅ سبويلر'

# TOO_LONG_MESSAGE
locale_pt.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Desculpe, sua mensagem não pode ser enviada porque excedeu o limite de 200 caracteres.'
locale_en.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Sorry, your message can\'t be sent as it exceeds the limit of 200 characters.'
locale_ru.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Ваше сообщение не может быть отправлено, так как его длина превышает лимит в 200 символов.'
locale_uk.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Ваше повідомлення не може бути відправлено, так як його довжина перевищує ліміт в 200 символів.'
locale_de.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Sorry, deine Nachricht kann nicht gesendet werden, da sie das Limit von 200 Zeichen überschreitet.'
locale_it.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Mi dispiace, il tuo messaggio non può essere mandato, supera il limite di 200 caratteri.'
locale_fr.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Désolé, votre message ne peut pas être envoyé car il dépasse la limite de 200 caractères.'
locale_es.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Lo siento, tu mensaje no puede ser enviado ya que excede el límite de 200 caracteres.'
locale_ja.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> 200文字の制限を超えたため、メッセージを送信できません。'
locale_zh.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> 对不起，您的消息无法发送，因为它超过了200个字符的限制。'
locale_hi.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> क्षमा करें, आपका संदेश 200 अक्षरों की सीमा से अधिक होने के कारण भेजा नहीं जा सकता है।'
locale_ar.too_long_message = (
    '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> عذرا، لا يمكن إرسال رسالتك لأنها تتجاوز الحد المسموح به من 200 حرف.'
)

# FOR_MESSAGE
locale_pt.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Mensagem secreta enviada com sucesso para %s.'
locale_en.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Private message for %s.'
locale_ru.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Приватное сообщение для %s.'
locale_uk.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Приватне повідомлення для %s.'
locale_de.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Private Nachricht für %s.'
locale_it.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Messaggio privato per %s.'
locale_fr.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Message privé pour %s.'
locale_es.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Mensaje privado para %s.'
locale_ja.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> %s へのプライベート メッセージ。'
locale_zh.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> 給 %s 的私信。'
locale_hi.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> %s के लिए निजी संदेश।'
locale_ar.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> رسالة خاصة ل %s.'

# EXCEPT_MESSAGE
locale_pt.except_message = '💬 %s, você foi excluído(a) desta mensagem secreta.'
locale_en.except_message = '💬 Private message for everyone except %s.'
locale_ru.except_message = '💬 Приватное сообщение для всех, кроме %s.'
locale_uk.except_message = '💬 Приватне повідомлення для всіх, крім %s.'
locale_de.except_message = '💬 Private Nachricht an alle außer %s.'
locale_it.except_message = '💬 Messaggio privato per tutti tranne %s.'
locale_fr.except_message = '💬 Message privé pour tout le monde sauf %s.'
locale_es.except_message = '💬 Mensaje privado para todos excepto %s.'
locale_ja.except_message = '💬 %s以外の全員へのプライベートメッセージ。'
locale_zh.except_message = '💬 给除%s之外的所有人的私人消息。'
locale_hi.except_message = '💬 %s को छोड़कर सभी के लिए निजी संदेश।'
locale_ar.except_message = '💬 رسالة خاصة للجميع ما عدا %s.'


# SPOILER_MESSAGE
locale_pt.spoiler_message = (
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Mensagem enviada para todos os integrantes do grupo.'
)
locale_en.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Public spoiler message.'
locale_ru.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Публичное сообщение под спойлером.'
locale_uk.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Публічне повідомлення під спойлером.'
locale_de.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Öffentlicher Spoiler für alle:'
locale_it.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Messaggio contenente spoiler.'
locale_fr.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Spoiler public.'
locale_es.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Spoiler público.'
locale_ja.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> パブリックスポイラーメッセージ。'
locale_zh.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> 公共剧透消息。'
locale_hi.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> सार्वजनिक स्पॉइलर संदेश।'
locale_ar.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> رسالة حرق للجميع.'


# GROUP_GREETING_MESSAGE
locale_pt.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Olá, meu nome é %s! Obrigado por me adicionar em seu grupo\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Posso ajudá-lo a enviar mensagens privadas que apenas os usuarios escolhidos por você podem ver.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Para saber mais envie /start@%s e sinta-se à vontade para pedir ajuda em nosso '
    '<a href="t.me/pombomsgbotchannel">Canal oficial</a> e <a href="t.me/kylorensbot">Suporte</a> se você tiver alguma dúvida.'
)
locale_en.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Hello, my name is %s! Thanks for adding me to your group\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> I can help you send private messages that only the users you choose can see.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> To learn more send /start@%s and feel free to ask for help on our '
    '<a href="t.me/pombomsgbotchannel">Official channel</a> and <a href="t.me/kylorensbot">Support</a> if you have any questions.'
)
locale_ru.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Привет, меня зовут %s! Спасибо, что добавили меня в свою группу\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Я могу помочь вам отправлять личные сообщения, которые могут видеть только выбранные вами пользователи.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Чтобы узнать больше, отправьте /start@%s и не стесняйтесь обращаться за помощью в нашу '
    '<a href="t.me/pombomsgbotchannel">Официальный канал</a> и <a href="t.me/kylorensbot">Поддержка</a>, если у вас есть какие-либо вопросы.'
)
locale_uk.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Привіт, мене звати %s! Дякую за додавання мене до вашої групи\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Я можу допомогти вам надсилати приватні повідомлення, які можуть бачити тільки користувачі, яких ви виберете.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Щоб дізнатися більше, відправте /start@%s та не соромтеся звертатися за допомогою до нашого '
    '<a href="t.me/pombomsgbotchannel">Офіційного каналу</a> та <a href="t.me/kylorensbot">Підтримки</a>, якщо у вас є якісь питання.'
)
locale_de.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Hallo, mein Name ist %s! Danke, dass du mich zu deiner Gruppe hinzugefügt hast\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Ich kann dir helfen, private Nachrichten zu senden, die nur die von dir ausgewählten Benutzer sehen können.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Um mehr zu erfahren, senden Sie /start@%s und fragen Sie auf unserer '
    '<a href="t.me/pombomsgbotchannel">Offizieller Kanal</a> und <a href="t.me/kylorensbot">Support</a>, wenn Sie Fragen haben.'
)
locale_it.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Ciao, mi chiamo %s! Grazie per avermi aggiunto al tuo gruppo\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Posso aiutarti a inviare messaggi privati che solo gli utenti che scegli possono vedere.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Per saperne di più invia /start@%s e sentiti libero di chiedere aiuto sul nostro '
    '<a href="t.me/pombomsgbotchannel">Canale ufficiale</a> e <a href="t.me/kylorensbot">Assistenza</a> in caso di domande.'
)
locale_fr.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Bonjour, je m\'appelle %s! Merci de m\'avoir ajouté à votre groupe\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Je peux vous aider à envoyer des messages privés que seuls les utilisateurs que vous choisissez peuvent voir.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Pour en savoir plus, envoyez /start@%s et n\'hésitez pas à demander de l\'aide sur notre '
    '<a href="t.me/pombomsgbotchannel">Chaîne officielle</a> et <a href="t.me/kylorensbot">Assistance</a> si vous avez des questions.'
)
locale_es.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> ¡Hola, mi nombre es %s! Gracias por agregarme a tu grupo\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Puedo ayudarte a enviar mensajes privados que solo pueden ver los usuarios que elijas.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Para obtener más información, envíe /start@%s y no dude en solicitar ayuda en nuestro '
    '<a href="t.me/pombomsgbotchannel">Canal oficial</a> y <a href="t.me/kylorensbot">Soporte</a> si tiene alguna pregunta.'
)
locale_ja.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> こんにちは、私の名前は%sです！グループに追加していただきありがとうございます\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> あなたが選んだユーザーだけが見ることができるプライベートメッセージを送信するのを手伝うことができます。\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> もっと詳しく知りたい場合は、/start@%s を送信して、質問がある場合は '
    '<a href="t.me/pombomsgbotchannel">公式チャンネル</a>と<a href="t.me/kylorensbot">サポート</a>にお問い合わせください。'
)
locale_zh.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> 你好，我的名字是%s！感谢将我添加到你的群组中\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> 我可以帮助你发送仅有你选择的用户可以看到的私人消息\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> 要了解更多，请发送 /start@%s，并随时在我们的 '
    '<a href="t.me/pombomsgbotchannel">官方频道</a>和<a href="t.me/kylorensbot">支持</a>上寻求帮助，如果您有任何问题。'
)
locale_hi.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> नमस्ते, मेरा नाम %s है! आपके समूह में जोड़ने के लिए धन्यवाद\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> मैं आपको उन निश्चित उपयोगकर्ताओं तक निजी संदेश भेजने में मदद कर सकता हूँ, जो आप चुनते हैं।\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> और अधिक जानने के लिए /start@%s भेजें और अगर आपके पास कोई सवाल हो तो हमारे '
    '<a href="t.me/pombomsgbotchannel">आधिकारिक चैनल</a> और <a href="t.me/kylorensbot">सहायता</a> पर मदद के लिए पूछने में स्वतंत्र महसूस करें। '
)
locale_ar.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> مرحبًا ، اسمي %s! شكرًا على إضافتي إلى مجموعتك\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> يمكنني مساعدتك في إرسال رسائل خاصة يمكن للمستخدمين الذين تختارهم فقط رؤيتها.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> للمزيد من المعلومات ، أرسل /start@%s ولا تتردد في طلب المساعدة على '
    '<a href="t.me/pombomsgbotchannel">القناة الرسمية</a> و <a href="t.me/kylorensbot">الدعم</a> إذا كان لديك أي أسئلة.'
)

# INFO_MESSAGE
locale_pt.info_message = (
    '@pombomsgbot é um bot inline do Telegram para <b>manter suas mensagens privadas escondidas de olhares indiscretos.</b>\n\n'
    'Envie mensagens privadas para um ou mais usuários no grupo, e tenha conversas privadas sem precisar ir no chat privado.\n\n'
    'Clique nos botões abaixo e entre nosso canal oficial com explicações e atualizações, o se preferir me chame através do suporte.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Canal de figurinhas:</b> <a href="https://t.me/lbrabo">Clique aqui</a>\n'
)
locale_en.info_message = (
    '@pombomsgbot is an inline Telegram bot to <b>keep your private messages hidden from prying eyes.</b>\n\n'
    'Send private messages to one or more users in the group, and have private conversations without having to go to private chat.\n\n'
    'Click on the buttons below and enter our official channel with explanations and updates, or if you prefer, call me through support.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Sticker channel:</b> <a href="https://t.me/lbrabo">Click here</a>\n'
)
locale_ru.info_message = (
    '@pombomsgbot — это встроенный бот Telegram, <b>который скрывает ваши личные сообщения от посторонних глаз.</b>\n\n'
    'Отправляйте личные сообщения одному или нескольким пользователям в группе и ведите личные беседы, не переходя в приватный чат.\n\n'
    'Нажмите на кнопки ниже и войдите в наш официальный канал с объяснениями и обновлениями, или, если хотите, позвоните мне через службу поддержки.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Канал стикеров:</b> <a href="https://t.me/lbrabo">Нажмите здесь</a>\n'
)
locale_uk.info_message = (
    '@pombomsgbot — вбудований бот Telegram, який <b>приховує ваші особисті повідомлення від сторонніх очей.</b>\n\n'
    'Надсилайте приватні повідомлення одному чи кільком користувачам у групі та ведіть приватні розмови без необхідності переходити в приватний чат.\n\n'
    'Натисніть кнопки нижче та перейдіть на наш офіційний канал із поясненнями та оновленнями або, якщо хочете, зателефонуйте мені через службу підтримки.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Канал наклейок:</b> <a href="https://t.me/lbrabo">Натисніть тут</a>\n'
)
locale_de.info_message = (
    '@pombomsgbot ist ein Inline-Telegram-Bot, um <b>Ihre privaten Nachrichten vor neugierigen Blicken zu verbergen.</b>\n\n'
    'Private Nachrichten an einen oder mehrere Benutzer in der Gruppe senden und private Unterhaltungen führen, ohne in den privaten Chat gehen zu müssen.\n\n'
    'Klicken Sie auf die Schaltflächen unten und betreten Sie unseren offiziellen Kanal mit Erklärungen und Updates, oder rufen Sie mich über den Support an, wenn Sie dies vorziehen.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Stickerkanal:</b> <a href="https://t.me/lbrabo">Klicken Sie hier</a>\n'
)
locale_it.info_message = (
    '@pombomsgbot è un bot di Telegram integrato <b>per mantenere i tuoi messaggi privati nascosti da occhi indiscreti.</b>\n\n'
    'Invia messaggi privati a uno o più utenti del gruppo e conversa in privato senza dover accedere alla chat privata.\n\n'
    'Fai clic sui pulsanti in basso ed entra nel nostro canale ufficiale con spiegazioni e aggiornamenti, o se preferisci chiamami tramite il supporto.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Canale adesivi:</b> <a href="https://t.me/lbrabo">Clicca qui</a>\n'
)
locale_fr.info_message = (
    '@pombomsgbot est un bot Telegram en ligne <b>pour garder vos messages privés cachés des regards indiscrets.</b>\n\n'
    'Envoyer des messages privés à un ou plusieurs utilisateurs du groupe et avoir des conversations privées sans avoir à accéder au chat privé.\n\n'
    "Cliquez sur les boutons ci-dessous et accédez à notre chaîne officielle avec des explications et des mises à jour, ou si vous préférez, appelez-moi via l'assistance.\n\n"
'<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Chaîne d\'autocollants :</b> <a href="https://t.me/lbrabo">Cliquez ici</a>\n'
)
locale_es.info_message = (
    '@pombomsgbot es un bot de Telegram en línea para <b>mantener tus mensajes privados ocultos de miradas indiscretas.</b>\n\n'
    'Envía mensajes privados a uno o más usuarios del grupo y mantén conversaciones privadas sin tener que ir al chat privado.\n\n'
    'Haz clic en los botones de abajo e ingresa a nuestro canal oficial con explicaciones y actualizaciones, o si lo prefieres, llámame a través de soporte.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Canal de pegatinas:</b> <a href="https://t.me/lbrabo">Haz clic aquí</a>\n'
)
locale_ja.info_message = (
    '@pombomsgbot は、プライベート <b>メッセージを覗き見されないようにするためのインライン テレグラム ボットです。</b>\n\n'
    'グループ内の 1 人以上のユーザーにプライベート メッセージを送信し、プライベート チャットに行かなくてもプライベートな会話ができます。\n\n'
    '下のボタンをクリックして、説明と最新情報が記載された公式チャンネルにアクセスしてください。または、必要に応じて、サポートを通じて私に電話してください。\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>ステッカー チャンネル:</b> <a href="https://t.me/lbrabo">ここをクリックしてください</a>\n'
)
locale_zh.info_message = (
    '@pombomsgbot 是一個內嵌的 Telegram <b>機器人，可以保護您的私人消息不被窺視。</b>\n\n'
    '向群組中的一位或多位用戶發送私人消息，無需進入私人聊天即可進行私人對話。\n\n'
    '單擊下面的按鈕並進入我們的官方頻道，其中包含解釋和更新，或者如果您願意，請通過支持給我打電話。\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>貼紙頻道：</b> <a href="https://t.me/lbrabo">点击这里</a>\n'
)
locale_hi.info_message = (
    '@pombomsgbot आपके निजी संदेशों <b>को ताक-झांक करने वाली नज़रों से छुपाने के लिए एक इनलाइन टेलीग्राम बॉट है।</b>\n\n'
    'समूह में एक या अधिक उपयोगकर्ताओं को निजी संदेश भेजें, और निजी चैट पर जाए बिना निजी वार्तालाप करें।\n\n'
    'नीचे दिए गए बटनों पर क्लिक करें और स्पष्टीकरण और अपडेट के साथ हमारे आधिकारिक चैनल में प्रवेश करें, या यदि आप चाहें, तो मुझे समर्थन के माध्यम से कॉल करें।\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b> स्टिकर चैनल:</b> <a href="https://t.me/lbrabo">यहाँ क्लिक करें</a>\n'
)
locale_ar.info_message = (
    '@pombomsgbot هو روبوت Telegram <b>مضمّن لإخفاء رسائلك الخاصة عن أعين المتطفلين. </b>\n\n'
    'أرسل رسائل خاصة إلى مستخدم واحد أو أكثر في المجموعة ، واستمتع بمحادثات خاصة دون الحاجة إلى الذهاب إلى محادثة خاصة. \n\n'
    'انقر فوق الأزرار أدناه وادخل إلى قناتنا الرسمية مع الشروحات والتحديثات ، أو اتصل بي من خلال الدعم ، إذا كنت تفضل ذلك. \n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>قناة الملصق:</b> <a href="https://t.me/lbrabo">انقر هنا</a>\n'
)

# HOW_TO_USE
locale_pt.how_to_use = 'Como usar este bot?'
locale_en.how_to_use = 'How to use this bot?'
locale_ru.how_to_use = 'Как пользоваться этим ботом?'
locale_uk.how_to_use = 'Як користуватися цим ботом?'
locale_de.how_to_use = 'Wie geht das?'
locale_it.how_to_use = 'Come usare questo bot?'
locale_fr.how_to_use = 'Comment utiliser ce bot ?'
locale_es.how_to_use = '¿Cómo usar este bot?'
locale_ja.how_to_use = 'このボットの使い方'
locale_zh.how_to_use = '如何使用此机器人？'
locale_hi.how_to_use = 'इस बॉट का उपयोग कैसे करें?'
locale_ar.how_to_use = 'كيفية استخدام هذا الروبوت؟'


# TOO_LONG_DESCRIPTION
locale_pt.too_long_description = 'Reduza o tamanho da sua mensagem para que não exceda o limite de 200 caracteres. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_en.too_long_description = "Please shorten the length of your message so that it doesn't exceed the limit of 200 characters. <tg-emoji emoji-id='5447315718825582234'>🤏</tg-emoji>"
locale_ru.too_long_description = 'Пожалуйста, сократите длину вашего сообщения, чтобы она не превышала лимит в 200 символов. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_uk.too_long_description = 'Будь ласка, скоротіть довжину Вашого повідомлення, щоб вона не перевищувала ліміт в 200 символів. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_de.too_long_description = 'Bitte fasse dich etwas kürzer und überschreite das Limit von 200 Zeichen nicht. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_it.too_long_description = 'Perfavore accorcia la lunghezza del tuo messaggio in modo che non superi i 200 caratteri. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_fr.too_long_description = "Veuillez raccourcir la longueur de votre message pour qu'il ne dépasse pas la limite de 200 caractères. <tg-emoji emoji-id='5447315718825582234'>🤏</tg-emoji>"
locale_es.too_long_description = 'Por favor, acorte la longitud de su mensaje para que no exceda el límite de 200 caracteres. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_ja.too_long_description = 'メッセージの長さが200文字を超えないように、メッセージを短くしてください。<tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_zh.too_long_description = '请缩短消息的长度，以使其不超过200个字符的限制。<tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_hi.too_long_description = (
    'कृपया अपना संदेश इतना छोटा करें कि यह 200 अक्षर की सीमा से अधिक न हो। <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
)
locale_ar.too_long_description = (
    'يرجى تقصير طول رسالتك حتى لا يتجاوز الحد الأقصى للـ 200 حرف. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
)


# NOT_ALLOWED 
locale_pt.not_allowed = (
    'Você não tem permissão para visualizar este conteúdo.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
)
locale_en.not_allowed = 'You are not allowed to view this content.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_ru.not_allowed = 'Вам запрещено просматривать этот контент.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_uk.not_allowed = 'Вам заборонено переглядати цей контент.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_de.not_allowed = 'Dir ist nicht gestattet, diesen Inhalt zu lesen.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_it.not_allowed = 'Non hai il permesso per vedere questo messaggio.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_fr.not_allowed = "Vous n'êtes pas autorisé à voir ce contenu.<tg-emoji emoji-id='5197288647275071607'>🔐</tg-emoji>"
locale_es.not_allowed = 'No tienes permitido ver este contenido.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_ja.not_allowed = 'このコンテンツを表示することは許可されていません。<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_zh.not_allowed = '您无权查看此内容。<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_hi.not_allowed = 'आप इस सामग्री को देखने की अनुमति नहीं हैं।<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_ar.not_allowed = 'لا يُسمح لك بعرض هذا المحتوى.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'

# NOT_ACCESSIBLE 
locale_pt.not_accessible = 'Este conteúdo não está mais acessível.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_en.not_accessible = 'This content is no longer accessible.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_ru.not_accessible = 'Этот контент больше недоступен.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_uk.not_accessible = 'Цей контент більше недоступний.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_de.not_accessible = 'Der Inhalt ist nicht mehr sichtbar.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_it.not_accessible = 'Questo contenuto non è più accessibile.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_fr.not_accessible = "Ce contenu n'est plus accessible.<tg-emoji emoji-id='6039591820613127611'>🚫</tg-emoji>"
locale_es.not_accessible = 'Este contenido ya no está disponible.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_ja.not_accessible = 'このコンテンツはもうアクセスできません。<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_zh.not_accessible = '此内容不再可访问。<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_hi.not_accessible = 'यह सामग्री अब अधिक उपलब्ध नहीं है।<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_ar.not_accessible = 'لا يمكن الوصول إلى هذا المحتوى بعد الآن.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'


# VIEW  
locale_pt.view = 'Clique para ler'
locale_en.view = 'View'
locale_ru.view = 'Открыть'
locale_uk.view = 'Відкрити'
locale_de.view = 'Ansehen'
locale_it.view = 'Vedi'
locale_fr.view = 'Voir'
locale_es.view = 'Ver'
locale_ja.view = '表示'
locale_zh.view = '查看'
locale_hi.view = 'देखें'
locale_ar.view = 'عرض'


# AND_CONNECTOR
locale_pt.and_connector = 'ᴇ'
locale_en.and_connector = 'and'
locale_ru.and_connector = 'и'
locale_uk.and_connector = 'i'
locale_de.and_connector = '&'
locale_it.and_connector = 'e'
locale_fr.and_connector = 'et'
locale_es.and_connector = 'y'
locale_ja.and_connector = 'と'
locale_zh.and_connector = '和'
locale_hi.and_connector = 'और'
locale_ar.and_connector = 'و'


# Add Group
locale_pt.button_addGroup = ' Adicione-me em seu grupo'
locale_en.button_addGroup = ' Add me to your group'
locale_ru.button_addGroup = ' Добавьте меня в вашу группу'
locale_uk.button_addGroup = ' Додайте мене до вашої групи'
locale_de.button_addGroup = ' Füge mich zu deiner Gruppe hinzu'
locale_it.button_addGroup = ' Aggiungimi al tuo gruppo'
locale_fr.button_addGroup = ' Ajoutez-moi à votre groupe'
locale_es.button_addGroup = ' Añádeme a tu grupo'
locale_ja.button_addGroup = ' グループに私を追加してください'
locale_zh.button_addGroup = ' 把我加入你的群组中'
locale_hi.button_addGroup = ' मुझे अपने समूह में जोड़ें'
locale_ar.button_addGroup = ' أضفني إلى مجموعتك'

locale_pt.button_channel_message = ' Canal Oficial'
locale_en.button_channel_message = ' Official Channel'
locale_ru.button_channel_message = ' Официальный канал'
locale_uk.button_channel_message = ' Офіційний канал'
locale_de.button_channel_message = ' Offizieller Kanal'
locale_it.button_channel_message = ' Canale ufficiale'
locale_fr.button_channel_message = ' Chaîne officielle'
locale_es.button_channel_message = ' Canal oficial'
locale_ja.button_channel_message = ' 公式チャンネル'
locale_zh.button_channel_message = ' 官方频道'
locale_hi.button_channel_message = ' आधिकारिक चैनल'
locale_ar.button_channel_message = ' القناة الرسمية'

# Donate
locale_pt.button_donate_message = ' Doação'
locale_en.button_donate_message = ' Donation'
locale_ru.button_donate_message = ' Пожертвование'
locale_uk.button_donate_message = ' Пожертвування'
locale_de.button_donate_message = ' Spende'
locale_it.button_donate_message = ' Donazione'
locale_fr.button_donate_message = ' Don'
locale_es.button_donate_message = ' Donación'
locale_ja.button_donate_message = ' 寄付'
locale_zh.button_donate_message = ' 捐款'
locale_hi.button_donate_message = ' दान'
locale_ar.button_donate_message = ' هبة'

# Use
locale_pt.button_use_message = ' Grupo Oficial'
locale_en.button_use_message = ' Official chat'
locale_ru.button_use_message = ' Официальный чат'
locale_uk.button_use_message = ' Офіційний чат'
locale_de.button_use_message = ' Offizieller Chat'
locale_it.button_use_message = ' Chat ufficiale'
locale_fr.button_use_message = ' Chat officiel'
locale_es.button_use_message = ' Chat oficial'
locale_ja.button_use_message = ' 公式チャット'
locale_zh.button_use_message = ' 官方聊天'
locale_hi.button_use_message = ' आधिकारिक चैट'
locale_ar.button_use_message = ' الدردشة الرسمية'

# Support
locale_pt.button_support_message = ' Suporte'
locale_en.button_support_message = ' Support'
locale_ru.button_support_message = ' Поддержка'
locale_uk.button_support_message = ' Підтримка'
locale_de.button_support_message = ' Unterstützung'
locale_it.button_support_message = ' Supporto'
locale_fr.button_support_message = ' Support'
locale_es.button_support_message = ' Soporte'
locale_ja.button_support_message = ' サポート'
locale_zh.button_support_message = ' 支持'
locale_hi.button_support_message = ' समर्थन'
locale_ar.button_support_message = 'الدعم'

# Command Start
locale_pt.commands_start = 'Menu inicial'
locale_en.commands_start = 'Home Menu'
locale_ru.commands_start = 'Главное меню'
locale_uk.commands_start = 'Головне меню'
locale_de.commands_start = 'Startmenü'
locale_it.commands_start = 'Menu principale'
locale_fr.commands_start = 'Menu principal'
locale_es.commands_start = 'Menú principal'
locale_ja.commands_start = 'ホームメニュー'
locale_zh.commands_start = '主菜单'
locale_hi.commands_start = 'मुख्य मेनू'
locale_ar.commands_start = 'القائمة الرئيسية'

# Command Help
locale_pt.commands_help = 'Como usar o bot'
locale_en.commands_help = 'How to use the bot'
locale_ru.commands_help = 'Как использовать бота'
locale_uk.commands_help = 'Як використовувати бота'
locale_de.commands_help = 'Wie man den Bot verwendet'
locale_it.commands_help = 'Come utilizzare il bot'
locale_fr.commands_help = 'Comment utiliser le bot'
locale_es.commands_help = 'Cómo usar el bot'
locale_ja.commands_help = 'ボットの使用方法'
locale_zh.commands_help = '如何使用机器人'
locale_hi.commands_help = 'बॉट का उपयोग कैसे करें'
locale_ar.commands_help = 'كيفية استخدام البوت'

# Short description
locale_pt.short_description = 'É um bot embutido para manter suas mensagens privadas escondidas. \n\nCanal Oficial: @pombomsgbotchannel'
locale_en.short_description = 'Is an inline bot to keep your private messages hidden. \n\nOfficial Channel: @pombomsgbotchannel'
locale_ru.short_description = 'Бот для скрытия ваших личных сообщений от ненавязчивых глаз. \n\nОфициальный канал: @pombomsgbotchannel'
locale_uk.short_description = "Бот для приховування ваших особистих повідомлень від нав'язливих очей. \n\nОфіційний канал: @pombomsgbotchannel"
locale_de.short_description = 'Ein integrierter Bot zum Ausblenden Ihrer privaten Nachrichten. \n\nOffizieller Kanal: @pombomsgbotchannel'
locale_it.short_description = 'È un bot integrato per nascondere i tuoi messaggi privati. \n\nCanale ufficiale: @pombomsgbotchannel'
locale_fr.short_description = 'Est un robot en ligne pour protéger vos messages privés. \n\nChaîne officielle : @pombomsgbotchannel'
locale_es.short_description = 'Es un bot en línea para ocultar tus mensajes privados de miradas curiosas. \n\nCanal oficial: @pombomsgbotchannel'
locale_ja.short_description = 'このインラインボットは、あなたのプライベートメッセージを他人の目から隠すためのものです。 \n\n公式チャンネル：@pombomsgbotchannel'
locale_zh.short_description = (
    '这是一个内联机器人，用于保护您的私人消息不受窥探。 \n\n官方频道：@pombomsgbotchannel'
)
locale_hi.short_description = 'यह एक इंलाइन बॉट है जिसका उपयोग आपके निजी संदेशों को चुपा सकते हैं। \n\nआधिकृत चैनल: @pombomsgbotchannel'
locale_ar.short_description = 'هذا هو بوت مضمن لإخفاء رسائلك الخاصة عن الأعين الفضولية. \n\nالقناة الرسمية: @pombomsgbotchannel'

# description
locale_pt.description = 'A função do bot é enviar mensagens privadas para uma ou mais pessoas do grupo que você deseja. Não lemos a sua mensagem, privacidade e confiabilidade é o nosso lema. Canal Oficial: @pombomsgbotchannel'
locale_en.description = "The bot's function is to send private messages to one or more people in the group that you want. We don't read your message, privacy and reliability is our motto. Official Channel: @pombomsgbotchannel"
locale_ru.description = 'Функция бота - отправлять личные сообщения одному или нескольким людям в группе, которую вы хотите. Мы не читаем ваше сообщение, конфиденциальность и надежность - наш девиз. Официальный канал: @pombomsgbotchannel'
locale_uk.description = 'Функція бота - надсилати особисті повідомлення одній або декільком людям у групі, яку ви бажаєте. Ми не читаємо ваше повідомлення, конфіденційність та надійність - наш девіз. Офіційний канал: @pombomsgbotchannel'
locale_de.description = 'Die Funktion des Bots besteht darin, private Nachrichten an eine oder mehrere Personen in der Gruppe zu senden, die Sie möchten. Wir lesen Ihre Nachricht nicht, Privatsphäre und Zuverlässigkeit sind unser Motto. Offizieller Kanal: @pombomsgbotchannel'
locale_it.description = 'La funzione del bot è inviare messaggi privati a una o più persone nel gruppo che desideri. Non leggiamo il tuo messaggio, la privacy e la affidabilità sono il nostro motto. Canale ufficiale: @pombomsgbotchannel'
locale_fr.description = "La fonction du bot est d'envoyer des messages privés à une ou plusieurs personnes du groupe de votre choix. Nous ne lisons pas votre message, la confidentialité et la fiabilité sont notre devise. Chaîne officielle : @pombomsgbotchannel"
locale_es.description = 'La función del bot es enviar mensajes privados a una o más personas en el grupo que desees. No leemos tu mensaje, la privacidad y la confiabilidad son nuestro lema. Canal oficial: @pombomsgbotchannel'
locale_ja.description = 'このボットの機能は、希望するグループ内の1人以上の人々にプライベートメッセージを送信することです。私たちはあなたのメッセージを読みません、プライバシーと信頼性が私たちのモットーです。公式チャンネル：@pombomsgbotchannel'
locale_zh.description = '该机器人的功能是向您想要的群组中的一个或多个人发送私人消息。我们不会阅读您的消息，隐私和可靠性是我们的座右铭。官方频道：@pombomsgbotchannel'
locale_hi.description = 'बॉट का कार्य है कि आप चाहें तो समूह में एक या एक से अधिक व्यक्तियों को निजी संदेश भेजें। हम आपका संदेश नहीं पढ़ते, गोपनीयता और विश्वसनीयता हमारा मोटो है। आधिकृत चैनल: @pombomsgbotchannel'
locale_ar.description = 'وظيفة البوت هي إرسال رسائل خاصة إلى شخص واحد أو أكثر في المجموعة التي ترغب فيها. نحن لا نقرأ رسالتك، الخصوصية والموثوقية هما شعارنا. القناة الرسمية: @pombomsgbotchannel'

# Bot Name
locale_pt.bot_name = 'Pombo Correio'
locale_en.bot_name = 'Carrier Pigeon'
locale_ru.bot_name = 'Голубь-почтовик'
locale_uk.bot_name = 'Голуб-поштар'
locale_de.bot_name = 'Brieftaube'
locale_it.bot_name = 'Piccione postino'
locale_fr.bot_name = 'Pigeon voyageur'
locale_es.bot_name = 'Paloma mensajera'
locale_ja.bot_name = '運搬鳩'
locale_zh.bot_name = '信鸽'
locale_hi.bot_name = 'कैरियर पिजन'
locale_ar.bot_name = 'حمامة الحمل'

# HOW TO USE LINKS
locale_pt.how_to_use_link = 'https://telegra.ph/pombomsgbot-pt-11-05'
locale_en.how_to_use_link = 'https://telegra.ph/pombomsgbot-en-11-05'
locale_ru.how_to_use_link = 'https://telegra.ph/pombomsgbot-ru-11-05'
locale_uk.how_to_use_link = 'https://telegra.ph/pombomsgbot-uk-11-05'
locale_de.how_to_use_link = 'https://telegra.ph/pombomsgbot-de-11-05'
locale_it.how_to_use_link = 'https://telegra.ph/pombomsgbot-it-11-05'
locale_fr.how_to_use_link = 'https://telegra.ph/pombomsgbot-fr-11-05'
locale_es.how_to_use_link = 'https://telegra.ph/pombomsgbot-es-11-05'
locale_ja.how_to_use_link = 'https://telegra.ph/pombomsgbot-ja-11-05'
locale_zh.how_to_use_link = 'https://telegra.ph/pombomsgbot-zh-11-05'
locale_hi.how_to_use_link = 'https://telegra.ph/pombomsgbot-hi-11-06'
locale_ar.how_to_use_link = 'https://telegra.ph/pombomsgbot-ar-11-05'


# HOW TO USE TEXT
locale_pt.how_to_use_text = '<b>Como usar esse bot?</b>\n\nPara usar esse bot, basta digita <code>@pombomsgbot texto exemplo @user1 @user2 @user3</code>\n\nObs.: Você pode usar @Username ou @user_id\n\n• @pombomsgbot – menção inline do bot\n• texto exemplo – texto a ser ocultado\n• @user1 @user2 @user3 – lista de usuários no escopo\n\n<b>Modos disponíveis</b>\n\nspoiler – o conteúdo oculto pode ser visto por todos\npara – o conteúdo oculto só pode ser visto pelo autor e pelos usuários no escopo\nexceto – o conteúdo oculto pode ser visto por todos, exceto os usuários no escopo\n\n<b>Outras funcionalidades</b>\n\n<code>@pombomsgbot Acho que é hora de remover {name} deste chat. Não aguento mais esse palhaço.</code>\n\n<code>{username}</code> – nome de usuário do espectador (por exemplo, @kylorensbot)\n<code>{uid}</code> – UID do espectador (por exemplo, id837151456)\n<code>{lang}</code> – código de idioma do espectador (por exemplo, en ou pt-br)\n<code>{pid}</code> – ID da postagem (linha do banco de dados) (por exemplo, #32400360)\n<code>{created}</code> – carimbo de data/hora de criação da postagem (por exemplo, 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – contagem total de consultas inline enviadas pelo espectador (por exemplo, 42)\n<code>{first_interaction}</code> – carimbo de data/hora UTC precisa quando o espectador foi salvo no banco de dados pela primeira vez (por exemplo, 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – indica se o espectador já escreveu para o bot em bate-papo privado (por exemplo, Sim)\n<code>{utc}</code> – carimbo de data/hora UTC precisa (por exemplo, 2077-07-05 19:53:17.864156)\n<code>{date}</code> – data UTC atual (por exemplo, 2077-07-05)\n<code>{time}</code> – hora UTC atual (por exemplo, 19:53)\n<code>{name}</code> – nome completo do espectador (por exemplo, Big Floppa)\n<code>{first_name}</code> – primeiro nome do espectador (por exemplo, Big)\n<code>{last_name}</code> – sobrenome do espectador (por exemplo, Floppa)\n\n<a href="https://telegra.ph/pombomsgbot-pt-11-05">Saiba Mais</a>'
locale_en.how_to_use_text = "<b>How to use this bot?</b>\n\nTo use this bot, simply type <code>@pombomsgbot sample text @user1 @user2 @user3</code>\n\nNote: You can use @Username or @user_id\n\n• @pombomsgbot – inline mention of the bot\n• sample text – text to be hidden\n• @user1 @user2 @user3 – list of users in scope\n\n<b>Available Modes</b>\n\nspoiler – hidden content can be seen by everyone\nfor – hidden content can only be seen by the author and users in scope\nexcept – hidden content can be seen by everyone except users in scope\n\n<b>Other Features</b>\n\n<code>@pombomsgbot I guess it's time to remove {name} from this chat. Can't stand this clown anymore.</code>\n\n<code>{username}</code> – viewer's username (e.g., @kylorensbot)\n<code>{uid}</code> – viewer's UID (e.g., id837151456)\n<code>{lang}</code> – viewer's language code (e.g., en or pt-br)\n<code>{pid}</code> – post (DB row) ID (e.g., #32400360)\n<code>{created}</code> – post creation timestamp (e.g., 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – total count of inline queries sent by viewer (e.g., 42)\n<code>{first_interaction}</code> – precise UTC timestamp of when viewer was saved to the database for the first time (e.g., 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – indicates whether viewer has ever written to the bot in private chat (e.g., Yes)\n<code>{utc}</code> – precise UTC timestamp (e.g., 2077-07-05 19:53:17.864156)\n<code>{date}</code> – current UTC date (e.g., 2077-07-05)\n<code>{time}</code> – current UTC time (e.g., 19:53)\n<code>{name}</code> – viewer's full name (e.g., Big Floppa)\n<code>{first_name}</code> – viewer's first name (e.g., Big)\n<code>{last_name}</code> – viewer's last name (e.g., Floppa)\n\n<a href=\"https://telegra.ph/pombomsgbot-en-11-05\">Learn More</a>"
locale_ru.how_to_use_text = '<b>Как использовать этого бота?</b>\n\nЧтобы использовать этого бота, просто введите <code>@pombomsgbot пример текста @user1 @user2 @user3</code>\n\nПримечание: Вы можете использовать @ИмяПользователя или @user_id\n\n• @pombomsgbot – упоминание бота внутри текста\n• пример текста – текст, который нужно скрыть\n• @user1 @user2 @user3 – список пользователей в пределах видимости\n\n<b>Доступные режимы</b>\n\nспойлер – скрытый контент может быть виден всем\nдля – скрытый контент может видеть только автор и пользователи в пределах видимости\nкроме – скрытый контент может быть виден всем, кроме пользователей в пределах видимости\n\n<b>Другие функции</b>\n\n<code>@pombomsgbot Похоже, пришло время удалить {name} из этого чата. Больше не могу терпеть этого клоуна.</code>\n\n<code>{username}</code> – имя пользователя зрителя (например, @kylorensbot)\n<code>{uid}</code> – UID зрителя (например, id837151456)\n<code>{lang}</code> – код языка зрителя (например, en или pt-br)\n<code>{pid}</code> – ID сообщения (строка в БД) (например, #32400360)\n<code>{created}</code> – временная метка создания сообщения (например, 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – общее количество запросов встроенных запросов, отправленных зрителем (например, 42)\n<code>{first_interaction}</code> – точная временная метка UTC, когда зритель был впервые сохранен в базе данных (например, 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – указывает, писал ли зритель когда-либо боту в личном чате (например, Да)\n<code>{utc}</code> – точная временная метка UTC (например, 2077-07-05 19:53:17.864156)\n<code>{date}</code> – текущая дата UTC (например, 2077-07-05)\n<code>{time}</code> – текущее время UTC (например, 19:53)\n<code>{name}</code> – полное имя зрителя (например, Большой Флоппа)\n<code>{first_name}</code> – имя зрителя (например, Большой)\n<code>{last_name}</code> – фамилия зрителя (например, Флоппа)\n\n<a href="https://telegra.ph/pombomsgbot-ru-11-05">Узнать больше</a>'
locale_uk.how_to_use_text = "<b>Як використовувати цього бота?</b>\n\nДля використання цього бота просто введіть <code>@pombomsgbot приклад тексту @user1 @user2 @user3</code>\n\nПримітка: Ви можете використовувати @Ім'яКористувача або @user_id\n\n• @pombomsgbot – упоминання бота всередині тексту\n• приклад тексту – текст, який потрібно приховати\n• @user1 @user2 @user3 – список користувачів у межах видимості\n\n<b>Доступні режими</b>\n\nспойлер – прихований вміст можуть бачити всі\nдля – прихований вміст може бачити лише автор і користувачі у межах видимості\nкрім – прихований вміст можуть бачити всі, крім користувачів у межах видимості\n\n<b>Інші можливості</b>\n\n<code>@pombomsgbot Здається, час видалити {name} з цього чата. Більше не можу терпіти цього клоуна.</code>\n\n<code>{username}</code> – ім'я користувача глядача (наприклад, @kylorensbot)\n<code>{uid}</code> – UID глядача (наприклад, id837151456)\n<code>{lang}</code> – код мови глядача (наприклад, en або pt-br)\n<code>{pid}</code> – ID повідомлення (рядок у базі даних) (наприклад, #32400360)\n<code>{created}</code> – мітка часу створення повідомлення (наприклад, 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – загальна кількість вбудованих запитів, відправлених глядачем (наприклад, 42)\n<code>{first_interaction}</code> – точна мітка часу UTC, коли глядач був вперше збережений у базі даних (наприклад, 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – вказує, писав чи ні глядач коли-небудь боту у приватному чаті (наприклад, Так)\n<code>{utc}</code> – точна мітка часу UTC (наприклад, 2077-07-05 19:53:17.864156)\n<code>{date}</code> – поточна дата UTC (наприклад, 2077-07-05)\n<code>{time}</code> – поточний час UTC (наприклад, 19:53)\n<code>{name}</code> – повне ім'я глядача (наприклад, Великий Флоппа)\n<code>{first_name}</code> – ім'я глядача (наприклад, Великий)\n<code>{last_name}</code> – прізвище глядача (наприклад, Флоппа)\n\n<a href=\"https://telegra.ph/pombomsgbot-uk-11-05\">Дізнатися більше</a>"
locale_de.how_to_use_text = '<b>Wie benutzt man diesen Bot?</b>\n\nUm diesen Bot zu verwenden, geben Sie einfach ein <code>@pombomsgbot Beispieltext @user1 @user2 @user3</code>\n\nHinweis: Sie können @Benutzername oder @user_id verwenden\n\n• @pombomsgbot – Inline-Erwähnung des Bots\n• Beispieltext – zu verbergender Text\n• @user1 @user2 @user3 – Liste der Benutzer im Bereich\n\n<b>Verfügbare Modi</b>\n\nSpoiler – Versteckter Inhalt kann von allen gesehen werden\nfür – Versteckter Inhalt kann nur vom Autor und von Benutzern im Bereich gesehen werden\naußer – Versteckter Inhalt kann von allen außer den Benutzern im Bereich gesehen werden\n\n<b>Weitere Funktionen</b>\n\n<code>@pombomsgbot Ich denke, es ist Zeit, {name} aus diesem Chat zu entfernen. Kann diesen Clown nicht mehr ertragen.</code>\n\n<code>{username}</code> – Benutzername des Betrachters (z. B. @kylorensbot)\n<code>{uid}</code> – UID des Betrachters (z. B. id837151456)\n<code>{lang}</code> – Sprachcode des Betrachters (z. B. en oder pt-br)\n<code>{pid}</code> – Post (DB-Reihe) ID (z. B. #32400360)\n<code>{created}</code> – Zeitstempel der Post-Erstellung (z. B. 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – Gesamtanzahl der Inline-Abfragen, die vom Betrachter gesendet wurden (z. B. 42)\n<code>{first_interaction}</code> – genauer UTC-Zeitstempel, wann der Betrachter zum ersten Mal in der Datenbank gespeichert wurde (z. B. 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – zeigt an, ob der Betrachter jemals im privaten Chat an den Bot geschrieben hat (z. B. Ja)\n<code>{utc}</code> – genauer UTC-Zeitstempel (z. B. 2077-07-05 19:53:17.864156)\n<code>{date}</code> – aktuelles UTC-Datum (z. B. 2077-07-05)\n<code>{time}</code> – aktuelle UTC-Zeit (z. B. 19:53)\n<code>{name}</code> – vollständiger Name des Betrachters (z. B. Big Floppa)\n<code>{first_name}</code> – Vorname des Betrachters (z. B. Big)\n<code>{last_name}</code> – Nachname des Betrachters (z. B. Floppa)\n\n<a href="https://telegra.ph/pombomsgbot-de-11-05">Mehr erfahren</a>'
locale_it.how_to_use_text = "<b>Come usare questo bot?</b>\n\nPer utilizzare questo bot, basta digitare <code>@pombomsgbot testo esempio @user1 @user2 @user3</code>\n\nNota: È possibile utilizzare @NomeUtente o @user_id\n\n• @pombomsgbot – menzione inline del bot\n• testo esempio – testo da nascondere\n• @user1 @user2 @user3 – elenco degli utenti nel contesto\n\n<b>Modalità disponibili</b>\n\nspoiler – il contenuto nascosto può essere visto da tutti\nper – il contenuto nascosto può essere visto solo dall'autore e dagli utenti nel contesto\neccetto – il contenuto nascosto può essere visto da tutti tranne dagli utenti nel contesto\n\n<b>Altre funzionalità</b>\n\n<code>@pombomsgbot Penso sia ora di rimuovere {name} da questa chat. Non posso sopportare più questo pagliaccio.</code>\n\n<code>{username}</code> – nome utente dell'osservatore (es. @kylorensbot)\n<code>{uid}</code> – UID dell'osservatore (es. id837151456)\n<code>{lang}</code> – codice lingua dell'osservatore (es. en o pt-br)\n<code>{pid}</code> – ID del post (riga del DB) (es. #32400360)\n<code>{created}</code> – timestamp di creazione del post (es. 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – conteggio totale delle query inline inviate dall'osservatore (es. 42)\n<code>{first_interaction}</code> – timestamp preciso UTC di quando l'osservatore è stato salvato nel database per la prima volta (es. 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – indica se l'osservatore ha mai scritto al bot in chat privata (es. Sì)\n<code>{utc}</code> – timestamp preciso UTC (es. 2077-07-05 19:53:17.864156)\n<code>{date}</code> – data UTC corrente (es. 2077-07-05)\n<code>{time}</code> – ora UTC corrente (es. 19:53)\n<code>{name}</code> – nome completo dell'osservatore (es. Big Floppa)\n<code>{first_name}</code> – nome dell'osservatore (es. Big)\n<code>{last_name}</code> – cognome dell'osservatore (es. Floppa)\n\n<a href=\"https://telegra.ph/pombomsgbot-it-11-05\">Scopri di più</a>"
locale_fr.how_to_use_text = "<b>Comment utiliser ce bot ?</b>\n\nPour utiliser ce bot, il suffit de taper <code>@pombomsgbot texte exemple @user1 @user2 @user3</code>\n\nRemarque : Vous pouvez utiliser @NomUtilisateur ou @user_id\n\n• @pombomsgbot – mention en ligne du bot\n• texte exemple – texte à masquer\n• @user1 @user2 @user3 – liste des utilisateurs dans le champ\n\n<b> Modes disponibles</b>\n\nspoiler – le contenu caché peut être vu par tout le monde\npour – le contenu caché ne peut être vu que par l'auteur et les utilisateurs dans le champ\nexcepté – le contenu caché peut être vu par tout le monde sauf par les utilisateurs dans le champ\n\n<b> Autres fonctionnalités</b>\n\n<code>@pombomsgbot Je pense qu'il est temps de retirer {name} de ce chat. Je ne supporte plus ce clown.</code>\n\n<code>{username}</code> – nom d'utilisateur du spectateur (par exemple, @kylorensbot)\n<code>{uid}</code> – UID du spectateur (par exemple, id837151456)\n<code>{lang}</code> – code de langue du spectateur (par exemple, en ou pt-br)\n<code>{pid}</code> – ID du post (ligne DB) (par exemple, #32400360)\n<code>{created}</code> – timestamp de création du post (par exemple, 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – nombre total de requêtes inline envoyées par le spectateur (par exemple, 42)\n<code>{first_interaction}</code> – timestamp UTC précis lorsque le spectateur a été enregistré dans la base de données pour la première fois (par exemple, 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – indique si le spectateur a déjà écrit au bot en chat privé (par exemple, Oui)\n<code>{utc}</code> – timestamp UTC précis (par exemple, 2077-07-05 19:53:17.864156)\n<code>{date}</code> – date UTC actuelle (par exemple, 2077-07-05)\n<code>{time}</code> – heure UTC actuelle (par exemple, 19:53)\n<code>{name}</code> – nom complet du spectateur (par exemple, Big Floppa)\n<code>{first_name}</code> – prénom du spectateur (par exemple, Big)\n<code>{last_name}</code> – nom de famille du spectateur (par exemple, Floppa)\n\n<a href=\"https://telegra.ph/pombomsgbot-fr-11-05\">En savoir plus</a>"
locale_es.how_to_use_text = '<b>¿Cómo usar este bot?</b>\n\nPara usar este bot, simplemente escribe <code>@pombomsgbot texto de ejemplo @user1 @user2 @user3</code>\n\nNota: Puedes usar @NombreDeUsuario o @user_id\n\n• @pombomsgbot – mención en línea del bot\n• texto de ejemplo – texto a ocultar\n• @user1 @user2 @user3 – lista de usuarios en el ámbito\n\n<b>Modos disponibles</b>\n\nspoiler – el contenido oculto puede ser visto por todos\npara – el contenido oculto solo puede ser visto por el autor y por los usuarios en el ámbito\nexcepto – el contenido oculto puede ser visto por todos excepto los usuarios en el ámbito\n\n<b>Otras funcionalidades</b>\n\n<code>@pombomsgbot Creo que es hora de eliminar {name} de este chat. Ya no aguanto a este payaso.</code>\n\n<code>{username}</code> – nombre de usuario del espectador (por ejemplo, @kylorensbot)\n<code>{uid}</code> – UID del espectador (por ejemplo, id837151456)\n<code>{lang}</code> – código de idioma del espectador (por ejemplo, en o pt-br)\n<code>{pid}</code> – ID de la publicación (fila de DB) (por ejemplo, #32400360)\n<code>{created}</code> – marca de tiempo de creación de la publicación (por ejemplo, 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – recuento total de consultas en línea enviadas por el espectador (por ejemplo, 42)\n<code>{first_interaction}</code> – marca de tiempo UTC precisa de cuando el espectador fue guardado por primera vez en la base de datos (por ejemplo, 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – indica si el espectador alguna vez escribió al bot en chat privado (por ejemplo, Sí)\n<code>{utc}</code> – marca de tiempo UTC precisa (por ejemplo, 2077-07-05 19:53:17.864156)\n<code>{date}</code> – fecha UTC actual (por ejemplo, 2077-07-05)\n<code>{time}</code> – hora UTC actual (por ejemplo, 19:53)\n<code>{name}</code> – nombre completo del espectador (por ejemplo, Big Floppa)\n<code>{first_name}</code> – primer nombre del espectador (por ejemplo, Big)\n<code>{last_name}</code> – apellido del espectador (por ejemplo, Floppa)\n\n<a href="https://telegra.ph/pombomsgbot-es-11-05">Saber más</a>'
locale_ja.how_to_use_text = '<b>このボットの使い方は？</b>\n\nこのボットを使用するには、<code>@pombomsgbot サンプルテキスト @user1 @user2 @user3</code> と入力するだけです。\n\n注意：@ユーザー名 または @user_id を使用できます。\n\n• @pombomsgbot – ボットのインラインメンション\n• サンプルテキスト – 隠すテキスト\n• @user1 @user2 @user3 – スコープ内のユーザーリスト\n\n<b>利用可能なモード</b>\n\nスポイラー – 隠された内容は誰もが見ることができます\nfor – 隠された内容は作者とスコープ内のユーザーのみが見ることができます\nexcept – スコープ内のユーザーを除く全員が隠された内容を見ることができます\n\n<b>その他の機能</b>\n\n<code>@pombomsgbot {name} をこのチャットから削除する時間だと思います。もうこの道化師は我慢できません。</code>\n\n<code>{username}</code> – ユーザーのユーザー名（例：@kylorensbot）\n<code>{uid}</code> – ユーザーのUID（例：id837151456）\n<code>{lang}</code> – ユーザーの言語コード（例：enまたはpt-br）\n<code>{pid}</code> – 投稿（DBの行）のID（例：#32400360）\n<code>{created}</code> – 投稿作成のタイムスタンプ（例：2077-07-05 19:53:17.864156）\n<code>{queries}</code> – ユーザーが送信したインラインクエリの合計数（例：42）\n<code>{first_interaction}</code> – ユーザーが最初にデータベースに保存された正確なUTCタイムスタンプ（例：2077-07-05 19:53:17.864156）\n<code>{dialog}</code> – ユーザーが以前にボットにプライベートチャットで書き込んだかどうかを示します（例：Yes）\n<code>{utc}</code> – 正確なUTCタイムスタンプ（例：2077-07-05 19:53:17.864156）\n<code>{date}</code> – 現在のUTC日付（例：2077-07-05）\n<code>{time}</code> – 現在のUTC時刻（例：19:53）\n<code>{name}</code> – ユーザーのフルネーム（例：Big Floppa）\n<code>{first_name}</code> – ユーザーの名前（例：Big）\n<code>{last_name}</code> – ユーザーの姓（例：Floppa）\n\n<a href="https://telegra.ph/pombomsgbot-ja-11-05">詳細を見る</a>'
locale_zh.how_to_use_text = '<b>如何使用这个机器人？</b>\n\n要使用此机器人，只需键入 <code>@pombomsgbot 示例文本 @user1 @user2 @user3</code>\n\n注意：您可以使用 @用户名 或 @user_id\n\n• @pombomsgbot – 机器人的内联提及\n• 示例文本 – 要隐藏的文本\n• @user1 @user2 @user3 – 范围内的用户列表\n\n<b>可用模式</b>\n\n剧透 – 所有人都可以看到隐藏的内容\n给 – 只有作者和范围内的用户可以看到隐藏的内容\n除了 – 除范围内的用户外，所有人都可以看到隐藏的内容\n\n<b>其他功能</b>\n\n<code>@pombomsgbot 我想是时候将 {name} 从此聊天中移除了。再也受不了这个小丑了。</code>\n\n<code>{username}</code> – 观众的用户名（例如：@kylorensbot）\n<code>{uid}</code> – 观众的UID（例如：id837151456）\n<code>{lang}</code> – 观众的语言代码（例如：en或pt-br）\n<code>{pid}</code> – 帖子（DB行）ID（例如：#32400360）\n<code>{created}</code> – 帖子创建时间戳（例如：2077-07-05 19:53:17.864156）\n<code>{queries}</code> – 观众发送的内联查询总数（例如：42）\n<code>{first_interaction}</code> – 观众首次保存到数据库的精确UTC时间戳（例如：2077-07-05 19:53:17.864156）\n<code>{dialog}</code> – 指示观众是否曾经在私聊中向机器人写过（例如：是）\n<code>{utc}</code> – 精确的UTC时间戳（例如：2077-07-05 19:53:17.864156）\n<code>{date}</code> – 当前的UTC日期（例如：2077-07-05）\n<code>{time}</code> – 当前的UTC时间（例如：19:53）\n<code>{name}</code> – 观众的全名（例如：Big Floppa）\n<code>{first_name}</code> – 观众的名字（例如：Big）\n<code>{last_name}</code> – 观众的姓氏（例如：Floppa）\n\n<a href="https://telegra.ph/pombomsgbot-zh-11-05">了解更多</a>'
locale_hi.how_to_use_text = '<b>इस बॉट का उपयोग कैसे करें?</b>\n\nइस बॉट का उपयोग करने के लिए, <code>@pombomsgbot उदाहरण पाठ @user1 @user2 @user3</code> टाइप करें।\n\nध्यान दें: आप @उपयोगकर्तानाम या @user_id का उपयोग कर सकते हैं\n\n• @pombomsgbot – बॉट का इनलाइन संदर्भ\n• उदाहरण पाठ – छिपाने के लिए पाठ\n• @user1 @user2 @user3 – स्कोप में उपयोगकर्ता सूची\n\n<b>उपलब्ध मोड्स</b>\n\nस्पॉइलर – छिपी हुई सामग्री सभी द्वारा देखी जा सकती है\nfor – छिपी हुई सामग्री केवल लेखक और स्कोप में उपयोगकर्ता द्वारा देखी जा सकती है\nexcept – छिपी हुई सामग्री को स्कोप में उपयोगकर्ताओं को छोड़कर सभी देख सकते हैं\n\n<b>अन्य सुविधाएँ</b>\n\n<code>@pombomsgbot मुझे लगता है कि {name} को इस चैट से हटाने का समय हो गया है। इस पागल को और बर्दाश्त नहीं होता।</code>\n\n<code>{username}</code> – दर्शक का उपयोगकर्ता नाम (उदाहरण के लिए, @kylorensbot)\n<code>{uid}</code> – दर्शक का UID (उदाहरण के लिए, id837151456)\n<code>{lang}</code> – दर्शक का भाषा कोड (उदाहरण के लिए, en या pt-br)\n<code>{pid}</code> – पोस्ट (डीबी पंक्ति) आईडी (उदाहरण के लिए, #32400360)\n<code>{created}</code> – पोस्ट निर्माण टाइमस्टैम्प (उदाहरण के लिए, 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – दर्शक द्वारा भेजे गए इनलाइन क्वेरी की कुल संख्या (उदाहरण के लिए, 42)\n<code>{first_interaction}</code> – जब दर्शक को पहली बार डेटाबेस में सहेजा गया था, तो सटीक UTC टाइमस्टैम्प (उदाहरण के लिए, 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – दर्शक ने क्या कभी बॉट को निजी चैट में लिखा है, यह सूचित करता है (उदाहरण के लिए, हाँ)\n<code>{utc}</code> – सटीक UTC टाइमस्टैम्प (उदाहरण के लिए, 2077-07-05 19:53:17.864156)\n<code>{date}</code> – वर्तमान UTC तारीख (उदाहरण के लिए, 2077-07-05)\n<code>{time}</code> – वर्तमान UTC समय (उदाहरण के लिए, 19:53)\n<code>{name}</code> – दर्शक का पूरा नाम (उदाहरण के लिए, बड़ा फ्लोपा)\n<code>{first_name}</code> – दर्शक का पहला नाम (उदाहरण के लिए, बड़ा)\n<code>{last_name}</code> – दर्शक का अंतिम नाम (उदाहरण के लिए, फ्लोपा)\n\n<a href="https://telegra.ph/pombomsgbot-hi-11-06">और अधिक जानें</a>'
locale_ar.how_to_use_text = '<b>كيفية استخدام هذا البوت؟</b>\n\nلاستخدام هذا الروبوت، ببساطة اكتب <code>@pombomsgbot نص عينة @user1 @user2 @user3</code>\n\nملاحظة: يمكنك استخدام @اسم_المستخدم أو @user_id\n\n• @pombomsgbot – الإشارة المباشرة للروبوت\n• نص عينة – النص المراد إخفاؤه\n• @user1 @user2 @user3 – قائمة المستخدمين في النطاق\n\n<b>الأوضاع المتاحة</b>\n\nspoiler – يمكن رؤية المحتوى المخفي من قبل الجميع\nfor – يمكن رؤية المحتوى المخفي فقط من قبل الكاتب والمستخدمين في النطاق\nexcept – يمكن رؤية المحتوى المخفي من قبل الجميع باستثناء المستخدمين في النطاق\n\n<b>ميزات أخرى</b>\n\n<code>@pombomsgbot أعتقد أنه حان الوقت لإزالة {name} من هذه المحادثة. لا أستطيع تحمل هذا المهرج بعد الآن.</code>\n\n<code>{username}</code> – اسم المستخدم للمشاهد (مثال: @kylorensbot)\n<code>{uid}</code> – مُعرف المشاهد (مثال: id837151456)\n<code>{lang}</code> – رمز لغة المشاهد (مثال: en أو pt-br)\n<code>{pid}</code> – معرف المشاركة (صف القاعدة) (مثال: #32400360)\n<code>{created}</code> – الطابع الزمني لإنشاء المشاركة (مثال: 2077-07-05 19:53:17.864156)\n<code>{queries}</code> – إجمالي عدد الاستعلامات الداخلية التي تم إرسالها بواسطة المشاهد (مثال: 42)\n<code>{first_interaction}</code> – الطابع الزمني الدقيق للتوقيت العالمي المنسق عندما تم حفظ المشاهد في قاعدة البيانات لأول مرة (مثال: 2077-07-05 19:53:17.864156)\n<code>{dialog}</code> – يشير ما إذا كان المشاهد قد كتب إلى الروبوت في الدردشة الخاصة من قبل (مثال: نعم)\n<code>{utc}</code> – الطابع الزمني الدقيق للتوقيت العالمي المنسق (مثال: 2077-07-05 19:53:17.864156)\n<code>{date}</code> – التاريخ العالمي الحالي (مثال: 2077-07-05)\n<code>{time}</code> – الوقت العالمي الحالي (مثال: 19:53)\n<code>{name}</code> – اسم المشاهد الكامل (مثال: Big Floppa)\n<code>{first_name}</code> – الاسم الأول للمشاهد (مثال: Big)\n<code>{last_name}</code> – اسم العائلة للمشاهد (مثال: Floppa)\n\n<a href="https://telegra.ph/pombomsgbot-ar-11-05">تعلم المزيد</a>'

# Voltar
locale_pt.button_back = ' Voltar'
locale_en.button_back = ' Back'
locale_ru.button_back = ' Назад'
locale_uk.button_back = ' Назад'
locale_de.button_back = ' Zurück'
locale_it.button_back = ' Indietro'
locale_fr.button_back = ' Retour'
locale_es.button_back = ' Volver'
locale_ja.button_back = ' 戻る'
locale_zh.button_back = ' 返回'
locale_hi.button_back = ' वापस'
locale_ar.button_back = ' العودة'

# HOW_TO_USE
locale_pt.button_how_to_use = ' Como usar este bot?'
locale_en.button_how_to_use = ' How to use this bot?'
locale_ru.button_how_to_use = ' Как пользоваться этим ботом?'
locale_uk.button_how_to_use = ' Як користуватися цим ботом?'
locale_de.button_how_to_use = ' Wie geht das?'
locale_it.button_how_to_use = ' Come usare questo bot?'
locale_fr.button_how_to_use = ' Comment utiliser ce bot ?'
locale_es.button_how_to_use = ' ¿Cómo usar este bot?'
locale_ja.button_how_to_use = ' このボットの使い方'
locale_zh.button_how_to_use = ' 如何使用此机器人？'
locale_hi.button_how_to_use = ' इस बॉट का उपयोग कैसे करें?'
locale_ar.button_how_to_use = ' كيفية استخدام هذا الروبوت؟'

# ===== TURKISH (tr) =====

locale_tr.too_long_title = '😮 Mesajın çok uzun'
locale_tr.for_title = '💬 %s için'
locale_tr.except_title = '💬 %s hariç'
locale_tr.spoiler_title = '✅ Herkese göster'
locale_tr.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Üzgünüm, mesajın 200 karakter sınırını aştığı için gönderilemedi.'
locale_tr.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> %s için gizli mesaj.'
locale_tr.except_message = '💬 %s hariç herkese gizli mesaj.'
locale_tr.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Herkese açık mesaj.'
locale_tr.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Merhaba, adım %s! Beni grubunuza eklediğiniz için teşekkürler\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Seçtiğiniz kullanıcıların görebileceği gizli mesajlar göndermenize yardımcı olabilirim.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Daha fazla bilgi için /start@%s gönderin ve sorularınız için '
    '<a href="t.me/pombomsgbotchannel">Resmi Kanal</a> ve <a href="t.me/kylorensbot">Destek</a> sayfalarımıza başvurun.'
)
locale_tr.info_message = (
    '@pombomsgbot, <b>gizli mesajlarınızı meraklı gözlerden koruyan</b> bir Telegram inline botudur.\n\n'
    'Gruptaki bir veya birden fazla kullanıcıya gizli mesaj gönderin, özel sohbet açmadan özel konuşmalar yapın.\n\n'
    'Aşağıdaki düğmelere tıklayın ve resmi kanalımıza girin.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Stiker kanalı:</b> <a href="https://t.me/lbrabo">Buraya tıklayın</a>\n'
)
locale_tr.how_to_use = 'Bu bot nasıl kullanılır?'
locale_tr.too_long_description = 'Lütfen mesajınızın uzunluğunu 200 karakter sınırını aşmayacak şekilde kısaltın. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_tr.not_allowed = 'Bu içeriği görüntüleme izniniz yok.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_tr.not_accessible = 'Bu içeriğe artık erişilemiyor.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_tr.view = 'Görüntüle'
locale_tr.and_connector = 've'
locale_tr.button_addGroup = ' Grubuma ekle'
locale_tr.button_channel_message = ' Resmi Kanal'
locale_tr.button_donate_message = ' Bağış'
locale_tr.button_use_message = ' Resmi Grup'
locale_tr.button_support_message = ' Destek'
locale_tr.commands_start = 'Ana Menü'
locale_tr.commands_help = 'Bot nasıl kullanılır'
locale_tr.short_description = 'Gizli mesajlarınızı meraklı gözlerden koruyan bir inline bot.\n\nResmi Kanal: @pombomsgbotchannel'
locale_tr.description = 'Botun işlevi, istediğiniz gruptaki bir veya daha fazla kişiye özel mesaj göndermektir. Mesajınızı okumuyoruz, gizlilik ve güvenilirlik bizim ilkemizdir. Resmi Kanal: @pombomsgbotchannel'
locale_tr.bot_name = 'Posta Güvercini'
locale_tr.how_to_use_link = 'https://telegra.ph/pombomsgbot-en-11-05'
locale_tr.how_to_use_text = '<b>Bu bot nasıl kullanılır?</b>\n\nBu botu kullanmak için: <code>@pombomsgbot örnek metin @kullanici1 @kullanici2</code>\n\nNot: @kullaniciadı veya id kullanabilirsiniz\n\n<b>Kullanılabilir Modlar</b>\n\nspoiler – gizli içerik herkesçe görülebilir\niçin – gizli içerik yalnızca yazar ve kapsam içindeki kullanıcılar tarafından görülebilir\nhariç – gizli içerik kapsam dışındaki herkes tarafından görülebilir\n\n<a href="https://telegra.ph/pombomsgbot-en-11-05">Daha fazla bilgi</a>'
locale_tr.button_back = ' Geri'
locale_tr.button_how_to_use = ' Bu bot nasıl kullanılır?'

# ===== INDONESIAN (id) =====

locale_id.too_long_title = '😮 Pesanmu terlalu panjang'
locale_id.for_title = '💬 Untuk %s'
locale_id.except_title = '💬 Kecuali %s'
locale_id.spoiler_title = '✅ Tampilkan ke semua'
locale_id.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Maaf, pesanmu tidak dapat dikirim karena melebihi batas 200 karakter.'
locale_id.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Pesan rahasia untuk %s.'
locale_id.except_message = '💬 Pesan rahasia untuk semua kecuali %s.'
locale_id.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Pesan spoiler publik.'
locale_id.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Halo, namaku %s! Terima kasih telah menambahkanku ke grupmu\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Aku bisa membantumu mengirim pesan rahasia yang hanya bisa dilihat oleh pengguna yang kamu pilih.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Untuk mengetahui lebih lanjut kirim /start@%s dan jangan ragu untuk meminta bantuan di '
    '<a href="t.me/pombomsgbotchannel">Saluran Resmi</a> dan <a href="t.me/kylorensbot">Dukungan</a> kami.'
)
locale_id.info_message = (
    '@pombomsgbot adalah bot Telegram inline untuk <b>menyembunyikan pesan pribadimu dari mata-mata.</b>\n\n'
    'Kirim pesan rahasia ke satu atau lebih pengguna di grup tanpa harus masuk ke obrolan privat.\n\n'
    'Klik tombol di bawah dan masuk ke saluran resmi kami.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Saluran stiker:</b> <a href="https://t.me/lbrabo">Klik di sini</a>\n'
)
locale_id.how_to_use = 'Bagaimana cara menggunakan bot ini?'
locale_id.too_long_description = 'Tolong persingkat pesanmu agar tidak melebihi batas 200 karakter. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_id.not_allowed = 'Kamu tidak diizinkan melihat konten ini.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_id.not_accessible = 'Konten ini tidak lagi dapat diakses.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_id.view = 'Lihat'
locale_id.and_connector = 'dan'
locale_id.button_addGroup = ' Tambahkan ke grupku'
locale_id.button_channel_message = ' Saluran Resmi'
locale_id.button_donate_message = ' Donasi'
locale_id.button_use_message = ' Grup Resmi'
locale_id.button_support_message = ' Dukungan'
locale_id.commands_start = 'Menu Utama'
locale_id.commands_help = 'Cara menggunakan bot'
locale_id.short_description = 'Bot inline untuk menyembunyikan pesan pribadimu.\n\nSaluran Resmi: @pombomsgbotchannel'
locale_id.description = 'Fungsi bot ini adalah mengirim pesan rahasia ke satu atau lebih orang di grup yang kamu inginkan. Kami tidak membaca pesanmu, privasi dan keandalan adalah motto kami. Saluran Resmi: @pombomsgbotchannel'
locale_id.bot_name = 'Merpati Pos'
locale_id.how_to_use_link = 'https://telegra.ph/pombomsgbot-en-11-05'
locale_id.how_to_use_text = '<b>Bagaimana cara menggunakan bot ini?</b>\n\nKetik: <code>@pombomsgbot teks contoh @pengguna1 @pengguna2</code>\n\nCatatan: Kamu dapat menggunakan @NamaPengguna atau id\n\n<b>Mode yang tersedia</b>\n\nspoiler – konten tersembunyi bisa dilihat semua orang\nuntuk – konten tersembunyi hanya bisa dilihat penulis dan pengguna dalam cakupan\nkecuali – konten tersembunyi bisa dilihat semua orang kecuali pengguna dalam cakupan\n\n<a href="https://telegra.ph/pombomsgbot-en-11-05">Pelajari lebih lanjut</a>'
locale_id.button_back = ' Kembali'
locale_id.button_how_to_use = ' Bagaimana cara menggunakan bot ini?'

# ===== PERSIAN / FARSI (fa) =====

locale_fa.too_long_title = '😮 پیام شما خیلی طولانی است'
locale_fa.for_title = '💬 برای %s'
locale_fa.except_title = '💬 به جز %s'
locale_fa.spoiler_title = '✅ نمایش به همه'
locale_fa.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> متأسفم، پیام شما به دلیل تجاوز از حد ۲۰۰ کاراکتر ارسال نشد.'
locale_fa.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> پیام محرمانه برای %s.'
locale_fa.except_message = '💬 پیام محرمانه برای همه به جز %s.'
locale_fa.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> پیام عمومی برای همه.'
locale_fa.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> سلام، اسمم %s است! ممنون که مرا به گروهتان اضافه کردید\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> می‌توانم به شما کمک کنم پیام‌های محرمانه‌ای ارسال کنید که فقط کاربران انتخابی شما بتوانند ببینند.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> برای اطلاعات بیشتر /start@%s را ارسال کنید و در صورت سؤال به '
    '<a href="t.me/pombomsgbotchannel">کانال رسمی</a> و <a href="t.me/kylorensbot">پشتیبانی</a> ما مراجعه کنید.'
)
locale_fa.info_message = (
    '@pombomsgbot یک ربات inline تلگرام برای <b>مخفی کردن پیام‌های خصوصی از چشمان کنجکاو است.</b>\n\n'
    'پیام‌های خصوصی را به یک یا چند کاربر در گروه ارسال کنید.\n\n'
    'روی دکمه‌های زیر کلیک کنید و به کانال رسمی ما بپیوندید.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>کانال استیکر:</b> <a href="https://t.me/lbrabo">اینجا کلیک کنید</a>\n'
)
locale_fa.how_to_use = 'چطور از این ربات استفاده کنم؟'
locale_fa.too_long_description = 'لطفاً پیام خود را کوتاه‌تر کنید تا از ۲۰۰ کاراکتر تجاوز نکند. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_fa.not_allowed = 'شما مجاز به مشاهده این محتوا نیستید.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_fa.not_accessible = 'این محتوا دیگر قابل دسترسی نیست.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_fa.view = 'مشاهده'
locale_fa.and_connector = 'و'
locale_fa.button_addGroup = ' به گروهم اضافه کن'
locale_fa.button_channel_message = ' کانال رسمی'
locale_fa.button_donate_message = ' کمک مالی'
locale_fa.button_use_message = ' گروه رسمی'
locale_fa.button_support_message = ' پشتیبانی'
locale_fa.commands_start = 'منوی اصلی'
locale_fa.commands_help = 'نحوه استفاده از ربات'
locale_fa.short_description = 'یک ربات inline برای مخفی کردن پیام‌های خصوصی شما.\n\nکانال رسمی: @pombomsgbotchannel'
locale_fa.description = 'وظیفه این ربات ارسال پیام‌های خصوصی به یک یا چند نفر در گروه است. پیام شما را نمی‌خوانیم، حریم خصوصی و قابلیت اطمینان شعار ماست. کانال رسمی: @pombomsgbotchannel'
locale_fa.bot_name = 'کبوتر نامه‌بر'
locale_fa.how_to_use_link = 'https://telegra.ph/pombomsgbot-en-11-05'
locale_fa.how_to_use_text = '<b>چطور از این ربات استفاده کنم؟</b>\n\nبرای استفاده تایپ کنید: <code>@pombomsgbot متن نمونه @کاربر1 @کاربر2</code>\n\n<b>حالت‌های موجود</b>\n\nspoiler – محتوای پنهان برای همه قابل مشاهده است\nبرای – محتوای پنهان فقط توسط نویسنده و کاربران در حوزه دیده می‌شود\nبه جز – محتوای پنهان توسط همه به جز کاربران در حوزه دیده می‌شود\n\n<a href="https://telegra.ph/pombomsgbot-en-11-05">بیشتر بدانید</a>'
locale_fa.button_back = ' برگشت'
locale_fa.button_how_to_use = ' چطور از این ربات استفاده کنم؟'

# ===== KOREAN (ko) =====

locale_ko.too_long_title = '😮 메시지가 너무 깁니다'
locale_ko.for_title = '💬 %s에게'
locale_ko.except_title = '💬 %s 제외'
locale_ko.spoiler_title = '✅ 모두에게 보이기'
locale_ko.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> 죄송합니다. 200자 제한을 초과하여 메시지를 보낼 수 없습니다.'
locale_ko.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> %s에게 보내는 비밀 메시지.'
locale_ko.except_message = '💬 %s을(를) 제외한 모두에게 보내는 비밀 메시지.'
locale_ko.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> 공개 스포일러 메시지.'
locale_ko.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> 안녕하세요, 저는 %s입니다! 그룹에 추가해 주셔서 감사합니다\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> 선택한 사용자만 볼 수 있는 비밀 메시지를 보내는 데 도움을 드릴 수 있습니다.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> 더 알고 싶으시면 /start@%s를 보내시고 질문이 있으시면 '
    '<a href="t.me/pombomsgbotchannel">공식 채널</a>과 <a href="t.me/kylorensbot">지원</a>에 문의하세요.'
)
locale_ko.info_message = (
    '@pombomsgbot은 <b>비밀 메시지를 엿보는 눈으로부터 숨기는</b> 텔레그램 인라인 봇입니다.\n\n'
    '그룹의 한 명 이상의 사용자에게 비밀 메시지를 보내고 개인 채팅에 가지 않고도 사적인 대화를 나눌 수 있습니다.\n\n'
    '아래 버튼을 클릭하고 공식 채널에서 설명과 업데이트를 확인하세요.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>스티커 채널:</b> <a href="https://t.me/lbrabo">여기 클릭</a>\n'
)
locale_ko.how_to_use = '이 봇은 어떻게 사용하나요?'
locale_ko.too_long_description = '메시지 길이를 200자 이내로 줄여주세요. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_ko.not_allowed = '이 콘텐츠를 볼 권한이 없습니다.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_ko.not_accessible = '이 콘텐츠에 더 이상 액세스할 수 없습니다.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_ko.view = '보기'
locale_ko.and_connector = '그리고'
locale_ko.button_addGroup = ' 내 그룹에 추가'
locale_ko.button_channel_message = ' 공식 채널'
locale_ko.button_donate_message = ' 후원'
locale_ko.button_use_message = ' 공식 그룹'
locale_ko.button_support_message = ' 지원'
locale_ko.commands_start = '홈 메뉴'
locale_ko.commands_help = '봇 사용 방법'
locale_ko.short_description = '비밀 메시지를 숨기는 인라인 봇.\n\n공식 채널: @pombomsgbotchannel'
locale_ko.description = '봇의 기능은 원하는 그룹에서 한 명 이상의 사람에게 비밀 메시지를 보내는 것입니다. 메시지를 읽지 않으며, 개인 정보 보호와 신뢰성이 우리의 모토입니다. 공식 채널: @pombomsgbotchannel'
locale_ko.bot_name = '전령 비둘기'
locale_ko.how_to_use_link = 'https://telegra.ph/pombomsgbot-en-11-05'
locale_ko.how_to_use_text = '<b>이 봇은 어떻게 사용하나요?</b>\n\n사용법: <code>@pombomsgbot 샘플 텍스트 @사용자1 @사용자2</code>\n\n참고: @사용자명 또는 id를 사용할 수 있습니다\n\n<b>사용 가능한 모드</b>\n\nspoiler – 숨겨진 내용을 모두가 볼 수 있습니다\nfor – 숨겨진 내용은 작성자와 범위 내 사용자만 볼 수 있습니다\nexcept – 범위 내 사용자를 제외한 모든 사람이 숨겨진 내용을 볼 수 있습니다\n\n<a href="https://telegra.ph/pombomsgbot-en-11-05">자세히 알아보기</a>'
locale_ko.button_back = ' 뒤로'
locale_ko.button_how_to_use = ' 이 봇은 어떻게 사용하나요?'

# ===== POLISH (pl) =====

locale_pl.too_long_title = '😮 Twoja wiadomość jest za długa'
locale_pl.for_title = '💬 Dla %s'
locale_pl.except_title = '💬 Z wyjątkiem %s'
locale_pl.spoiler_title = '✅ Pokaż wszystkim'
locale_pl.too_long_message = '<tg-emoji emoji-id="5235748511747681307">🥺</tg-emoji> Przepraszam, wiadomość nie może być wysłana, ponieważ przekracza limit 200 znaków.'
locale_pl.for_message = '<tg-emoji emoji-id="5197288647275071607">🔒</tg-emoji> Prywatna wiadomość dla %s.'
locale_pl.except_message = '💬 Prywatna wiadomość dla wszystkich z wyjątkiem %s.'
locale_pl.spoiler_message = '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> Publiczna wiadomość spoiler.'
locale_pl.group_greeting_message = (
    '<tg-emoji emoji-id="5938028303762853509">👋</tg-emoji> Cześć, mam na imię %s! Dziękuję za dodanie mnie do grupy\n\n'
    '<tg-emoji emoji-id="4969923081603645985">🗺️</tg-emoji> Mogę pomóc Ci wysyłać prywatne wiadomości, które mogą zobaczyć tylko wybrani przez Ciebie użytkownicy.\n\n'
    '<tg-emoji emoji-id="5388787654022148728">🔱</tg-emoji> Aby dowiedzieć się więcej, wyślij /start@%s i nie wahaj się pytać o pomoc na naszym '
    '<a href="t.me/pombomsgbotchannel">Oficjalnym kanale</a> i <a href="t.me/kylorensbot">Wsparciu</a>.'
)
locale_pl.info_message = (
    '@pombomsgbot to inline bot Telegram, aby <b>ukryć prywatne wiadomości przed wścibskimi oczami.</b>\n\n'
    'Wysyłaj prywatne wiadomości do jednego lub więcej użytkowników w grupie bez konieczności przechodzenia do prywatnego czatu.\n\n'
    'Kliknij poniższe przyciski i wejdź na nasz oficjalny kanał.\n\n'
    '<tg-emoji emoji-id="5258513401784573443">👥</tg-emoji> <b>Kanał ze naklejkami:</b> <a href="https://t.me/lbrabo">Kliknij tutaj</a>\n'
)
locale_pl.how_to_use = 'Jak korzystać z tego bota?'
locale_pl.too_long_description = 'Proszę skróć wiadomość, aby nie przekraczała limitu 200 znaków. <tg-emoji emoji-id="5447315718825582234">🤏</tg-emoji>'
locale_pl.not_allowed = 'Nie masz uprawnień do wyświetlania tej treści.<tg-emoji emoji-id="5197288647275071607">🔐</tg-emoji>'
locale_pl.not_accessible = 'Ta treść jest już niedostępna.<tg-emoji emoji-id="6039591820613127611">🚫</tg-emoji>'
locale_pl.view = 'Wyświetl'
locale_pl.and_connector = 'i'
locale_pl.button_addGroup = ' Dodaj do grupy'
locale_pl.button_channel_message = ' Oficjalny kanał'
locale_pl.button_donate_message = ' Dotacja'
locale_pl.button_use_message = ' Oficjalna grupa'
locale_pl.button_support_message = ' Wsparcie'
locale_pl.commands_start = 'Menu główne'
locale_pl.commands_help = 'Jak używać bota'
locale_pl.short_description = 'Inline bot do ukrywania prywatnych wiadomości.\n\nOfficjalny kanał: @pombomsgbotchannel'
locale_pl.description = 'Funkcją bota jest wysyłanie prywatnych wiadomości do jednej lub więcej osób w wybranej grupie. Nie czytamy Twoich wiadomości, prywatność i niezawodność to nasze motto. Oficjalny kanał: @pombomsgbotchannel'
locale_pl.bot_name = 'Gołąb pocztowy'
locale_pl.how_to_use_link = 'https://telegra.ph/pombomsgbot-en-11-05'
locale_pl.how_to_use_text = '<b>Jak korzystać z tego bota?</b>\n\nWpisz: <code>@pombomsgbot przykładowy tekst @uzytkownik1 @uzytkownik2</code>\n\nUwaga: Możesz użyć @NazwaUżytkownika lub id\n\n<b>Dostępne tryby</b>\n\nspoiler – ukryta treść jest widoczna dla wszystkich\ndla – ukryta treść widoczna tylko dla autora i użytkowników w zakresie\nz wyjątkiem – ukryta treść widoczna dla wszystkich z wyjątkiem użytkowników w zakresie\n\n<a href="https://telegra.ph/pombomsgbot-en-11-05">Dowiedz się więcej</a>'
locale_pl.button_back = ' Wstecz'
locale_pl.button_how_to_use = ' Jak korzystać z tego bota?'
