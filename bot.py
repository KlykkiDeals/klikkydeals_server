import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from aiogram.client.session.aiohttp import AiohttpSession

# ✅ Подключаем все обработчики
from handlers import start, lang, menu, aviatickets

# 🔄 Сброс webhook при запуске, если бот "молчит"
async def reset_webhook(bot: Bot):
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        print("✅ Webhook удалён (если был)")
    except Exception as e:
        print(f"⚠️ Ошибка при удалении webhook: {e}")

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    # ⛔️ Очищаем старые конфликты Telegram
    await reset_webhook(bot)

    # 📌 Роутеры
    dp.include_router(start.router)
    dp.include_router(lang.router)
    dp.include_router(menu.router)
    dp.include_router(aviatickets.router)

    # 🚀 Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
