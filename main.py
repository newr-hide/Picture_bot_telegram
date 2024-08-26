import telebot
from PIL import Image, ImageDraw
import config
import fonts
from datetime import datetime
import random

token = config.TOKEN

# достаем дату и время для названия картинки
dt_picture = datetime.now()
format_dt = dt_picture.strftime('%Y-%m-%d_%H-%M_')

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.photo:
        user_id = message.chat.id
        print(user_id)
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        save_path = 'photo.jpg'
        with open('signature.txt','r', encoding='utf-8') as signature:
            var_text = signature.readlines()
            random_text = random.choice(var_text)
           # print(random_text)
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        img = Image.open('photo.jpg')
        draw = ImageDraw.Draw(img)

        # # Рисуем текст на изображении
        draw.text( (10, 10), random_text, (255, 255, 0), font=fonts.font_lobster)
        title_pic = f'{format_dt}_{user_id}'
        img.save(rf'{config.address}{title_pic}.jpg') # Путь до картинки настраивается в файле config пользователем бота
        global global_var_title_image
        global_var_title_image = (rf'{config.address}{title_pic}.jpg')

        # Отправляем изменённое изображение пользователю
        bot.send_photo(
            message.chat.id,
            photo=open(rf'{config.address}{title_pic}.jpg', 'rb')
        )
#Отправка в канал вашей картинки
@bot.message_handler(func=lambda message: message.text == "Отправить в канал")
def send_community(message, id_canal=config.id_canal):

    bot.send_photo(id_canal, open(global_var_title_image,'rb'))
    bot.send_message(chat_id=message.chat.id, text='Картинка отправлена')



if __name__ == '__main__':
    print("Bot is running!")
    bot.polling()




