import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import select_purchase_type, opt, retail

logging.basicConfig(level=logging.INFO)


# Запуск бота
async def main():
    bot = Bot(token="6875914308:AAFu8F9-HIB49cWB1sBQ1d-SR9sFLmYh6Mg")
    dp = Dispatcher()

    dp.include_routers(select_purchase_type.router, opt.router, retail.router)

    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
