import discord
import threading
import asyncio
from discord import channel
import substring
import random
import requests 
from discord.ext import commands
import aiohttp
from io import BytesIO
from requests.sessions import session


TOKEN = open("token.txt").read()


		


class MyClient(discord.Client):
	
	async def on_ready(self):
		print(f'{self.user} has connected to Discord!')
		print('Servers connected to:')
		for server in client.guilds:
			print(server)
	
	async def on_message(self,message):	
		if message.author == self.user:
			return
		print(message.content)
		
	async def on_member_join(self,member):
		print("new member joined")
	

client = MyClient()



client.run(TOKEN)