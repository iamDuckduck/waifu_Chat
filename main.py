from chatgpt_wrapper import ChatGPT
from promptDrawing import promptForDrawing1
from promptDrawing import previewDrawing
from displayImage import switch_image
from chatgptPrompt import promptSetUp
from chatgptPrompt import promptSetup2
from chatgptPrompt import promptSetup3

print('processing to chatgpt')
bot = ChatGPT()


userChoice = input('1 for the most customized prompt \n'
                   '2 for creating a similar characteristic of a well-known character\n'
                   '3 for special prompt\n'
                   'Please input:')

while not (userChoice == '1' or userChoice == '2' or userChoice == '3'):
    userChoice = input('error. Please input 1,2 or 3:')


if userChoice == '1': # option 1
    preview = '1'

    while preview == '1':
        name = input("What is the name of your waifu? ")
        gender = input("What is the gender of your waifu?(female or male) ").lower()
        if gender == 'female':
            gender = '1girl'
        elif gender == 'male':
            gender = '1boy'

        hair = (input("What is the hair color of your waifu? ") + " hair")
        eye = (input("What is the eye color of your waifu? ") + " eyes")
        clothes = input("What clothes is your waifu wearing? ")
        trait = input("What Characteristics do you want your waifu to have? ")

        userPrompt = f"{gender}, {hair}, {eye}, {clothes}, {trait}"

        print('Previewing your waifu.')
        output = previewDrawing(hair, userPrompt)
        switch_image(output)
        preview = input('press 1 if you want to regenerate your waifu, else press 2:')

    bot = promptSetup2(name, trait, gender, hair, eye, clothes, bot)
    promptForDrawing1(bot, userPrompt, name)


if userChoice == '2':
    preview = '1'

    while preview == '1':
        name = input("What is the name of your waifu? ")
        series = input("from what series? ")
        hair = (input("What is the hair color of your waifu? ") + " hair")
        eye = (input("What is the eye color of your waifu? ") + " eyes")
        otherTrait = input('other things you would like to add?(Yes or No)')
        if otherTrait == 'Yes':
            otherTrait = input('please input:')
        else:
            otherTrait = ''

        userPrompt = f"{hair}, {eye}, {otherTrait}"
        print('Previewing your waifu.')
        output = previewDrawing(hair, userPrompt)
        switch_image(output)
        preview = input('press 1 if you want to regenerate your waifu, else press 2: ')

    bot = promptSetUp(name, series)
    promptForDrawing1(bot, userPrompt, name)


if userChoice == '3': # option 3
    preview = '1'

    while preview == '1':
        name = input("What is the name of your waifu? ")
        gender = input("What is the gender of your waifu?(female or male) ").lower()

        hair = (input("What is the hair color of your waifu? ") + " hair")
        eye = (input("What is the eye color of your waifu? ") + " eyes")
        clothes = input("What clothes is your waifu wearing? ")
        trait = input("What Characteristics do you want your waifu to have? ")

        # this for image generation
        if gender == 'female':
            userPrompt = f"1girl, {hair}, {eye}, {clothes}, {trait}"
        elif gender == 'male':
            userPrompt = f"1boy, {hair}, {eye}, {clothes}, {trait}"

        print('Previewing your waifu.')
        output = previewDrawing(hair, userPrompt)
        switch_image(output)
        preview = input('press 1 if you want to regenerate your waifu, else press 2:')

    bot = promptSetup3(name, trait, gender, bot)
    promptForDrawing1(bot, userPrompt, name)



