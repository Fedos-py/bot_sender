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
def run():
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
                                o = open('status.txt', 'w')
                                o.write('False')
                                o.close()
                                write_msg(event.object.peer_id, 'Вы выключили автобота')
                            elif arg == '1':
                                o = open('status.txt', 'w')
                                o.write('True')
                                o.close()
                                write_msg(event.object.peer_id, 'Вы включили автобота')
                            else:
                                write_msg(event.object.peer_id, 'invalid argument (укажите цифру 0 или 1)')
                        else:
                            write_msg(event.object.peer_id, 'invalid argument (укажите аргумент)')
                    if event.object.text.split(' ')[0] == '/tt':
                        o = open('timetable.txt')
                        timetable = o.read().split('\n')
                        o.close()
                        write_msg(event.object.peer_id, f'Расписание: {timetable}')
                    if event.object.text.split(' ')[0] == '/gs':
                        o = open('status.txt')
                        status = o.read()
                        o.close()
                        write_msg(event.object.peer_id, f'Статус: {status}')
                    else:
                        write_msg(event.object.peer_id, random.choice(phrases).format(event.object.text))
        except Exception as e:
            print(e)

run()