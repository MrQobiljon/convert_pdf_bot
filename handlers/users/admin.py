from telebot.types import Message
from data.loader import bot
from config import ADMINS
from .rec import get_rec


@bot.message_handler(commands=['rec'], chat_types='private')
def rec(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    for admin in ADMINS:
        if from_user_id == admin:
            msg = bot.send_message(chat_id, f"Assalomu alaykum, {message.from_user.first_name}!\n"
                                            f"Reklamani jo'nating 😊")
            bot.register_next_step_handler(msg, get_rec)

