# -*- coding: utf-8 -*-

import telebot


class Main:
    ADMINS = [] # your id

    VERSION = "0.2"

    START_TIME = ""

    TOKEN = "2090356465:AAF7J9Rr7jJLKpp81MIwa2Y7bIR-gadfLYM" # bot token

    BOT = telebot.TeleBot(TOKEN)

    BAN_LIST = []
    USER_LIST = {}

    NEWS =  "за 17.12.2020", \
            "\nДобавлено больше теорем."