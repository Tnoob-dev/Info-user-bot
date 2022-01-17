from pyrogram import Client as Cli, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from creds import Creds


ID_bot = Cli(
    "ID_Bot",
    api_hash=Creds.api_hash, # API_HASH FROM my.telegram.org
    api_id=Creds.api_id, # API_ID FROM my.telegram.org,
    bot_token=Creds.bot_token, # TOKEN FROM @Botfather
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
    ],[
        InlineKeyboardButton("🆘Ver Ayuda🆘", callback_data='help')
    ]]
   
    ))




#########################################################################
###################### Watch ur INFO ####################################
#########################################################################


@ID_bot.on_message(filters.command("info") & ~filters.edited)
async def data_user(client, message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_frst_name = message.from_user.first_name
    user_lst_name = message.from_user.last_name
    
    await message.reply_text(f"__Datos de usuario:__❤️\n**Nombre:** ```{user_frst_name}```\n**Apellido:** ```{user_lst_name}```\n**ID:** ```{user_id}```\n**Username:** ```@{username}```")


############################################################################
###################### Watch group INFO ####################################
############################################################################


@ID_bot.on_message(filters.command("group") & filters.group)
async def get_group(client, message: Message):
    group_id = message.chat.id
    group_name = message.chat.title
    group_link = message.chat.invite_link
    group_username = message.chat.username

    await message.reply_text(f"__Datos del grupo:__❤️\n**Nombre:** ```{group_name}```\n**Link:** ```{group_link}```\n**ID:** ```{group_id}```\n**Username:** ```@{group_username}```")

##############################################################################
###################### Watch channel INFO ####################################
##############################################################################


@ID_bot.on_message(filters.command("channel_info") & filters.channel)
async def channel_id(client, message: Message):
    channel_name = message.chat.title
    channel_id = message.chat.id
    channel_username = message.chat.username
    channel_link = message.chat.invite_link
    
    await message.reply_text(f"__Datos del Canal:__❤️\n**Nombre:** ```{channel_name}```\n**Link:** ```{channel_link}```\n**ID:** ```{channel_id}```\n**Username:** ```@{channel_username}```")


#########################################################################################
###################### Watch user-msg-forwarded INFO ####################################
#########################################################################################


@ID_bot.on_message(filters.private & filters.forwarded)
async def data_other_users(client, message: Message):
    frwrd = message.forward_from

    an_user_id = frwrd.id
    an_user_username = frwrd.username
    an_user_frst_name = frwrd.first_name
    an_user_lst_name = frwrd.last_name

    await message.reply_text(f"__Datos de usuario:__❤️\n**Nombre:** ```{an_user_frst_name}```\n**Apellido:** ```{an_user_lst_name}```\n**ID:** ```{an_user_id}```\n**Username:** ```@{an_user_username}```")


####################################################################################
###################### Watch user in group INFO ####################################
####################################################################################



@ID_bot.on_message(filters.command("get_info") & filters.group)
async def get_info_in_group(client, message: Message):
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    user_lstname = message.reply_to_message.from_user.last_name
    user_username = message.reply_to_message.from_user.username
    group_name = message.reply_to_message.chat.title

    await message.reply_text(f"__Datos de usuario en el grupo {group_name}:__❤️\n**Nombre:** ```{user_name}```\n**Apellido:** ```{user_lstname}```\n**ID:** ```{user_id}```\n**Username:** ```@{user_username}```")



@ID_bot.on_callback_query(filters.regex('help'))
async def help(client, callbackquery: Message):
    await callbackquery.answer("Por favor espere")
    await callbackquery.message.edit_text("Simple Bot para obtener información de **Grupos/Canales/usuarios:**\n\nPara obtener sus propios datos puede usar /info\n\nPara obtener la informacion de otro usuario, puede reenviar un mensaje de ese usuario a aqui al bot\n\nSi desea obtener la informacion de un usuario dentro de un grupo, primero añada al bot a ese grupo, y luego responda a un mensaje de ese usuario con /get_info\n\nSi desea ver la informacion de un grupo, añada al bot a un grupo, y luego utilice el comando /group y vera la información del grupo\n\nSi desea ver la informacion de un canal, añada al bot al canal y utilice /channel_info en el canal\n\n\nEsperamos que @ID_Simple-bot sea de su agrado😊", 
    
    reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("🔙Volver Atras🔙", callback_data='back')]]))

@ID_bot.on_callback_query(filters.regex('back'))
async def back(client, callbackquery):

    await callbackquery.answer("Regresando")
    await callbackquery.message.edit_text(f"😌Hola Usuario, soy un sencillo bot, el cual si le pones /get_data_user obtendras tus datos📝, y si reenvias un mensaje de cualquier usuario, te dire sus datos tambien📝",
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("❤️Canal Interesante💙", url="https://t.me/s3softwareyprogramacion"),
        InlineKeyboardButton("🤍Grupo del canal🤍", url="https://t.me/S3SPGrupo")
    ],[
        InlineKeyboardButton("💜Github💜", url="https://github.com/Tnoob-dev"),
        InlineKeyboardButton("💛Repo💛", url="https://github.com/Tnoob-dev/Info-user-bot")
    ],[
        InlineKeyboardButton("🖤GigaChad-Bot🖤", url="https://t.me/Uploader_Tbot")
    ],[
        InlineKeyboardButton("Ver Ayuda", callback_data='help')
    ]]
    
    ))


print("Started")
ID_bot.run()
