from data import bot, db
import handlers
db.create_user_table()



if __name__ == '__main__':
    bot.infinity_polling()
