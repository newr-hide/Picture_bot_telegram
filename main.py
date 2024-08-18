import telebot
from PIL import Image, ImageDraw

# Получаем токен доступа
import config

token = config.TOKEN

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.photo:
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        save_path = 'photo.jpg'
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        img = Image.open(downloaded_file)
        draw = ImageDraw.Draw(img)
        # Рисуем текст на изображении
        draw.text((10, 10), "Красивоt фото", (255, 255, 0))
        # Отправляем изменённое изображение пользователю
        bot.send_photo(
            message.chat.id,
            photo,
            caption="Красивоt фото"
         )

bot.polling()
