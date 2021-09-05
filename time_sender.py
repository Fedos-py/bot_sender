from constants import *
from vk_functions import *
import time
# import sched
import schedule
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
peer_id = 235573478



def printer():
    o = open('status.txt')
    status = o.read()
    o.close()
    print(status)
    if status == 'True':
        try:
            print('Что-то написал')
            data = get_suggestionslist()
            i = 0
            for elem in data['items']:
                vk_session = vk_api.VkApi(LOGIN, PASSWORD)
                vk_session.auth()
                vk_u = vk_session.get_api()
                colvo = len(vk_u.friends.getMutual(target_uid=elem['id']))
                if colvo >= 100:
                    vk_u.friends.add(user_id=elem['id'])
                    i += 1
            write_msg(peer_id, f'Выполнили функцию по рассписанию. Из {len(data["items"])} возможных друзей отправили {i} заявок.')
        except Exception as e:
            write_msg(peer_id, f'Ошибка: {e}')



def run_sender():
    o = open('timetable.txt')
    timetable = o.read().split('\n')
    o.close()
    print(timetable)
    for line in timetable:
        schedule.every().day.at(line).do(printer)
    # schedule.every(10).seconds.do(printer)
    while 1:
        schedule.run_pending()

run_sender()