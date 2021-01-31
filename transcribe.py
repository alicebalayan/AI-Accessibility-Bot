# Import libraries
from pydub import AudioSegment
from google.cloud import speech
from google.cloud.speech import *


def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    import io

    client = speech.SpeechClient()
    
    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        # sample_rate_hertz=16000,
        language_code="en-US",
        audio_channel_count=2
    )

    response = client.recognize(config=config, audio=audio)
    transcription=[]
    # print(response)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        transcription.append(result.alternatives[0].transcript)
    return transcription

        
# transcribe_file("recording/509648114_data/1-ColorfulPockets_0617.ogg")