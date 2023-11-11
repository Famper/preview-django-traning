#!venv/bin/python
import os
import logging
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token=os.environ.get("API_KEY"))
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /ping
@dp.message_handler(commands="ping")
async def cmd_test1(message: types.Message):
    await message.reply("pong")


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
