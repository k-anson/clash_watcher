from discord.ext import commands
from discord.ext.commands import Bot, Context, CommandError
from discord import TextChannel
from coc import EventsClient, ClanWar
from datetime import date, datetime

from config import Config

from utils.attack_reactions import Attack_Reactions

def create_war_commands(config:Config, bot:Bot, coc_client:EventsClient):
  attack_reactions = Attack_Reactions(config)

  @bot.group(invoke_without_command=True)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def war(ctx:Context):
    # TODO: send tooltip
    pass

  @war.command(name='analyze')
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def analyze_war(ctx:Context):
    current_war:ClanWar = await coc_client.get_current_war(tag=config.clan_tag)
    # Grab our war log
    # Grab enemy war log

  @war.command(name='test')
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def  test(ctx:Context, attacker_name:str, defender_name:str):
    gif = attack_reactions.random_good_gif('', '')
    await bot.get_channel(config.coc_channel).send(attack_reactions.random_good_line(
      WarMemberMock(attacker_name),
      WarMemberMock(defender_name)
    ))
    await bot.get_channel(config.coc_channel).send(gif)

# Analyze list of wars
def analyze_war_log(war_log:list):
  pass

class WarMemberMock():
  name:str

  def __init__(self, name):
    self.name = name