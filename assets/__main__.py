import random
import requests
import argparse
from uaharvester import *
from resources.headers import user_agents
from assets.colors import green, white, reset

class UAHarvestr:
	def __init__(self,args):
		self.api = "http://api.userstack.com/detect"
		self.params = {"access_key": "756fc7012c632887c7d7e2e5f4660d22", "ua": args.ua}
		self.headers = {"User-Agent": f"{random.choice(user_agents)}"}
		self.resp = requests.get(self.api, params = self.params, headers = self.headers).json()
		
	def on_connection(self, args):
		if args.crawler:
			print(f"""{white}
Crawler Information
┌ Category: {green}{self.resp['crawler']['category']}{white}
├─ Is crawler: {green}{self.resp['crawler']['is_crawler']}{white}
└─╼ Last seen: {green}{self.resp['crawler']['last_seen']}{reset}""")
			
		else:
			print(f"""{white}
Brand
┌ Name: {green}{self.resp['brand']}{white}
├─ Organization: {green}{self.resp['os']['family_vendor']}{white}
└──╼ Website: {green}{self.resp['url']}{white}

Device
┌ Name: {green}{self.resp['device']['name']}{white}
├─ Vendor: {green}{self.resp['os']['family_vendor']}{white}
├── Type: {green}{self.resp['device']['type']}{white}
└──╼ Is Mobile : {green}{self.resp['device']['is_mobile_device']}{white}

Operating System
┌ Name: {green}{self.resp['os']['name']}{white}
├─ Family: {green}{self.resp['os']['family']}{white}
├── Vendor: {green}{self.resp['os']['family_vendor']}{white}
└──╼ Website: {green}{self.resp['url']}{white}

Browser
┌ Engine: {green}{self.resp['browser']['engine']}{white}
├─ Name: {green}{self.resp['browser']['name']}{white}
├── Version: {green}{self.resp['browser']['version']}{white}
├─── Type: {green}{self.resp['type']}{white}
└───╼ User-Agent: {green}{self.resp['ua']}{white}""")
