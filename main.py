import telebot
from dialog import Dialog

token = '723314573:AAH5-onyzwyA1fMDnk73GLBQ7sE2a2j_qD4'

bot = telebot.TeleBot(token=token)

print(f'Your token is: {token}')
print('Start pooling...')

dialog = Dialog(bot, {
    'voc': 'voc.yaml',
})

dialog.start()
