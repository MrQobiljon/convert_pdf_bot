from telebot.types import Message, ReplyKeyboardRemove
from data.loader import bot, db
from keyboards.default import confirmation

data = {}


def get_rec(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    message_id = message.message_id

    data[from_user_id] = {'message_id': message_id}

    msg = bot.send_message(chat_id, f"Reklamani jo'natishni xoxlaysizmi? 🤓", reply_markup=confirmation())
    bot.register_next_step_handler(msg, send_rec)

def send_rec(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    bot.send_sticker(chat_id, 'CAACAgIAAxkBAAIIGWMzTSoHCCdKj6mAlFV58ETvvRAYAAJOAQACFkJrCm3VFOE7anCCKgQ', reply_markup=ReplyKeyboardRemove())
    message_id = data[from_user_id]['message_id']
    if message.text == 'Xa':
        users = db.select_telegram_id()
        for user in users:
            try:
                bot.copy_message(user[0], from_user_id, message_id)
            except Exception as e:
                pass
        bot.send_message(chat_id, f"Reklama jo'natildi 😊")
    elif message.text == "Yo'q":
        del data[from_user_id]['message_id']
        bot.send_message(chat_id, f"Reklama jo'natilmadi.\n"
                                  f"Reklamani qayta jo'natish uchun /rec komandasni bosib, so'ng reklamani yuboring!")
    bot.delete_message(chat_id, message_id + 3)