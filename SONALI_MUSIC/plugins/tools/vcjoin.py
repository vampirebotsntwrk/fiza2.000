from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges
from SONALI_MUSIC import app


import asyncio


@app.on_chat_member_updated()
async def video_chat_event(client, update):
    if update.new_chat_member:
        user = update.new_chat_member.user
        chat_id = update.chat.id
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        username = f"@{user.username}" if user.username else "No Username"
        user_id = user.id

        message = f"**⚘ ᴊσɪηєᴅ ᴠɪᴅєᴏ ᴄʜᴧᴛ**\n\n**:⧽ ηᴧϻє :** {mention}\n**:⧽ ᴜsєʀ ɪᴅ :** `{user_id}`\n**:⧽ ᴜsєʀηᴧϻє :** {username}"
        
        msg = await client.send_message(chat_id, message)  # मैसेज भेजें
        await asyncio.sleep(60)  # 1 मिनट बाद मैसेज डिलीट करें
        await client.delete_messages(chat_id, msg.message_id)  # मैसेज डिलीट करें

app.run()
