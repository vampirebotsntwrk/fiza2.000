from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ ᴡєʟᴄσϻє ᴛᴏ ᴛєᴧϻ ᴠᴀᴍᴘɪʀᴇ ʀєᴘσs ❃</u>
 
✼ ʀєᴘᴏ ᴛᴏ ηʜɪ ϻɪʟєɢᴧ ʏʜᴧ
 
❉ ᴘᴧʜʟє ᴠᴀᴍᴘɪʀᴇ ᴋᴏ ᴘᴧᴘᴧ ʙσʟ 

✼ || [ᴠᴀᴍᴘɪʀᴇ-ᴋɪɴɢ](https://t.me/lllVAMPIRE_UPDATElll) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜєʟᴘ •", url="https://t.me/lllVAMPIRE_UPDATElll"),
          InlineKeyboardButton("• 𝛅ᴜᴘᴘσʀᴛ •", url="https://t.me/lllVAMPIRE_UPDATElll"),
          ],
[
InlineKeyboardButton("• ϻᴧɪη ʙσᴛ •", url=f"https://t.me/lllVAMPIRE_UPDATElll"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/kbi6t5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
