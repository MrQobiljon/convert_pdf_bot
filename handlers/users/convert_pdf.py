from data import bot, db
from telebot.types import Message
import os
from docx2pdf import convert

@bot.message_handler(content_types=['document'])
def get_document(message: Message):
    document_name = message.document.file_name.split('.')
    if document_name[-1] in ['docx']:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'file' + '/' + message.document.file_name

        with open(src, mode='wb') as file:
            file.write(downloaded_file)

        pdf_name = document_name[0] + '.pdf'
        convert(src, 'file' + '/' + pdf_name)

        pdf = open('file/' + pdf_name, mode='rb')
        bot.send_document(message.from_user.id, document=pdf, caption='Bizning botimizdan foydalaganligingiz uchun rahmat!\n👉 <a href="https://t.me/convert_word_to_pdf_bot">Bot linki</a>')
        pdf.close()
        os.remove('file/' + message.document.file_name)
        os.remove('file/' + pdf_name)
