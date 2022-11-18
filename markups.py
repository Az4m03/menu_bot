from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton('⬅️ Главное меню')

# --- Main Menu ---
btnRandom = KeyboardButton('🔘 Рандомное число')
btnOther = KeyboardButton('➡️ Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnOther)


# --- Other Menu ---
btnInfo = KeyboardButton('📚 Информация')
btnMoney = KeyboardButton('📈 Курсы валют')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)
