from constants import *
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

phrases = ['Правда {}?', 'Точно {}?', 'Ты сказал {}?', 'Вы сказали {}?', 'Вы уверены, что {}?', 'Ты уверен, что {}?']


# Авторизуемся как сообщество


# Функция посылающая сообщение
def write_msg(peer_id, message, attachment=''):
    random_id = vk_api.utils.get_random_id()
    print(peer_id, message, random_id)
    vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random_id, 'attachment': attachment})

# Основной цикл
while True:
    longpoll = VkBotLongPoll(vk, 206863393)
    try:
        for event in longpoll.listen():
            # print(event)
            if event.object.text != '':
                print(event.object.peer_id)
                write_msg(event.object.peer_id, random.choice(phrases).format(event.object.text))
    except Exception as e:
        print(e)