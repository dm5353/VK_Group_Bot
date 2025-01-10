import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests

TOKEN = "токен группы"
GROUP_ID = "id группы"
WELCOME_MESSAGE = "Добро пожаловать! Спасибо за подписку!"

session = requests.Session()
session.proxies = { #прокси если нужен
    'http': 'http://95.66.138.21:8880'
}

vk_session = vk_api.VkApi(token=TOKEN, session=session)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, GROUP_ID)

print(f"Бот запущен...")

for event in longpoll.listen():
    if event.type == VkBotEventType.GROUP_JOIN:
        user_id = event.object['user_id']
        try:
            vk.messages.send(
                user_id=user_id,
                message=WELCOME_MESSAGE,
                random_id=0
            )
            print(f"Сообщение отправлено пользователю {user_id}")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
