from data import bot, db
from telebot.types import Message

@bot.message_handler(commands=['start'], chat_types='private')
def welcome(message: Message):
    chat_id = message.from_user.id
    db.insert_telegram_id(chat_id)
    bot.send_message(chat_id, f'Assalomu alaykum hurmatli {message.from_user.first_name}, botga xush kelibsiz!😊\n'
                              f'<b>Pdf</b> formatiga o\'tkazish uchun <b>word</b> fayl yuboring!')