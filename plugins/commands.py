


import os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from sample_config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database.add import add_user_to_database


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)

    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )

@Client.on_message(filters.private & filters.command("settings"))
async def settings_handler(bot: Client, event: Message):
    if not event.from_user:
        return await event.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, event)
    editable = await event.reply_text(
        text="**👀 Processing...**"
    )
    await OpenSettings(editable, user_id=event.from_user.id)
