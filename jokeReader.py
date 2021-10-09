import json
import pyttsx3
import random
import keyboard

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 170)

f_reddit = open('reddit_jokes.json')
j_reddit = json.load(f_reddit)
f_stupidstuff = open('stupidstuff.json')
j_ss = json.load(f_stupidstuff)

while True:
    if keyboard.read_key() == "j":        
        flag = random.randint(0,5)
        if flag == 0:
            index = random.randint(0,len(j_ss)-1)
            while True:
                if(j_ss[index]["rating"]<3):
                    index = random.randint(0,len(j_reddit)-1)
                else:
                    break
            body = j_ss[index]["body"]
            engine.say(body)
            engine.runAndWait()
            if keyboard.is_pressed("esc"):
                engine.stop()
        else:
            index = random.randint(0,len(j_reddit)-1)
            while True:
                if(j_reddit[index]["score"]<3):
                    index = random.randint(0,len(j_reddit)-1)
                else:
                    break
            title = j_reddit[index]["title"]
            body = j_reddit[index]["body"]
            engine.say(title)
            engine.runAndWait()
            engine.say(body)
            engine.runAndWait()
            if keyboard.is_pressed("esc"):
                engine.stop()
            

