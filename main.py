import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from handlers.start import start_command, show_main_menu, ENTER_ADDRESS, ENTER_PHONE
from handlers.tariffs import show_tariffs_categories, show_internet_tariffs, show_tv_tariffs
from handlers.application import start_application, enter_address, enter_phone, cancel_application

# Загружаем переменные из .env файла
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    # Получаем токен из переменных окружения
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    if not BOT_TOKEN:
        print("❌ Ошибка: BOT_TOKEN не найден в переменных окружения")
        print("💡 Создайте файл .env с содержимым: BOT_TOKEN=ваш_токен_бота")
        return
    
    # Остальной код без изменений...
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Остальной код без изменений...
    application_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('^✅ Оставить заявку$'), start_application)],
        states={
            ENTER_ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_address)],
            ENTER_PHONE: [
                MessageHandler(filters.CONTACT, enter_phone),
                MessageHandler(filters.TEXT & ~filters.COMMAND, enter_phone)
            ],
        },
        fallbacks=[
            MessageHandler(filters.Regex('^❌ Отменить заявку$'), cancel_application),
            CommandHandler('cancel', cancel_application)
        ]
    )
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(application_handler)
    application.add_handler(MessageHandler(filters.Regex('^📊 Посмотреть тарифы$'), show_tariffs_categories))
    application.add_handler(MessageHandler(filters.Regex('^🌐 Интернет$'), show_internet_tariffs))
    application.add_handler(MessageHandler(filters.Regex('^📺 Телевидение$'), show_tv_tariffs))
    application.add_handler(MessageHandler(filters.Regex('^🔙 Назад$'), show_main_menu))
    application.add_handler(MessageHandler(filters.Regex('^📱 Главное меню$'), show_main_menu))
    application.add_handler(MessageHandler(filters.Regex('^🛟 Поддержка$'), show_main_menu))
    
    # Запускаем бота
    print("🤖 Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()