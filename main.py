import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv("DISCORD_BOT_TOKEN")


intents = discord.Intents.default()  # Default intents (read messages, reactions, etc.)
intents.messages = True  # Explicitly enable message events if needed
intents.message_content = True
client=discord.Client(intents=intents)


@client.event
async def on_ready():
    print("helper bot is ready to use")

@client.event
async def on_message(message):
    if message.content.startswith("!hello"):
        await message.channel.send("hello,anything you want ? ")
    if message.content.startswith("!services"):
        response="to create a poll use the command !poll \n"
        response+="to create a survey use the command !survey \n"
        response+="to create an event use the command !event \n"
        await  message.channel.send(response)



client.run(TOKEN)
