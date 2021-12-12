# MIT License

# Copyright (c) 2021 By_Azade

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import os
import sys

from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

USER = Config.USER
OWNER = Config.OWNER
HOME_TEXT = Config.HOME_TEXT
HOME_TEXT_OWNER = Config.HOME_TEXT_OWNER
HELP = Config.HELP


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
	if str(cmd.from_user.id) != OWNER:
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name,
			                 cmd.from_user.id, USER, USER, USER, OWNER),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/By_Azade'),
						InlineKeyboardButton("🤖Other Bots", url="https://t.me/KanalLinkleri")
					],
                    [
                        InlineKeyboardButton(
                            "🔗Source Code", url="https://github.com/Muhammedfurkan/Instagram-Bot"),
						InlineKeyboardButton(
						    "🧩Deploy Own Bot", url="https://heroku.com/deploy?template=https://github.com/muhammedfurkan/Instagram-Bot")
                    ],
                    [
                        InlineKeyboardButton(
                            "👨🏼‍🦯How To Use?", callback_data="help#subin"),
						InlineKeyboardButton("⚙️Update Channel",
						                     url="https://t.me/KanalLinkleri")

                    ]

				]
			)
		)
	else:
		await cmd.reply_text(
			HOME_TEXT_OWNER.format(cmd.from_user.first_name, cmd.from_user.id),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/By_Azade'),
						InlineKeyboardButton("🤖Other Bots", url="https://t.me/KanalLinkleri")"),
					],
                    [
                        InlineKeyboardButton(
                            "🔗Source Code", url="https://github.com/muhammedfurkan/Instagram-Bot")
                    ],
                    [
                        InlineKeyboardButton(
                            "👨🏼‍🦯How To Use?", callback_data="help#subin"),
						InlineKeyboardButton("⚙️Update Channel",
						                     url="https://t.me/KanalLinkleri")

                    ]

				]
			)
		)


@ Client.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
	await cmd.reply_text(
		HELP,
		disable_web_page_preview = True,
		reply_markup = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/By_Azade'),
					InlineKeyboardButton("🤖Other Bots", url="https://t.me/KanalLinkleri")"),
					InlineKeyboardButton("⚙️Update Channel", url="https://t.me/KanalLinkleri")

				],
				[
					InlineKeyboardButton(
					    "🔗Source Code", url="https://github.com/By_Azade/Instagram-Bot"),
					InlineKeyboardButton(
					    "🧩Deploy Own Bot", url="https://heroku.com/deploy?template=https://github.com/muhammedfurkan/Instagram-Bot")
				]
			]
			)
		)

@ Client.on_message(filters.command("restart") & filters.private)
async def stop(bot, cmd):
	if str(cmd.from_user.id) != OWNER:
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name,
			                 cmd.from_user.id, USER, USER, USER, OWNER),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/By_Azade'),
						InlineKeyboardButton("🤖Other Bots", url="https://t.me/KanalLinkleri")")
					],
                    [
                        InlineKeyboardButton("🔗Source Code", url="https://github.com/By_Azade/Instagram-Bot"),
						InlineKeyboardButton("🧩Deploy Own Bot", url="https://heroku.com/deploy?template=https://github.com/muhammedfurkan/Instagram-Bot")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯How To Use?", callback_data="help#subin"),
						InlineKeyboardButton("⚙️Update Channel", url="https://t.me/KanalLinkleri")

                    ]
					
				]
			)
		)
		return
	msg = await bot.send_message(
		text="Restarting your bot..",
		chat_id=cmd.from_user.id
		)
	await asyncio.sleep(2)
	await msg.edit("All Processes Stopped and Restarted")
	os.execl(sys.executable, sys.executable, *sys.argv)
