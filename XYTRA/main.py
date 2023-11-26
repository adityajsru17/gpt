import os
import random
from pyrogram import Client, filters

from XYTRA.welcome import welcome_msgs
from XYTRA.exit import exit_msgs

# Set your API key and API hash as environment variables
api_key = os.environ.get("API_KEY")
api_hash = os.environ.get("API_HASH")

# Create a new Pyrogram client
bot = Client("my_bot", bot_token="6526084223:AAHRX5cIwWCyMN1vqmseXQXl1kNFFulevbs", api_id=6435225, api_hash=4e984ea35f854762dcde906dce426c2d)

@bot.on_message(filters.group & filters.new_chat_members)
async def welcome_new_members(client, message):
    chat_id = message.chat.id
    for user in message.new_chat_members:
        # Generate a random welcome message
        welcome_msg = random.choice(welcome_msgs)
        # Send the welcome message to the group
        await bot.send_message(chat_id, welcome_msg)

@bot.on_message(filters.group & filters.left_chat_member)
async def send_exit_message(client, message):
    chat_id = message.chat.id
    user = message.left_chat_member
    # Generate a random exit message
    exit_msg = random.choice(exit_msgs)
    # Send the exit message to the group
    await bot.send_message(chat_id, exit_msg)

# Start the bot
bot.run()
