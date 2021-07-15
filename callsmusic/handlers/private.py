from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'<b> - مرحبا بك عزيزي : {message.from_user.mention()}! 👋🏻</b>\n'     
        '\n- بوت تشغيل الاغاني الصوتية داخل المجموعات :\n\n'
        '\n- عليك اضافه حساب المساعد مع البوت معرف الحساب : @DarkeMusic .\n\n'
        '\n<b> - اوامر البوت ↙️ : </b>\n\n'
        'تشغيل الاغاني في المحادثة الصوتية - /play\n'
        'ايقاف الاغنية مؤقت - /pause\n'
        'استئناف الاغنية في البوت - /resume\n'
        'تخطي الاغنية او ايقافها  - /skip\n'
        'كتم الاغنية في المكالمة - /mute\n'
        'الغاء كتم الاغنية - /unmute\n'
        'ايقاف تشغيل جميع الاغاني  - /stop\n'
        '⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯\n'
        '<b> - DEV USER : @VLVLVI .</b>',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '- مـطور البوت .', url='https://t.me/F0FFE',
                    ),
                    InlineKeyboardButton(
                        '- آضغط لاضافتـي .', url='https://t.me/Music7iBot?startgroup=new',
                    ),
                ],
            ],
        ),
    )

