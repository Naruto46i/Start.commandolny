import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6337844046:AAGFdgIBZ21XfQGtMc6_CEPSIDEHCG5zVOY')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text
