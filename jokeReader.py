import json
import pyttsx3
import random
import keyboard
import multiprocessing
import webbrowser

def tellJoke(joke):
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(joke)
    engine.runAndWait()
    



if __name__ == "__main__":
    f_reddit = open('reddit_jokes.json')
    j_reddit = json.load(f_reddit)
    f_stupidstuff = open('stupidstuff.json')
    j_ss = json.load(f_stupidstuff)
    print("\n\n********PRESS r TO SWITCH TO BROWSER MODE********")

    print("\n\t" + 27*"*" + "\n\t* - - - JOKE TELLER - - - *\n\t* - - - - - - - - - - - - *\n\t*      j FOR JOKE         *\n\t*      s TO SKIP JOKE     *\n\t*      ESC TO EXIT        *\n\t" + 27 * "*")
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
                joke = j_ss[index]["body"]
            else:
                index = random.randint(0,len(j_reddit)-1)
                while True:
                    if(j_reddit[index]["score"]<3):
                        index = random.randint(0,len(j_reddit)-1)
                    else:
                        break
                title = j_reddit[index]["title"]
                body = j_reddit[index]["body"]

                joke = title + ", , ," + body
            p = multiprocessing.Process(target=tellJoke, args=(joke,))
            p.start()
            while p.is_alive():
                if keyboard.is_pressed('s'):
                    p.terminate()
                elif keyboard.read_key() == "esc":
                    p.terminate()
                    exit()
                else:
                    continue  
        elif keyboard.read_key() == "esc":
            exit()
        elif keyboard.read_key() == "r":
            webbrowser.open_new("https://www.youtube.com/watch?v=wpV-gGA4PSk")
