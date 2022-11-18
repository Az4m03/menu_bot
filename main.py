import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

import random

import settings


bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    if message.text == '🔘 Рандомное число':
        await bot.send_message(message.from_user.id, 'Ваше Число:' + str(random.randint(1000, 9999)))
    elif message.text == '⬅️ Главное меню':
        await bot.send_message(message.from_user.id, '⬅️ Главное меню', reply_markup=nav.mainMenu)
    elif message.text == '➡️ Другое':
        await bot.send_message(message.from_user.id, '➡️ Другое', reply_markup=nav.otherMenu)
    elif message.text == '📚 Информация':
        await bot.send_message(message.from_user.id, 'Какая-то информация')
    elif message.text == '📈 Курсы валют':
        await bot.send_message(message.from_user.id, 'Курс валют')
    else:
        await message.reply('Неивестная команда')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
