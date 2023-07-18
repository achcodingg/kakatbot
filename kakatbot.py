import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='i.')

token = "токен бота сюда"

curseWord = ['ты', 'я']

@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f"{message.author.mention} я запрещаю вам какать")
    else:
        return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```Укажите аргументы```')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("```Вы не имеете права```")


@client.event
async def on_ready():
    print("start")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="i.info"))

@client.command()
async def info(ctx):
    await ctx.send('test_info')

client.run(token)
