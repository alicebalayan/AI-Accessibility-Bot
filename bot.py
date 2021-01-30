import discord
import threading
import asyncio
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
import websockets
from discord import channel
import substring
import random
import requests 
from discord.ext import commands
import aiohttp
from io import BytesIO
from requests.sessions import session

TOKEN = open("token.txt").read()

# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)


def process_content(text):
	tokenized = word_tokenize(text)
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)
			
	except Exception as e:
		print(str(e))

class MyClient(discord.Client):
	# async def socket(self,websocket,path):
    #     # content=""
    #     # while true:
    #     #     await asyncio.sleep(2)
    #     pass
        
	async def on_ready(self):
		print(f'{self.user} has connected to Discord!')
		print('Servers connected to:')
		for server in client.guilds:
			print(server)
        
        # start_server = websockets.serve(self.socket, host=None,port=8765)

        # asyncio.get_event_loop().run_until_complete(start_server)
        # asyncio.get_event_loop().run_forever()
	async def on_message(self,message):	
		if message.author == self.user:
			return
		print(message.content)
		process_content(str(message.content))
		
	async def on_member_join(self,member):
		print("new member joined")
        
	

client = MyClient()

client.run(TOKEN)