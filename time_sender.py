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

schedule.every(10).minutes.do(printer)

while 1:
   schedule.run_pending()