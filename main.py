# importing modules
import os
import smtplib
import webbrowser
import datetime
import wikipedia
import time

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

    # username
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
        time.sleep(1)
        webbrowser.open("www.google.com")

    # opening spotify to listen to music
    elif "listen music" in a:
        print("opening spotify...")
        time.sleep(1)
        webbrowser.open("www.spotify.com")

    # changing user name
    elif "change my name" in a:
        x = a.replace("change my name to ", "")
        f = open("name.txt", "w")
        f.write(x)
        f.close()
        print("Your new name is ", x)

    # changing assistant name
    elif "change your name" in a:
        x = a.replace("change your name to ", "")
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

    # search in  YouTube
    elif "search in youtube" in a:
        video = a.replace("search in youtube for", "")
        print("searching on youtube for ", video)
        time.sleep(1)
        webbrowser.open("https://www.youtube.com/results?search_query=" + video)

    # opening youtube
    elif "youtube" in a:
        print("opening youtube...")
        time.sleep(1)
        webbrowser.open("www.youtube.com")

    # opening instagram
    elif "instagram" in a:
        print("opening instagram")
        time.sleep(1)
        webbrowser.open("instagram .com")

    # telling location
    elif "where i am" in a:
        webbrowser.open("maps.google.com")

    # searching in wikipedia
    elif "search in wikipedia" in a:
        a = a.replace("search in wikipedia for", "")
        print(wikipedia.search(a, results=4))
        result = wikipedia.summary(a, sentences=1)
        print(result)

    # searching in google        
    elif "search in google" in a:
        a = a.replace("search is google for ", "")
        print("searching for ", a)
        time.sleep(1)
        webbrowser.open("https://www.google.com/search?q=" + a)

    # sending mail
    elif "send mail to" in a:
        reciever = a.replace("send mail to", "")
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        # Authentication
        s.login("sabiwaraich206@gmail.com", "sehbaz @@ singh")

        # message to be sent
        message = input("what you want to send?")

        # sending the mail
        s.sendmail("sabiwaraich206@gmail.com", reciever, message)

        s.quit()


