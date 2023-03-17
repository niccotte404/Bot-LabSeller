from vars import dp, bot
from aiogram.utils import executor
from handlers import admin, user, other
from database import db

async def on_startup(_):
    print("bot started ok")
    await db.connection()
    
admin.reg_handlers(dp)
user.reg_handlers(dp)
other.reg_handlers(dp)
    
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)