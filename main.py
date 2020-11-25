# import discord
from discord.ext import commands
import coc

from config import Config
from commands.war import create_war_commands
from coc_events.war import create_war_events

config = Config()
bot = commands.Bot(command_prefix='!')
coc_client = coc.login(
  config.coc_dev_email,
  config.coc_dev_password,
  key_names='coc.py',
  throttle_limit=2,
  client=coc.EventsClient
)
# api = Clash_API(config)

@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')

# Commands
create_war_commands(config, bot, coc_client)

# CoC Events
create_war_events(config, bot, coc_client)

bot.run(config.bot_token)