import asyncio
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
    if message.text.lower() == "dice":
        await bot.send_dice(message.chat.id, emoji="🎲")
    elif message.text == "напомни":
        await message.reply("OK")
    elif message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)


async def work():
    await bot.send_message(chat_id=chat_id, text="пора бухать!")


async def scheduler():
    aioschedule.every().friday.at("21:00").do(work)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(ban)
    dp.register_message_handler(work)
