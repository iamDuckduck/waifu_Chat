import os
import azure.cognitiveservices.speech as speechsdk
import json

# Load the JSON file
with open('certification.json') as f:
    data = json.load(f)

# Access the variables
subscription = data['subscription']
region = data['region']



def generate_xml(message, style):
    style_values = {
        # cheerful, unfriendly, excited, sad, friendly, angry.
        "cheerful": (25.00, 25, 1.5),
        "unfriendly": (25.00, 20, 1.5),
        "excited": (25.00, 25, 1.5),
        "sad": (25.00, 30, 1.5),
        "friendly": (25.00, 20, 1),
        "angry": (25.00, 20, 1.5),
        # Add more styles and their corresponding values here
        # rate, pitch, styledegree
    }

    rate, pitch, styledegree = style_values[style]
    xml = f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">\n'
    xml += f'    <voice name="en-US-JennyNeural">\n'
    xml += f'        <prosody rate="+{rate}%" pitch="{pitch}%">'
    xml += f'             <mstts:express-as style="{style}" styledegree="{styledegree}">\n'
    xml += f'                 {message}\n'
    xml += f'             </mstts:express-as>\n'
    xml += f'        </prosody>'
    xml += f'    </voice>\n'
    xml += f'</speak>'
    return xml



def playAudio(xml):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    # use this if you put your set in certification: speech_config = speechsdk.SpeechConfig(subscription=subscription, region=region)
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    ssml_string = xml
    result = speech_synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("C:/Users\/user\PycharmProjects/testing1/ssml.wav")



# playAudio(generate_xml('nice to meet you! i am yuki!', 'cheerful'))


# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-text-to-speech?tabs=windows%2Cterminal&pivots=programming-language-python

# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-speech-synthesis?tabs=browserjs%2Cterminal&pivots=programming-language-python

# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-synthesis-markup-voice

# if using mac, check this 2 websites,
# https://stackoverflow.com/questions/41326387/get-error-when-try-to-install-pil
# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-text-to-speech?tabs=macos%2Cterminal&pivots=programming-language-python