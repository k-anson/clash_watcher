from dotenv import load_dotenv
import os

load_dotenv()

class Config():
  bot_token:str
  coc_channel:int
  coc_dev_email:str
  coc_dev_password:str
  clan_tag:str
  coc_api_key:str
  giphy_token:str
  tenor_token:str

  def __init__(self):
    self.bot_token = os.getenv('BOT_TOKEN')
    self.coc_channel = int(os.getenv('COC_CHANNEL'))
    self.coc_dev_email = os.getenv('COC_DEV_EMAIL')
    self.coc_dev_password = os.getenv('COC_DEV_PASSWORD')
    self.clan_tag = os.getenv('CLAN_TAG')
    self.coc_api_key = os.getenv('COC_API_KEY')
    self.giphy_token = os.getenv('GIPHY_TOKEN')
    self.tenor_token = os.getenv('TENOR_TOKEN')