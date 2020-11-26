# import discord
from discord.ext import commands
from discord.ext.commands import Context
import coc

from config import Config
from commands.war import create_war_commands
from coc_events.war import create_war_events

config = Config()
bot = commands.Bot(command_prefix='!')
coc_client = coc.login(
  config.coc_dev_email,
  config.coc_dev_password,
  key_names=config.coc_key_names,
  client=coc.EventsClient
)

@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')

# Ping pong test command
@bot.command(name='ping')
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def ping(ctx:Context):
  await ctx.send('Pong')

# Commands
create_war_commands(config, bot, coc_client)

# CoC Events
create_war_events(config, bot, coc_client)

bot.run(config.bot_token)