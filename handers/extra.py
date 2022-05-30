from aiogram import types, Dispatcher
from bot_instance import bot


async def secret_word(message: types.Message):
    await message.reply("yes my master")


async def ban(message: types.Message):
    ban_words = ["java", "пошел нахуй", "шлюха", "python is bad", "нахуй"]
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Bot-Admin deleted bad words")
    if message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: "dorei" in word.text)
    dp.register_message_handler(ban, content_types=["text"])
