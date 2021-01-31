const Discord = require('discord.js');
const fs = require('fs');
const { Readable } = require('stream');
//const auth = require('./token.json');
const client = new Discord.Client();
const googleSpeech = require('@google-cloud/speech')

const googleSpeechClient = new googleSpeech.SpeechClient()
const token = fs.readFileSync('./token.txt', 'ascii', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
//Has the Google API service been started up?
var joined = false;
class Silence extends Readable {
    _read() {
        this.push(SILENCE_FRAME);
    }
}
//Important (initializes bot)
client.once('ready', () => {
    console.log('Ready!');

});


const CMD = "!join";

client.on('message', async msg => {
    if (msg.content === "!join") {
        const member = msg.member
        memberVoiceChannel = member.voice.channel;

        if (!memberVoiceChannel) {
            return
        }

        const connection = await memberVoiceChannel.join()
        currentChannelName = memberVoiceChannel.name;


        //this prevents multiple requests per speech snippet to the google API
        if (joined) {
            return;
        }


        const receiver = connection.receiver

        //due to a restriction on Discords part, a bot cannot receive audio from a call until it plays audio. To circumvent this,
        //our bot continuously plays a clip of silence.
        connection.play(new Silence(), { type: 'opus' });
        connection.on('speaking', (user, speaking) => {
            if (!speaking || !user) {
                return
            }
            joined = true;
            // this creates a 16-bit signed PCM, stereo 48KHz stream
            const audioStream = receiver.createStream(user, { mode: 'pcm' })
            let writeStream = fs.createWriteStream('./recording.pcm', {})
            this.us = userStream
            this.ws = writeStream

            this.us.on("data", (chunk) => {
                console.log(chunk)
                this.us.pipe(this.ws)
            })
            this.ws.on("pipe", console.log)
                //Configuring stream to pipe data out to the Google API.
                // const requestConfig = {
                //     encoding: 'LINEAR16',
                //     sampleRateHertz: 48000,
                //     languageCode: 'en-US'
                // }
                // const request = {
                //     config: requestConfig
                // }

            // const recognizeStream = googleSpeechClient
            //     .streamingRecognize(request)
            //     .on('error', console.error)
            //     .on('data', response => {
            //         const transcription = response.results
            //             .map(result => result.alternatives[0].transcript)
            //             .join('\n')
            //             .toLowerCase();

            //         //Sets the current channel's name for transcript purposes.
            //         currentChannelName = connection.channel.name;
            //         //Goes through the opt in list and sends a private message to each user present containing the transcription.
            //         Object.keys(optin).forEach(u => discordClient.users.get(u).send(createEmbedFromUserTranscript(user, transcription)).then(msg => { msg.delete({ timeout: deleteTime }) }));

            //         console.log(`${user.username}: ${transcription}`);

            //     })

            // const convertTo1ChannelStream = new ConvertTo1ChannelStream()

            // audioStream.pipe(convertTo1ChannelStream).pipe(recognizeStream)

            // audioStream.on('end', async() => {
            //     console.log('audioStream end')

            // })
        })
    }
    // const match = msg.content.match(CMD); //array of regex match
    // if (match) {
    //     msg.author.join();
    // } else {
    //     console.log(msg.author.username + ": " + msg);
    // }

});

// console.log(token);
//Important (logs in)
//client.login(token.token); //for json
client.login(token);