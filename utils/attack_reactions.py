from coc import ClanWarMember
import random
import requests

from config import Config
from coc.wars import ClanWar

giphy_url = 'https://api.giphy.com/v1/random'
tenor_url = 'https://api.tenor.com/v1/random'

class Attack_Reactions():
  config:Config

  def __init__(self, config):
    self.config = config

  def random_good_line(self, attacker:ClanWarMember, defender:ClanWarMember):
    lines = [
      f'Great attack {attacker.name}!',
      f'Good stuff {attacker.name}!'
    ]
    return random.choice(lines)

  def random_decent_line(self, attacker:ClanWarMember, defender:ClanWarMember):
    pass

  def random_bad_line(self, attacker:ClanWarMember, defender:ClanWarMember):
    pass

  def random_good_gif(self, attacker:ClanWarMember, defender:ClanWarMember):
    tags = [
      'good stuff'
    ]
    return self.random_gif(random.choice(tags))

  def random_decent_gif(self, attacker:ClanWarMember, defender:ClanWarMember):
    pass

  def random_bad_gif(self, attacker:ClanWarMember, defender:ClanWarMember):
    pass

  def random_gif(self, tag):
    if (random.choice([False])):
      return self.random_giphy_gif(tag)
    else:
      return self.random_tenor_gif(tag)

  def random_giphy_gif(self, tag):
    pass

  def random_tenor_gif(self, tag):
    params = { 'key': self.config.tenor_token, 'q': tag }
    return requests.get(tenor_url, params=params).json()['results'][0]['url']