# Team 3 - Discord ASL Translator Bot
[![Documentation Status](https://readthedocs.org/projects/team-3/badge/?version=latest)](https://team-3.readthedocs.io/en/latest/?badge=latest)

- [Team 3 - Discord ASL Translator Bot](#team-3---discord-asl-translator-bot)
	+ [About Our Project](#about-our-project)
    + [Quick Set Up](#quick-set-up)
    + [Invite The Bot To Your Discord Server](#invite-the-bot-to-your-discord-server)
    + [ASL Discord Bot Documentation](#asl-discord-bot-documentation)
    + [Natural Language Processing](#natural-language-processing)
    + [2D Animation](#2d-animation)
    + [ASL Database](#asl-database)
    + [Gifs Support](#gifs-support)
    + [Security](#security)
   
### About Our Project 
This project was inspired by the Accessibility Competition at CSUN to help deaf students talk with others on voice platforms such as Discord. 

Our bot takes the audio from the voice channel, gets the text, and converts it to a 2D Animation in ASL. 
Also, our bot can convert text messages that transfers json from discord to websocket into 2D ASL animation as well as send gifs (giphy API) by the user's request. (To find out how, visit the ASL bot documentation).

### Quick Set Up
Type into your terminal:
```
python3
import nltk
nltk.download('all')
```
Then the bot will wake up.

### Invite The Bot To Your Discord Server
(link sharing disabled at the moment)

### ASL Discord Bot Documentation
(rtd link here) 

### Natural Language Processing
Our ASL Bot processes the words in the following way: removes words that aren't used, adds superlatives, converts superlatives to their roots, checks for word pairs (good morning), looks for words that mean time. 

### 2D Animation
Our ASL Discord Bot uses this [JS library](https://github.com/aslfont/sign-puppet) to display 2D animations to the user. 
(add code snippet here on the final day)

### ASL Database 
Our ASL Discord Bot relies on this [database](https://asl-lex.org/) to get relevant data points that we are using to map the 2D animations. This dataset contains sign durations, hand/body/fingers/eyebrows positions, and other movements that help us get more accurate animations.
(share the link to the file on the final day)

### Gifs Support
Our  ASL Discord Bot support a subset of ASL gifs that contain most common phrases and slang to keep ASL fun. Because who doesn't want fun? To learn how to run the commands, refer to the documentation about the bot. 
We are using [giphy](https://giphy.com/signwithrobert/) and narrowing down the search to the "Sign with Robert" content as it is the most relevant and accurate. 
[Home Run By Sign with Robert](http://gph.is/2j6qHob)
### Security
All of the auth keys are stored privately and not shared with anyone else outside of the development team. In addition, no user's information is been stored (audio recording).
### Code snippets
Capturing the audio and zipping the file 
```Python
if message.content.startswith("!stop"):
			await message.channel.send(".end")
			url="http://localhost:3004/"+servers[guild]["recordingID"]+"?format=flac&container=aupzip"
   ```
