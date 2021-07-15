from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'<b> - مرحبا بك عزيزي 👋🏻 : {message.from_user.mention()}!</b>\n\n'
        
'I am Calls Music bot, '
        'I let you play music in group calls.'
        '\n\nThe commands I currently support are:\n\n'
        '/play - play the replied audio file or YouTube video\n'
        '/pause - pause the audio stream\n'
        '/resume - resume the audio stream\n'
        '/skip - skip the current audio stream\n'
        '/mute - mute the userbot\n'
        '/unmute - unmute the userbot\n'
        '/stop - clear the queue and remove the userbot from the call',
        
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '- قناة البوت ⏺️', url='https://t.me/F0FFE',
                    ),
                    InlineKeyboardButton(
                        '- اضغط لاضافتي 💬', url='https://t.me/Music7iBot?startgroup=new',
                    ),
                ],
            ],
        ),
    )

