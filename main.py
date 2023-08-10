import asyncio
import logging
from GPTans import easy_shows_answer
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token='5890317181:AAFnIlVWx9fyBl6LbIvc74-vE1h2X5hmXd4')
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Ну что будем пробывать !")


@dp.message(F.text)
async def cmd_answer(message: types.Message):
    asis = easy_shows_answer(message.text)
    await message.answer(asis)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
