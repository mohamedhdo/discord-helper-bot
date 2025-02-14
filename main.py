from http.client import responses

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from numpy.lib.recfunctions import join_by

load_dotenv()

TOKEN=os.getenv("DISCORD_BOT_TOKEN")





intents = discord.Intents.default()
intents.messages = True
intents.message_content = True




bot=commands.Bot(command_prefix="!",intents=intents)

poll_messages={}




@bot.event
async def on_ready():
    print("helper bot is ready to use")


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention} , anything you need ? ")


@bot.command(name="guide")
async def services(ctx):
    response = f"hello {ctx.author.mention} , here is what you can do :\n"
    response += "To create a poll use the command !poll question option1 option2 ... option10\n"
    response += "To delete a poll use the command !deletepoll question  \n"
    response+="Note : -You can list at least 2 and at most 10 options for your poll \n"
    response+="            -You can only delete polls that you created\n"
    response+='            -The question must be between quotes ("")'
    await ctx.send(response)


@bot.command(name="poll")
async def create_poll(ctx,question,*options):
    if len(options)<2:
        await ctx.send("The poll should have at least two options ")
        return
    elif len(options)>10:
        await ctx.send("The poll should have at most 10 options")
        return

    poll_message="@everyone "+question+"\n"


    reactions=["🅰️","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯"][:len(options)]

    poll_message += "\n".join(f"{reactions[i]} - {options[i]}" for i in range(len(options)))
    poll=await ctx.send(poll_message)
    for reaction in reactions:
        await poll.add_reaction(reaction)

    poll_messages[question.lower()]=[poll.id,ctx.author.id]






@bot.command(name="deletepoll")
async def delete_poll(ctx,question):
    if question.lower() in poll_messages:
        poll_id = poll_messages[question][0]
        if ctx.author.id== poll_messages[question][1]:
            try:
                message=await ctx.channel.fetch_message(poll_id)
                await message.delete()
                await ctx.reply("Poll message deleted successfully",mention_author=False)
            except discord.NotFound:
                await ctx.reply("Poll message not found",mention_author=False)
        else:
            await ctx.reply("You don't have the permission to delete this poll",mention_author=False)
    else:
        await ctx.reply("Invalid poll id",mention_author=False)

    poll_messages.pop(question)


@bot.command(name="event")
async def create_event(ctx):
    pass



@bot.command(name="deleteevent")
async def delete_event(ctx):
    pass






























bot.run(TOKEN)
