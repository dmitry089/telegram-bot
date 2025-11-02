from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

# Состояния для ConversationHandler - ОСТАВЬТЕ ТОЛЬКО ЭТУ СТРОКУ
ENTER_ADDRESS, ENTER_TARIFF, ENTER_PHONE, ENTER_COMMENTS = range(4)
# УДАЛИТЕ эти две строки:
# ENTER_ADDRESS = 1
# ENTER_PHONE = 2

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['📊 Посмотреть тарифы', '✅ Оставить заявку'],
        ['📞 Мои заявки', '🛟 Поддержка']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        '👋 Добро пожаловать в сервис подключения интернета и TV!\n\n📱 Главное меню:',
        reply_markup=reply_markup
    )

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['📊 Посмотреть тарифы', '✅ Оставить заявку'],
        ['📞 Мои заявки', '🛟 Поддержка']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('📱 Главное меню:', reply_markup=reply_markup)