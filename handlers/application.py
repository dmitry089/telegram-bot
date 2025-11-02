from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes, ConversationHandler
from handlers.start import ENTER_ADDRESS, ENTER_TARIFF, ENTER_PHONE, ENTER_COMMENTS

async def start_application(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('📍 Введите адрес подключения (улица, дом, квартира):')
    return ENTER_ADDRESS

async def enter_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['address'] = update.message.text
    keyboard = [['❌ Отменить заявку']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    # Простая версия - сразу запрашиваем телефон
    contact_keyboard = [[KeyboardButton("📞 Отправить телефон", request_contact=True)]]
    phone_markup = ReplyKeyboardMarkup(contact_keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        f"✅ Адрес сохранен: {update.message.text}\n\nТеперь поделитесь номером телефона:",
        reply_markup=phone_markup
    )
    return ENTER_PHONE

async def enter_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.contact:
        phone = update.message.contact.phone_number
    else:
        phone = update.message.text
    
    context.user_data['phone'] = phone
    
    # Создаем "заявку"
    application_id = 12345  # Временный номер
    
    await update.message.reply_text(
        f"✅ Заявка #{application_id} принята!\n\n"
        f"Адрес: {context.user_data['address']}\n"
        f"Телефон: {phone}\n\n"
        "Менеджер свяжется с вами в ближайшее время!",
        parse_mode='Markdown',
        reply_markup=ReplyKeyboardMarkup([['📱 Главное меню']], resize_keyboard=True)
    )
    
    # Очищаем временные данные
    context.user_data.clear()
    return ConversationHandler.END

async def cancel_application(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    from handlers.start import show_main_menu
    await show_main_menu(update, context)
    return ConversationHandler.END