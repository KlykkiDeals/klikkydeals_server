import os
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from handlers import start, lang, menu, aviatickets
from config import BOT_TOKEN

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = os.getenv("WEBHOOK_URL") + WEBHOOK_PATH

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Подключение роутеров
dp.include_router(start.router)
dp.include_router(lang.router)
dp.include_router(menu.router)
dp.include_router(aviatickets.router)

# Установка Webhook
async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    print("✅ Webhook установлен:", WEBHOOK_URL)

# Создание aiohttp-приложения
app = web.Application()
app.on_startup.append(on_startup)

SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
setup_application(app, dp)

if __name__ == "__main__":
    web.run_app(app, port=8000)