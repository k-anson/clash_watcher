from coc import ClanWarMember
import random

from coc.wars import ClanWar

class Attack_Reactions():
  def random_good_line(attacker:ClanWarMember, defender:ClanWarMember):
    lines = [
      f'Great attack {attacker.name}!',
      f'Good stuff {attacker.name}!'
    ]
    return random.choice(lines)
  def random_good_gif(attacker:ClanWarMember, defender:ClanWarMember):
    gif_host = ['giphy', 'tenor']
    gifs = [
      f'/{random.choice(gif_host)} good stuff'
    ]
    return random.choice(gifs)

  def random_decent_line(attacker:ClanWarMember, defender:ClanWarMember):
    pass
  def random_decent_gif(attacker:ClanWarMember, defender:ClanWarMember):
    pass

  def random_bad_line(attacker:ClanWarMember, defender:ClanWarMember):
    pass
  def random_bad_gif(attacker:ClanWarMember, defender:ClanWarMember):
    pass