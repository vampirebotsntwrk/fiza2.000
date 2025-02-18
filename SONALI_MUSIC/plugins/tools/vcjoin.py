import asyncio
from SONALI_MUSIC import app
from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges

@app.on_chat_member_updated()
async def video_chat_event(client, update):
    if update.new_chat_member and update.new_chat_member.privileges:
        if update.new_chat_member.privileges.can_manage_video_chats:
            user = update.new_chat_member.user
            chat_id = update.chat.id
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            username = f"@{user.username}" if user.username else "ηᴏ ᴜsєʀηᴧϻє ☹️"
            user_id = user.id

            message = f"**⚘ ᴊσɪηєᴅ ᴠɪᴅєᴏ ᴄʜᴧᴛ**\n\n**:⧽ ηᴧϻє :** {mention}\n**:⧽ ᴜsєʀ ɪᴅ :** `{user_id}`\n**:⧽ ᴜsєʀηᴧϻє :** {username}"
            
            msg = await client.send_message(chat_id, message)  # मैसेज भेजें
            await asyncio.sleep(60)  # 60 सेकंड (1 मिनट) तक वेट करें
            await client.delete_messages(chat_id, msg.message_id)  # मैसेज डिलीट करें
