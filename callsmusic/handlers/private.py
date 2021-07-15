from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'<b> - مرحبا بك عزيزي 👋🏻 : {message.from_user.mention()}!</b>\n\n'
        
'- /play : قم بالرد على ملف صوتي او رابط اغنيه في اليوتيوب بهذا الامر لتشغيل الاغنيه في المكالمة\n'
'- /pause : ايقاف مؤقت للاغنيه\n'
'- /resume : استئناف الاغنيه\n'
'- /skip : تخطي الاغنيه التي يتم تشغيلها حالياً\n'
'- /unmute : كتم الاغنية في البوت\n'
'- /stop : ايقاف تشغيل جميع الاغاني\n'
'⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '- قناة البوت ⏺️', url='https://t.me/F0FFE',
                    ),
                    InlineKeyboardButton(
                        '- اضغط لاضافتي 💬', url='ttps://t.me/Music7iBot?startgroup=new',
                    ),
                ],
            ],
        ),
    )

