import replicate
import os
from displayImage import switch_image
from emotionalAnalysis import printAndPlay
from emotionalAnalysis import emotionalAnalysis
from TTS import generate_xml
from TTS import playAudio
import json

# Load the JSON file
with open('certification.json') as f:
    data = json.load(f)

# Access the variables
REPLICATE_API_TOKEN = data['REPLICATE_API_TOKEN']


def promptForDrawing1(bot, userPrompt, name):
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
    image = "Please list no more than 6 keywords from our conversation, we will use them for image generator." \
            "please do it with this format\n." \
            "example_keyword1, example_keyword2, example_keyword3..."

    while True:
        user_input = input("You : ")

        if user_input == "exit":
            break

        # when user_input == Image. it lets user input again, then an image will be generated within an audio
        if user_input == "Image.":
            user_input = input("You : ")

            # send user's message to chatgpt, process emotional analysis and turn them to xml.
            # also save emotion to emotion variable for later use
            success, response, message = bot.ask(user_input)
            emotion = emotionalAnalysis(response)
            xml = generate_xml(response, emotion)

            # tell chatgpt to list keyword and forward to image drawing API
            success, keyword, message = bot.ask(image)
            print("keyword: ", keyword, "Generating Image......")

            model = replicate.models.get("cjwbw/anything-v3-better-vae")
            version = model.versions.get("09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65")

            # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
            inputs = {
                # Input prompt
                'prompt': "masterpiece, best quality, illustration, beautiful detailed, finely detailed, "
                          "dramatic light, intricate details, colorful, lighting, portrait"
                          "" + userPrompt + keyword + emotion,

                # The prompt or prompts not to guide the image generation (what you do
                # not want to see in the generation). Ignored when not using guidance.
                'negative_prompt': "lowres, bad anatomy, bad hands, text, error, missing fingers,"
                                   " extra digit, fewer digits, cropped, worst quality, low quality,"
                                   " normal quality, jpeg artifacts, signature, watermark, username,"
                                   " blurry, artist name",

                # Width of output image. Maximum size is 1024x768 or 768x1024 because
                # of memory limits
                'width': 512,

                # Height of output image. Maximum size is 1024x768 or 768x1024 because
                # of memory limits
                'height': 512,

                # Number of images to output
                'num_outputs': 1,

                # Number of denoising steps
                # Range: 1 to 500
                'num_inference_steps': 20,

                # Scale for classifier-free guidance
                # Range: 1 to 20
                'guidance_scale': 7,

                # Choose a scheduler.
                'scheduler': "DPMSolverMultistep",

                # Random seed. Leave blank to randomize the seed
                # 'seed': ...,
            }

            # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema
            output = version.predict(**inputs)
            switch_image(output[0])
            print(name, ": ", response)
            playAudio(xml)
        else:
            success, response, message = bot.ask(user_input)
            printAndPlay(response, name)




def previewDrawing(hair, userPrompt):
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
    model = replicate.models.get("cjwbw/anything-v3-better-vae")
    version = model.versions.get("09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65")

    # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
    inputs = {
        # Input prompt
        'prompt': "masterpiece, best quality, 1girl, age friendly " + hair + userPrompt,

        # The prompt or prompts not to guide the image generation (what you do
        # not want to see in the generation). Ignored when not using guidance.
        # 'negative_prompt': ...,

        # Width of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'width': 512,

        # Height of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'height': 512,

        # Number of images to output
        'num_outputs': 1,

        # Number of denoising steps
        # Range: 1 to 500
        'num_inference_steps': 20,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 7,

        # Choose a scheduler.
        'scheduler': "DPMSolverMultistep",

        # Random seed. Leave blank to randomize the seed
        # 'seed': ...,
    }

    # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema
    output = version.predict(**inputs)
    return output[0]


