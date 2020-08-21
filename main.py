import random

import config
import telebot

import avatar

with open("token.txt", "r") as file:
    token = file.read()
with open("proxy.txt", "r") as file:
    telebot.apihelper.proxy = file.read()
bot = telebot.TeleBot(token=token)
lyrics = ["Выгляди эффективным."]


def random_text(lyrics):
    return random.randint(0, len(lyrics) - 1)


@bot.message_handler(commands=["avatar"])
def handle_start_help(message):
    user = message.chat.id
    avatar.main()
    bot.send_photo(user, open("avatar.png", "rb"))


@bot.message_handler(content_types=["text"])
def echo(message):
    text = message.text
    user = message.chat.id
    text = lyrics[random_text(lyrics)]
    bot.send_message(user, text)


bot.polling(none_stop=True)
