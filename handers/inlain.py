# import hashlib
# from aiogram import types, Dispatcher
#
#
#
# async def inline_google(query: types.InlineQuery):
#     text = query.query or "echo"
#     links = "https://www.google.com/search?q=" + text
#     result_id: str = hashlib.md5(text.encode()).hexdigest()
#     articles = [
#         types.InlineQueryResultArticle(
#             id=result_id,
#             title="google:",
#             url=links,
#             input_message_content=types.InputTextMessageContent(
#                 message_text=links
#
#             )
#         )
#     ]
#     await query.answer(articles, cache_time=2, is_personal=True)
#
# def register_handlers_inline(dp: Dispatcher):
#     dp.register_inline_handler(inline_google)
import hashlib
from aiogram import types, Dispatcher
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle


async def inline_wiki(query: types.InlineQuery):
    text = query.query or "echo"
    links = "https://www.google.com/search?q=" + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title="google:",
            url=links,
            input_message_content=types.InputTextMessageContent(message_text=links),
        )
    ]
    await query.answer(articles, cache_time=2, is_personal=True)


def register_handlers_inline(dp: Dispatcher):

    dp.register_inline_handler(inline_wiki)
