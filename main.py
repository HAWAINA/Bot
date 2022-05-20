from aiogram import executor
from bot_instance import dp
from handers import client, callback, extra, notification, inlain
from database import db_user
from handers import fsm_admin_hw
import asyncio

from handers.notification import scheduler


async def on_startup(_):
    db_user.sgl_create()
    asyncio.create_task(scheduler())
    print("bot is online")


client.register_handlers_client(dp)

fsm_admin_hw.register_handler_fsm_admin_user(dp)
fsm_admin_hw.register_handler_fsm_admin_user(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
notification.register_handler_notification(dp)
extra.register_handlers_extra(dp)
extra.register_handlers_extra(dp)
inlain.register_handlers_inline(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
