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

# This list is probably incomplete, but these are the words that just don't exist at all in ASL
REMOVED_WORDS = ['a','an', 'the','is','am','be','are']

# TODO get this list of time-words
TIME_WORDS = []

# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# Takes an English string and converts it to pseudo ASL
def process_content(text):
	tokenized = word_tokenize(text)
	tagged = []
	try:
		for i in tokenized:
			# Not sure why, but the words need to be tokenized twice.  This is just how they did it in the tutorial I watched /shrug
			word = nltk.word_tokenize(i)
			tagged.append(nltk.pos_tag(word))
		print(tagged)

		pseudo_ASL = pseudo_translate(tagged)
			
	except Exception as e:
		print(str(e))

# Takes a list of tagged words and does the following:
#	1. Removes words that aren't used in ASL (articles such as "the" or "a", be verbs such as "be" and "am")
#	2. Adds superlatives (in ASL, "biggest" could be signed as BIG + TOP).  
# 		Note, this is a naiive approach and should probably be changed at some point.
#	3. Converts superlatives and comparatives to their roots.  For instance, "bigger" --> "big" TODO
#	4. Checks for word pairs that have a single sign, such as "Good morning" or "Week last" TODO
#	5. Changes some word ordering, specifically for:
#		a. Time.  In ASL, timing words come first.  So rather than "I washed my car last week" it's LAST WEEK I WASH CAR
#		b. Possibly other things? More research required
def pseudo_translate(tagged):

	# Remove unused words
	tagged = [k for k in tagged if k[0][0].lower() not in REMOVED_WORDS]
	print(tagged)
	
	# Add superlatives
	words = []
	for tag in tagged:
		words.append(tag[0][0])
		if tag[0][1] == 'JJS':
			words.append('top')
	print(words)

	# TODO convert superlatives and comparatives to their roots (ie "bigger" --> "big")

	# TODO check for word pairs

	# Change time ordering TODO

	return list(map(lambda x: x.upper(), words))


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