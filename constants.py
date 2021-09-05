import random
import vk_api

TOKEN = '73cd5dd02980307652c4ed536ec0934ed9df5e121c1337dc54ebd2072046fea617f32197f60ccd8c39316'
LOGIN = '+79679757380'
PASSWORD = ''
vk = vk_api.VkApi(token=TOKEN)
bot_api = vk.get_api()

def write_msg(peer_id, message, attachment=''):
    random_id = vk_api.utils.get_random_id()
    print(peer_id, message, random_id)
    vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random_id, 'attachment': attachment})