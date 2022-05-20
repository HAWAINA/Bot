from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot_instance import bot
from database import db_user
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from keybords import database_kb


class User_status(StatesGroup):
    id = State()
    username = State()
    firstname = State()
    lastname = State()


async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(
        message.from_user.id,
        "I can add to data some information just give me a command as /status",
        reply_markup=database_kb.button_admin,
    )


async def cancel_hundler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    await state.finish()
    await message.reply("Canceled normally")


async def fsm_start(message: types.Message):
    await User_status.id.set()
    await message.reply("enter start")


async def load_id(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data["id"] = message.from_user.id
    await User_status.next()
    await message.reply("Send me a id")


async def load_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["username"] = message.from_user.username
    await User_status.next()
    await message.reply("Admin, send me username, please")


async def load_firstname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["fisrtname"] = message.from_user.first_name
    await User_status.next()
    await message.reply("Admin, send me firstname, please")


async def load_lastname(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data["lastname"] = message.from_user.last_name

    await db_user.sql_command_insert(state)
    await state.finish()


async def complate_delete(call: types.CallbackQuery):
    await db_user.sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(
        text=f"{call.data.replace('delete ', '')} deleted", show_alert=True
    )


async def delete_data(message: types.Message):
    if message.forward_from_message_id == ADMIN_ID:
        inserting = await db_user.sql_command_select(message)
        for result in inserting:
            await bot.send_message(
                message.forward_from_message_id,
                result[0],
                caption=f"ID: {result[0]}\n"
                f"username: {result[1]}\n"
                f"firstname: {result[2]}\n"
                f"lastname: {result[3]}\n",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(
                        f"delete: {result[0]}", callback_data=f"delete {result[0]}"
                    )
                ),
            )


def register_handler_fsm_admin_user(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=["status"], state=None)
    dp.register_message_handler(cancel_hundler, state="*", commands="cancel")
    dp.register_message_handler(
        cancel_hundler, Text(equals="cancel", ignore_case=True), state="*"
    )
    dp.register_message_handler(load_id, state=User_status.id)
    dp.register_message_handler(load_username, state=User_status.username)
    dp.register_message_handler(load_firstname, state=User_status.firstname)
    dp.register_message_handler(load_lastname, state=User_status.lastname)
    dp.register_message_handler(
        is_admin_func, commands=["user_register"], is_chat_admin=True
    )
    dp.register_callback_query_handler(
        complate_delete, lambda call: call.data and call.data("delete ")
    )
    dp.register_message_handler(delete_data, commands=["delete"])
