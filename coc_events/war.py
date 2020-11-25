from discord.ext.commands import Bot
import coc
from coc import EventsClient, ClanWar, WarAttack

from config import Config
from utils.attack_reactions import Attack_Reactions

def create_war_events(config:Config, bot:Bot, coc_client:EventsClient):
  @coc_client.event
  @coc.WarEvents.state(tags=config.clan_tag)
  async def on_war_state_change(old_war:ClanWar, new_war:ClanWar):
    bot.get_channel(config.coc_channel).send(f'War status changed: {new_war.status}')

  @coc_client.event
  @coc.WarEvents.war_attack(tags=config.clan_tag)
  async def on_war_attack(attack:WarAttack, war:ClanWar):
    # Attacker is from our clan
    if (attack.attacker.clan.tag == config.clan_tag):
      bot.get_channel(config.coc_channel).send(Attack_Reactions.random_good_line(attack.attacker, attack.defender))
    else:
      bot.get_channel(config.coc_channel).send(f'{attack.defender.name} defended against {attack.attacker.name}')