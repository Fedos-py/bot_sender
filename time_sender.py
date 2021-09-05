from constants import *
import time
# import sched
import schedule
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
peer_id = 235573478



# s = sched.scheduler(time.time, time.sleep)
def printer():
    print('Что-то написал')
    write_msg(peer_id, '@fedya_nelubin(Босс), тестируем автоотправлялку уже {i} раз')


def set_status_on():
    status = True


def set_status_off():
    status = False


def get_status():
    return status


def run_sender():
    schedule.every(10).seconds.do(printer)
    while 1:
        schedule.run_pending()