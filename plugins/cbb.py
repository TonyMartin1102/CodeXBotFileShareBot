#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : <a href='tg://user?id={OWNER_ID}'>𝐀𝐧𝐨𝐧𝐲𝐦𝐨𝐮𝐬 ☠️</a> \n \n○ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : <code>Python3</code>\n \n○ 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n \n○ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 : <a href='https://t.me/AnonymousOwner'>Buy Now</a>\n \n○ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @StreamTVIndex\n \n○ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : https://t.me/+kz0Al5B07X41ZmU1</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
