from constants import *
from time_sender import *
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

phrases = ['Правда {}?', 'Точно {}?', 'Ты сказал {}?', 'Вы сказали {}?', 'Вы уверены, что {}?', 'Ты уверен, что {}?']
status = True


# Авторизуемся как сообщество


# Функция посылающая сообщение
def write_msg(peer_id, message, attachment=''):
    random_id = vk_api.utils.get_random_id()
    print(peer_id, message, random_id)
    vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random_id, 'attachment': attachment})

# Основной цикл
def run():
    if status:
        run_sender()
    while True:
        longpoll = VkBotLongPoll(vk, 206863393)
        try:
            for event in longpoll.listen():
                # print(event)
                if event.object.text != '':
                    print(event.object.text.split(' '))
                    if event.object.text.split(' ')[0] == '/ss':
                        if len(event.object.text.split(' ')) == 2:
                            arg = event.object.text.split(' ')[1]
                            if arg == '0':
                                status = False
                                print(status)
                                # set_status_off()
                                write_msg(event.object.peer_id, 'Вы выключили автобота')
                            elif arg == '1':
                                status = True
                                print(status)
                                # set_status_on()
                                write_msg(event.object.peer_id, 'Вы включили автобота')
                            else:
                                write_msg(event.object.peer_id, 'invalid argument (укажите цифру 0 или 1)')
                        else:
                            write_msg(event.object.peer_id, 'invalid argument (укажите аргумент)')
                    else:
                        write_msg(event.object.peer_id, random.choice(phrases).format(event.object.text))
        except Exception as e:
            print(e)