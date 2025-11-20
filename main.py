import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('Your Token')





# ----- Создание кнопок -----
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # --- Можно вывести кнопку таким вариантом через "add" ---
    markup.add(types.InlineKeyboardButton('Перейти на сайт "Яндекс Дзен"', url='https://dzen.ru/?yredirect=true&clid=2270456&win=577'))

    # --- А можно и таким способом через "row" ---
    # --- Этот вариант позволяет выставлять кнопки в своем порядке когда способ выше нет ---
    button_2 = types.InlineKeyboardButton('Перейти на сайт "Кинопоиск"', url='https://www.kinopoisk.ru/')
    markup.row(button_2)

    # --- Этот вариант выставит кнопки в ряд ---
    button_3 = types.InlineKeyboardButton('Удалить отправленное сообщение', callback_data='delete')
    button_4 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(button_3, button_4)

    bot.send_message(message.chat.id, 'Menu', reply_markup=markup)


# ----- Callback декоратор который оборабатывает команду callback_data -----
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1) # Прошлый элемент
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id) # Текущий элемент




# ----- Открытие веб сайта -----
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com')



# ----- Сообщения со слешем '/' -----
@bot.message_handler(commands=['my_first_name'])
def main(message):
    bot.send_message(message.chat.id, f'Your first name: {message.from_user.first_name}')

@bot.message_handler(commands=['my_last_name'])
def main(message):
    bot.send_message(message.chat.id, f'Your last name: {message.from_user.last_name}')

@bot.message_handler(commands=['my_username'])
def main(message):
    bot.send_message(message.chat.id, f'Your username: {message.from_user.username}')

@bot.message_handler(commands=['message'])
def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<em><b>Help information</b></em>', parse_mode='html') # Можно передаьб и третий параметр который будет отвечать за стиль, parse_mode



# ----- Сообщения без слеша '/' -----
# ----- Стоит писать под вышеуказанными программами либо с использованием коман elif, else -----
@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.username}')

    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


# ----- Ответ на присылаемое фото -----
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Какое красивое фото')


bot.polling(none_stop=True) # Либо же можно написать аналогичную команду bot.infinity_polling()
