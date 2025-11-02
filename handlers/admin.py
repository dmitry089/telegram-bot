from telegram import Update
from telegram.ext import ContextTypes

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    # Проверяем админские права (можно добавить список админов в .env)
    admins = [123456789]  # Ваш ID
    
    if user_id not in admins:
        await update.message.reply_text("⛔ У вас нет доступа к этой команде")
        return
    
    keyboard = [
        ['📊 Статистика', '📋 Все заявки'],
        ['📢 Рассылка', '🔙 Назад']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "👨‍💼 Админ-панель:",
        reply_markup=reply_markup
    )