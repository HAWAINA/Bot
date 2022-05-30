import asyncio
import random
import aioschedule
from aiogram import types, Dispatcher

from bot_instance import bot


async def ban(message: types.Message):
    ban_words = ["сука", "bitch", "кот", "сука", "нахуй", "java"]
    global chat_id
    chat_id = message.chat.id
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Без мата")
    if message.text.lower() == "game":
        games = random.choice(["🎲", "⚽", "🏀", "🎯", "🎳", "🎰"])
        await bot.send_dice(message.chat.id, emoji=games, reply_to_message_id=games)
    elif message.text.lower() == "напомни":
        await message.reply("OK")
    elif message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)


async def work():
    await bot.send_message(chat_id=chat_id, text="пора бухать!")


async def scheduler():
    aioschedule.every().monday.at("03:12").do(work)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(ban)
    dp.register_message_handler(work)
