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

# This list is probably incomplete, but these are the words that just don't exist at all in ASL/will more often than not be skipped
REMOVED_WORDS = ['a','an', 'the','is','am','be','are', 'to']

time_words_file = open('time_words.txt', 'r')
TIME_WORDS = time_words_file.read().split()

PHRASE_ENDS = ['.',',',';',':']

GIFToken=open("gifKey.txt").read()
URL="https://api.giphy.com/v1/gifs/search?api_key="+GIFToken+'&q="'

pos_to_lex = {
	"CC"  : "Minor",
	"CD"  : "Number",
	"DT"  : "Minor",
	"EX"  : "Adverb",
	"FW"  : "Noun",
	"IN"  : "Minor",
	"JJ"  : "Adjective",
	"JJR" : "Adjective",
	"JJS" : "Adjective",
	"MD"  : "Verb",
	"NN"  : "Noun",
	"NNP" : "Noun",
	"NNPS": "Noun",
	"NNS" : "Noun",
	"PDT" : "Minor",
	"PRP" : "Minor",
	"PRP$": "Minor",
	"RB"  : "Adjective",
	"RP"  : "Minor",
	"UH"  : "Minor",
	"VB"  : "Verb",
	"VBD" : "Verb",
	"VBG" : "Verb",
	"VBN" : "Verb",
	"VBP" : "Verb",
	"VBZ" : "Verb",
	"WDT" : "Minor",
	"WP"  : "Minor",
	"WP$" : "Minor",
	"WRB" : "Minor"
}


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
		#print(tagged)

		pseudo_ASL = pseudo_translate(tagged)

		print(pseudo_ASL)
			
	except Exception as e:
		print(str(e))

# Takes a list of tagged words and does the following:
#	1. Removes words that aren't used in ASL (articles such as "the" or "a", be verbs such as "be" and "am")
#	2. Adds superlatives (in ASL, "biggest" could be signed as BIG + TOP).  
# 		Note, this is a naiive approach and should probably be changed at some point.
#	3. Uses reduplication for plurals (when it encounters a plural noun, such as "dogs", it does the sign twice) TODO
#	3. Converts superlatives and comparatives to their roots.  For instance, "bigger" --> "big" TODO
#	4. Checks for word pairs that have a single sign, such as "Good morning" or "Week last" TODO
#	5. Changes some word ordering, specifically for:
#		a. Time.  In ASL, timing words come first.  So rather than "I washed my car last week" it's WEEK-LAST I WASH CAR
#		b. Possibly other things? More research required

def pseudo_translate(tagged):

	# Remove unused words
	tagged = [k for k in tagged if k[0][0].lower() not in REMOVED_WORDS]
	#print(tagged)
	
	# Add superlatives
	words = []
	for tag in tagged:
		words.append(tag[0])
		#print(tag[0][1])
		if tag[0][1] == 'JJS':
			words.append(('top','JJ'))

	# TODO Add reduplication of plural nouns

	# TODO convert superlatives and comparatives to their roots (ie "bigger" --> "big")

	# TODO check for word pairs

	# Change time ordering 
	for i in range(len(words)):
		word = words[i]
		if word[0] in TIME_WORDS:
			move_to_start_of_sentence(words, i)

	# Convert Parts of Speech to Lexical Classes
	return_words = []
	for word in words:
		word = list(word)
		if word[1] in pos_to_lex:
			print(word[1])
			word[1] = pos_to_lex.get(word[1])
		else:
			word[1] = "Symbol"
		
		return_words.append([word[0], word[1]])

	return return_words

# Takes list of words, and position of word to be moved
def move_to_start_of_sentence(words, pos):
	i = pos
	while (i > 0):
		if words[i][0] in PHRASE_ENDS:
			word = words.pop(pos)
			words.insert(i+1, word)
			return
		i -= 1
	word = words.pop(pos)
	words.insert(0, word)


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
		if message.content.startswith("!asl"):
			endQuery=' @ Sign with Robert"'
			
			query=URL+message.content[4:].strip()+endQuery
			response=requests.get(query)
			response=json.loads(response.content)
			print(query)
			sendGif="No result"
			for gif in response["data"]:
				if gif["username"]=="signwithrobert" and not gif["embed_url"]=="https://giphy.com/embed/3o6ZtmnidXHIoQJfH2":
					sendGif=gif["embed_url"]
					break
			# print(response)
			await message.channel.send(sendGif)

		
	async def on_member_join(self,member):
		print("new member joined")
        
	

client = MyClient()

client.run(TOKEN)