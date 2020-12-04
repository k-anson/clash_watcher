from dotenv import load_dotenv
import os

load_dotenv()

class Config():
  # Discord configuration
  bot_token:str
  coc_channel:int

  # CoC configuration
  coc_dev_email:str
  coc_dev_password:str
  coc_key_names:str
  clan_tag:str
  coc_api_key:str

  # Gif configuration
  attack_gifs:bool
  giphy_token:str
  tenor_token:str

  def __init__(self):
    self.bot_token = os.getenv('BOT_TOKEN')
    self.coc_channel = int(os.getenv('COC_CHANNEL'))

    self.coc_dev_email = os.getenv('COC_DEV_EMAIL')
    self.coc_dev_password = os.getenv('COC_DEV_PASSWORD')
    self.coc_key_names = os.getenv('COC_KEY_NAMES')
    self.clan_tag = os.getenv('CLAN_TAG')
    self.coc_api_key = os.getenv('COC_API_KEY')

    if (os.getenv('ATTACK_GIFS') == 'True'): self.attack_gifs = True
    else: self.attack_gifs = False
    self.giphy_token = os.getenv('GIPHY_TOKEN')
    self.tenor_token = os.getenv('TENOR_TOKEN')