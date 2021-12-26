from pyrogram import Client as Cli, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 


ID_bot = Cli(
    "ID_Bot",
    api_hash=None, # API_HASH FROM my.telegram.org
    api_id=None, # API_ID FROM my.telegram.org,
    bot_token=None, # TOKEN FROM @Botfather
)


@ID_bot.on_message(filters.command("start") & ~filters.edited)
async def start(client, message: Message):
    user_name = message.from_user.first_name
    await message.reply_text(f"😌Hola {user_name}, soy un sencillo bot, el cual si le pones /get_data_user obtendras tus datos📝, y si reenvias un mensaje de cualquier usuario, te dire sus datos tambien📝",
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("❤️Canal Interesante💙", url="https://t.me/s3softwareyprogramacion"),
        InlineKeyboardButton("🤍Grupo del canal🤍", url="https://t.me/S3SPGrupo")
    ],[
        InlineKeyboardButton("💜Github💜", url="https://github.com/Tnoob-dev"),
        InlineKeyboardButton("💛Repo💛", url="https://github.com/Tnoob-dev/Info-user-bot")
    ],[
        InlineKeyboardButton("🖤GigaChad-Bot🖤", url="https://t.me/Uploader_Tbot")
    ]]
    
    ))

@ID_bot.on_message(filters.command("help") & ~filters.edited)
async def help(client, message: Message):
    await message.reply_voice("https://file2directlink.herokuapp.com/304271000715422920370896300/voice_2021-12-26_06-55-25_.oga")

@ID_bot.on_message(filters.command("get_data_user") & ~filters.edited)
async def data_user(client, message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_frst_name = message.from_user.first_name
    user_lst_name = message.from_user.last_name
    await message.reply_text(f"__Datos de usuario:__❤️\n**Nombre:** ```{user_frst_name}```\n**Apellido:** ```{user_lst_name}```\n**ID:** ```{user_id}```\n**Username:** ```@{username}```")


@ID_bot.on_message()
async def data_other_users(client, message: Message):
    an_user_id = message.forward_from.id
    an_user_username = message.forward_from.username
    an_user_frst_name = message.forward_from.first_name
    an_user_lst_name = message.forward_from.last_name
    await message.reply_text(f"__Datos de usuario:__❤️\n**Nombre:** ```{an_user_frst_name}```\n**Apellido:** ```{an_user_lst_name}```\n**ID:** ```{an_user_id}```\n**Username:** ```@{an_user_username}```")
        
    return


print("Started")
ID_bot.run()