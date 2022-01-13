import matplotlib.pyplot as plt
from pynput.keyboard import Key, Listener
from datetime import datetime as dt 


count = 0
keys = []
map = {}
timeToCharCount = {}
timeToWordCount = {}

def on_press(key):
    global keys, count, map 

    keys.append(key)
    count +=1


    writeFile(keys)
    keys = []
    count = 0

#---------------------------------------------------
def writeFile(keys):
    global map
    now = dt.now()
    currentTime = now.strftime("%I:%M %p")
    file = open("key_text.txt", "a")
    for key in keys:
        if key == Key.space:
            # when space is clicked a new line is made to the textfile
            file.write("\n")   
            # make a dictornary of time and words input    
            if currentTime not in map: 
                map[currentTime] = []
                map[currentTime].append("\n")
            else: 
                map[currentTime].append("\n")

        else: 
            stringKey = str(key).replace("'", "")
            if currentTime not in map:
                map[currentTime] = []
                map[currentTime].append(str(stringKey))
            else: 
                map[currentTime].append(str(stringKey))
            file.write(str(stringKey))

#----------------------------------------------------------

def on_release(key):
    global map, timeToWordCount, timeToCharCount
    if key == Key.esc:
       for i in map:
           timeToWordCount[i] = 0
           timeToCharCount[i] = 0
           for j in map[i]:
               if j == "\n": 
                   timeToWordCount[i]+=1
                   timeToCharCount[i]+=1
               else: timeToCharCount[i]+=1
       print(timeToCharCount)
       return False
#----------------------------------------------------------

def ploting():
    global map, timeToWordCount, timeToCharCount
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    
    for i in map:
        x1.append(str(i))
        y1.append(len(map[i]))
    # char count 
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, marker= "*")
    plt.title("Character Count")


    for i in timeToWordCount:
        x2.append(str(i))
        y2.append(timeToWordCount[i])
    # word count
    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, marker= "*")
    plt.title("Word Count")

    plt.show()
    
#---------------------------------------------------------------
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    ploting()
#---------------------------------------------------------------