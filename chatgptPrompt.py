from chatgpt_wrapper import ChatGPT  # https://stackoverflow.com/questions/31235376/pycharm-doesnt-recognize-installed-module, if chatgpt_wrapper not working try to find solution from the link
from emotionalAnalysis import printAndPlay


def promptSetUp(name, series, bot): ##receive prompt setting from the user
    print("Generating your waifu in chatGPT, please wait......")

    bot.ask(
        "I want you to act like " + name + " from " + series + ". I want you to respond and answer like " + name + ". Using the tone, manner and vocabulary " + name + " would use. Do not write any explanations. Only answer like " + name + ". You must know all of the knowledge of " + name + "." + "My first sentence is Hi " + name + ".")
    success, response, message = bot.ask(f'Hi {name}')
    printAndPlay(response, name)
    return bot


def promptSetup2(name, trait, gender, hair, eye, clothes, bot):
    print("Generating your waifu, please wait......")

    success, character, message = bot.ask("Can you help me to create a character in 200 words, with the name " + name +
                        " and the following characteristics " + trait + ". The character also need to be " + gender +
                        ". The character also need to have " + hair + eye + clothes )

    print(character)
    success, temp, message = bot.ask(
        "I want you to act like " + name + ". I want you to respond and answer like "
        + name + ". Using the tone, manner and vocabulary "
        + name + "would use. Do not write any explanations. Only answer like "
        + name + ". You must know all of the knowledge of " + name + "." +
        "Please reply me in less than 2 sentences.")

    printAndPlay(temp, name)
    return bot


def promptSetup3(name, trait, gender, bot):
    print("Generating your waifu, please wait......")

    success, response, message = bot.ask("I want you to act as my friend " + name + ","
                                         " a Japanese high school " + gender + " with a personality of" + trait + ","
                                         " who attends the same school as me."
                                         " please start the conversation by greeting me,"
                                         " and keep your responses to around 3 or 4 sentences."
                                         " we will chat like normal friends would!")

    printAndPlay(response, name)
    return bot

