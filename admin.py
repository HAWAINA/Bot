from aiogram.utils import executor
from bot_instance import dp
from handers import client, extra, fsm_admin_hw

fsm_admin_hw.register_handler_fsm_admin_user(dp)
client.register_handlers_client(dp)

extra.register_handlers_extra(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
