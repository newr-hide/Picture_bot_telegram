FROM python:3.11-slim

# Установка зависимостей
RUN pip install --upgrade pip
RUN pip install telebot
RUN pip install Pillow

# Копирование файлов приложения
COPY . /app/
WORKDIR /app

# Запуск приложения
CMD ["python", "main.py"]