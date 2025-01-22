from pyrogram import Client, filters
from gtts import gTTS
from SONALI_MUSIC import app


@app.on_message(filters.command('tts'))
def text_to_speech(client, message):
    try:
        # Ensure the message contains text for TTS
        if len(message.text.split()) < 2:
            message.reply_text("Please provide text for TTS. Usage: `/tts <text>`")
            return

        # Extract text after the command
        text = message.text.split(' ', 1)[1]
        
        # Generate TTS audio
        tts = gTTS(text=text, lang='hi')
        file_name = 'speech.mp3'
        tts.save(file_name)
        
        # Send the generated audio file
        app.send_audio(message.chat.id, file_name)

    except Exception as e:
        # Handle errors gracefully
        message.reply_text(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ : {str(e)}")
