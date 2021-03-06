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
    message = ''
    if new_war.state == 'notInWar':
      message = 'Started clan war search'
    elif new_war.state == 'preparation':
      message = f'Clan war opponent found: {new_war.opponent.name}'
    elif new_war.state == 'inWar':
      message = f'Clan war against {new_war.opponent.name} started'
    elif new_war.state == 'warEnded':
      message = f'War ended: we {new_war.status}'

    coc_channel = bot.get_channel(config.coc_channel)
    await coc_channel.send(message)

  if (config.attack_gifs):
    @coc_client.event
    @coc.WarEvents.war_attack(tags=config.clan_tag)
    async def on_war_attack(attack:WarAttack, war:ClanWar):
      coc_channel = bot.get_channel(config.coc_channel)
      gif = ''

      # Attacker is from our clan
      if (attack.attacker.clan.tag == config.clan_tag):
        if (attack.stars == 3):
          gif = attack_reactions.random_great_gif(attack.attacker, attack.defender)
        elif (attack.stars == 2 and attack.destruction >= 65):
          gif = attack_reactions.random_good_gif(attack.attacker, attack.defender)
        elif (attack.stars == 2 and attack.destruction < 65):
          gif = attack_reactions.random_decent_gif(attack.attacker, attack.defender)
        elif (attack.stars == 1 and attack.destruction < 70):
          gif = attack_reactions.random_bad_gif(attack.attacker, attack.defender)
        else:
          gif = attack_reactions.random_terrible_gif(attack.attacker, attack.defender)
        await coc_channel.send(f'{attack.attacker.name} ({attack.attacker.map_position}) attacked {attack.defender.name} ({attack.defender.map_position}) and got {attack.stars} stars with {attack.destruction}% destruction')
        await coc_channel.send(gif)
      else:
        pass