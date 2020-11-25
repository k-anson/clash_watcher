from discord.ext.commands import Bot
from discord import TextChannel
import coc
from coc import EventsClient, ClanWar, WarAttack

from config import Config
from utils.attack_reactions import Attack_Reactions

def create_war_events(config:Config, bot:Bot, coc_client:EventsClient):
  attack_reactions = Attack_Reactions(config)

  @coc_client.event
  @coc.WarEvents.state(tags=config.clan_tag)
  async def on_war_state_change(old_war:ClanWar, new_war:ClanWar):
    coc_channel = bot.get_channel(config.coc_channel)

    await coc_channel.send(f'War status changed: {new_war.status}')

  @coc_client.event
  @coc.WarEvents.war_attack(tags=config.clan_tag)
  async def on_war_attack(attack:WarAttack, war:ClanWar):
    coc_channel = bot.get_channel(config.coc_channel)

    # Attacker is from our clan
    if (attack.attacker.clan.tag == config.clan_tag):
      gif = attack_reactions.random_good_gif(attack.attacker, attack.defender)
      await coc_channel.send(attack_reactions.random_good_line(attack.attacker, attack.defender))
      await coc_channel.send(gif)
    else:
      await coc_channel.send(f'{attack.defender.name} defended against {attack.attacker.name}')