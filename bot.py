import discord
import threading
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from discord import channel
import substring
import random
import requests 
from discord.ext import commands
import aiohttp
from io import BytesIO
from requests.sessions import session
import json
import time

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
	async def on_ready(self):
		print(f'{self.user} has connected to Discord!')
		print('Servers connected to:')
		for server in client.guilds:
			print(server)

	async def on_message(self,message):	
		if message.author == self.user:
			return
		# print(message.content)
		process_content(str(message.content))
		# global data
		# print(data)
		data={
			"time":time.time(),
			"data":message.content
		}
		f = open("data", "w")

		f.write(json.dumps(data,indent=4))
		f.close()
		
	async def on_member_join(self,member):
		print("new member joined")
        
	

client = MyClient()

client.run(TOKEN)