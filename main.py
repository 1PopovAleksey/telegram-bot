import telebot
from telebot import types

bot = telebot.TeleBot('5455650810:AAEjF19EDC0tZy6Sukp4fIw6gnuIupATqjY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}, are u like pets?)</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    video_cat = types.KeyboardButton('/video_cat')
    video_dog = types.KeyboardButton('/video_dog')
    video_pets = types.KeyboardButton('/video_pets')
    keyboard.add(start, video_cat, video_dog, video_pets)
    bot.send_message(message.chat.id, 'What u need?', reply_markup=keyboard, parse_mode='html')


@bot.message_handler(commands=['video_cat'])
def video(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Check this video!',
                                            url='https://www.youtube.com/watch?v=3-G-VCaoSaE&ab_channel=Meowthemall'))
    bot.send_message(message.chat.id, 'Best video about cats)', reply_markup=keyboard, parse_mode='html')


@bot.message_handler(commands=['video_dog'])
def video(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Check this video!', url='https://www.youtube.com/watch?v=wbbwnqWeZZw'))
    bot.send_message(message.chat.id, 'Best video about dogs)', reply_markup=keyboard, parse_mode='html')


@bot.message_handler(commands=['video_pets'])
def video(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Check this video!', url='https://www.youtube.com/watch?v=O-qqRaHVHiE'))
    bot.send_message(message.chat.id, 'Best video about pets)', reply_markup=keyboard, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "Hello! Nice to meet you)", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('img/funny_pets.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == "video":
#         bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=TOVjKDgNtO0&ab_channel=PetsTown",
#                          parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, "I don't know this command, sorry(", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Oh, cool photo!')


bot.polling(none_stop=True)
