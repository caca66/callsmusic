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
        '\n\n- اوامر البوت ↙️ :\n\n'
        'تشغيل الاغاني في المحادثة الصوتية - /play\n'
        'ايقاف الاغنية مؤقت - /pause\n'
        'استئناف الاغنية في البوت - /resume\n'
        'تخطي الاغنية او ايقافها  - /skip\n'
        'كتم الاغنية في المكالمة - /mute\n'
        'الغاء كتم الاغنية - /unmute\n'
        'ايقاف تشغيل جميع الاغاني  - /stop',
        
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '- مـطور البوت .', url='https://t.me/F0FFE',
                    ),
                    InlineKeyboardButton(
                        '- اضغط هنا الاضافتي .', url='https://t.me/{BOT_USERNAME}?startgroup=new',
                    ),
                ],
            ],
        ),
    )

