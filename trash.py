import telebot
from telebot import types

bot = telebot.TeleBot("7462162109:AAE0AtfFPhMsjKqb9bphHcKU69EttEd4BU4")

# Словарь тестов
tests = {
    "Математика": ["2 + 2 = ?", ["4", "5", "6", "7"], 0],
    "История": ["Кто был первым президентом США?", ["Джордж Вашингтон", "Томас Джефферсон", "Джон Адамс", "Абраам Линкольн"], 1],
    "Природа": ["Сколько океанов на Земле?", ["3", "4", "5", "6"], 2],
    "Технологии": ["Кто является основателем компании Apple?", ["Стив Джобс", "Билл Гейтс", "Марк Цукерберг", "Элон Маск"], 3]
}

# Словарь для хранения баллов пользователей
user_scores = {}

@bot.message_handler(commands=['start', 'restart'])
def send_welcome(message):
    user_id = message.from_user.id
    user_scores[user_id] = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = tests.keys()
    for button in buttons:
        markup.add(button)
    bot.send_message(message.chat.id, "Выберите категорию теста:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in tests.keys())
def send_question(message):
    user_id = message.from_user.id
    category = message.text
    question, options, correct_index = tests[category]
    
    # Создание клавиатуры с вариантами ответов
    reply_markup = types.InlineKeyboardMarkup()
    for option in options:
        reply_markup.add(types.InlineKeyboardButton(text=option, callback_data=f"{category}_{option}"))
    
    bot.send_message(message.chat.id, question, reply_markup=reply_markup)

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] in tests.keys())
def process_answer(call):
    user_id = call.from_user.id
    category, answer = call.data.split('_')
    correct_answer = tests[category][1][tests[category][2]]
    
    if answer == correct_answer:
        user_scores[user_id] += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Правильно! Ваши баллы: {user_scores[user_id]}")
    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Неправильно. Правильный ответ: {correct_answer}")
    
    bot.send_message(call.message.chat.id, "Выберите категорию теста или введите /restart для сброса баллов.")

bot.polling()