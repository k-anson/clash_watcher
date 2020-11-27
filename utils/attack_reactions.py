from coc import ClanWarMember
import random
import requests

from config import Config
from coc.wars import ClanWar

giphy_url = 'https://api.giphy.com/v1/random'
tenor_url = 'https://api.tenor.com/v1/search'

class Attack_Reactions():
  config:Config

  def __init__(self, config):
    self.config = config

  def random_great_gif(self, attacker:ClanWarMember, defender:ClanWarMember):
    tags = [
      'too easy',
      'perfection',
      'genius',
      'amazing',
      'holy shit'
    ]
    tag = random.choice(tags)
    print(f'fetching great gif using {tag} tag for {attacker.name}\'s attack')
    return self.random_gif(tag)

  def random_good_gif(self, attacker:ClanWarMember, defender:ClanWarMember):
    tags = [
      'nice',
      'yes',
      'too easy',
      'genius',
      'amazing'
    ]
    tag = random.choice(tags)
    print(f'fetching good gif using {tag} tag for {attacker.name}\'s attack')
    return self.random_gif(tag)

  def random_decent_gif(self, attacker:ClanWarMember, defender:ClanWarMember):
    tags = [
      'nice',
      'yes',
      'alright',
      'not bad'
    ]
    tag = random.choice(tags)
    print(f'fetching decent gif using {tag} tag for {attacker.name}\'s attack')
    return self.random_gif(tag)

  def random_bad_gif(self, attacker:ClanWarMember, defender:ClanWarMember):
    tags = [
      'be strong',
      'oh god',
      'please no',
      'what the fuck',
      'you need help'
    ]
    tag = random.choice(tags)
    print(f'fetching bad gif using {tag} tag for {attacker.name}\'s attack')
    return self.random_gif(tag)

  def random_terrible_gif(self, attacker:ClanWarMember, defender:ClanWarMember):
    tags = [
      'depression',
      'oh god',
      'please no',
      'what the fuck',
      'you need help',
      'rip'
    ]
    tag = random.choice(tags)
    print(f'fetching terrible gif using {tag} tag for {attacker.name}\'s attack')
    return self.random_gif(tag)

  def random_gif(self, tag):
    if (random.choice([False])):
      return self.random_giphy_gif(tag)
    else:
      return self.random_tenor_gif(tag)

  def random_giphy_gif(self, tag):
    pass

  def random_tenor_gif(self, tag):
    params = {
      'key': self.config.tenor_token,
      'q': tag,
      'limit': 1,
      'pos': random.randint(1, 50)
    }
    return requests.get(tenor_url, params=params).json()['results'][0]['url']