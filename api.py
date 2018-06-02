# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging
import datetime
import connectrion
# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}
name = ''
groupName = ''
# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.
        res['response']['text'] = 'Добрый день! Как я могу к вам обращаться?'
        return

    if req['session']['message_id'] == 1:
        name = req['request']['original_utterance']
        res['response']['text'] = 'А я расписание МГТУ. Приятно познакомиться, %s! В какой ты группе?' % (name)
        return
    
    num = req['session']['message_id']
    if num == 2:
        groupName = req['request']['original_utterance']
        listing = [user_id,name,groupName]
        connectrion.add(listing)
        temp = connectrion.check()
        res['response']['text'] = '%s. Ты можешь узнать свое расписание на сегодня, завтра и на неделю. %s' % (groupName,temp)
        res['response']['buttons'] = getSuggests(user_id)
        return
    
    res['response']['text'] = 'Спасибо'
    return
    

# Функция возвращает две подсказки для ответа.
def getSuggests(user_id):

    session = {
        'suggests': [
            "Сегодня.",
            "Завтра.",
            "Неделя.",
        ]
    }
    suggests = [
        {'title': suggest, 'hide': False}
        for suggest in session['suggests']
    ]
    return suggests