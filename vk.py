import vk_api
import requests
apiKey = 'b22cdf53821a1fdc8aaa4b1c122c4fbada187ea27623df0c5c993bed9c001f11f40ff22573552b51c3923'
session = requests.Session()
login, password = '+79220954334', '031219919vk.com'
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
#from vk_api.longpoll import VkLongPoll, VkEventType
#longpoll = VkLongPoll(vk_session)
#vk = vk_session.get_api()

#for event in longpoll.listen():
#    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
#            vk.messages.send(user_id=event.user_id, message=('Зачем ты пишешь - ' + event.text + '?'));
