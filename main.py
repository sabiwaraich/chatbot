# importing modules
import os
import webbrowser
import datetime
import wikipedia

# assistant name
assistant_name = open("assistant name.txt", "r")

# welcome message
print("Hi this is", assistant_name.read())

# while loop for looping the program
while True:

    # accepting input from user
    user_input = input()
    a = user_input

    if "hi" in a:
        print("how can i help you?")

    # user name
    elif "what is my name" in a:
        user_name = open("name.txt", "r")
        print(user_name.read())

    # telling time
    elif "date" in a:
        dt = datetime.datetime.now()
        print(dt.strftime("%d %B %Y"))

    # telling day of week
    elif "day" in a:
        dt = datetime.datetime.now()
        print(dt.strftime("%A"))

    # telling time
    elif "time" in a:
        dt = datetime.datetime.now()
        print(dt.strftime("%T"))

    # assistant name
    elif "what is your name" in a:
        assistant_name = open("assistant name.txt", "r")
        print(assistant_name.read())

    # opening browser
    elif "open browser" in a:
        print("Opening browser....")
        webbrowser.open("google.com")

    # opening spotify to listen to music
    elif "music" in a:
        print("opening spotify...")
        webbrowser.open("www.spotify.com")

    # changing user name
    elif "change my name" in a:
        x = input("what's your new name:")
        f = open("name.txt", "w")
        f.write(x)
        f.close()
        print("Your new name is ", x)

    # changing assistant name
    elif "change your name" in a:
        x = input("what new name you want to give me?  ")
        f = open("assistant name.txt", "w")
        f.write(x)
        f.close()
        print("My new name is ", x)

    # shutting down pc
    elif "shut down the pc" in a:
        conf = input("Are you sure you want to shut down the pc (yes/no): ")
        if conf == "yes":
            os.system("shutdown /s /t 10")
        else:
            print("command denied")

    # search in  youtube
    elif "search video" in a:
        video = input("what you want to see :")
        print("searching on youtube for ", video)
        webbrowser.open("https://www.youtube.com/results?search_query=" + video)

    # opening youtube
    elif "youtube" in a:
        print("opening youtube...")
        webbrowser.open("www.youtube.com")

    # opening instagram
    elif "instagram" in a:
        print("opening instagram")
        webbrowser.open("instagram .com")

    # telling location
    elif "where i am" in a:
        webbrowser.open("maps.google.com")

    # searching in wikipedia
    elif "search in wikipedia" in a:
        query = input("what you want to search?")
        result = wikipedia.summary(query)
        print(result)































    else:
        print("sorry,please enter a valid command")
