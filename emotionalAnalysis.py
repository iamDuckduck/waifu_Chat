import openai
from TTS import generate_xml
from TTS import playAudio
import json

# Load the JSON file
with open('certification.json') as f:
    data = json.load(f)

# Access the variables
openAI_API_KEY = data['openAI_API_KEY']



# print chatgpt response and play the audio together
def printAndPlay(input, name):
    if input == []:
        input = 'error'
        print(input)

    xml = generate_xml(input, emotionalAnalysis(input))
    print(name, ": ", input)
    playAudio(xml)




# emotion analysis with a return value of emotion
def emotionalAnalysis(prompt):
    openai.api_key = openAI_API_KEY
    # get response from API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The following is a quote and whether it is cheerful, unfriendly, excited, sad, "
               "friendly, neutral, or angry:\n"
               "text:" + prompt,
        temperature=0,
        max_tokens=1024,
    )

    emotion = response.choices[0].text.replace("\n", "").lower()

    # we should have cheerful, unfriendly, excited, sad, friendly, neutral(friendly), angry.
    print('Emotion: ' + emotion)
    if emotion == 'neutral':
        emotion = 'friendly'
        print('updated emotion: ' + emotion)
        return emotion

    return emotion

# https://www.youtube.com/watch?v=pUApF66-PZg



# some example: you may use for testing the voice with emotions
# friendly:
# printAndPlay('Hello. nice too meet you.', 'Test:')
# cheerful:
# printAndPlay('Hello! nice too meet you. I am glad to be invited here!', 'Test:')
# unfriendly:”
# printAndPlay('ahh...... you again? Just make it quick', 'Test:')
# excited
# printAndPlay('Really really really!? I am so excited about it!', 'Test:')
# sad
# printAndPlay("I just failed my test.", 'Test:')
# angry
# printAndPlay("It's not like i like you or anything! don't piss me off!", 'Test:')
