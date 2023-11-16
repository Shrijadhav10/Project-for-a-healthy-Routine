#healthy programing
from pygame import mixer
mixer.init()
from datetime import datetime
from time import time
print("TIME TABLE  SCHEDULE HEALTHY ROUTINE")
print("To make you healthy")
init_water=time()

init_eyes=time()
init_physical=time()
watersecs=15*60
eyesecs=30*60
physicalsecs=45*60
while True:
    
    if time()-init_water>watersecs:
        mixer.music.load("3water.mp3")
        print("music start playing..........")
        mixer.music.set_volume(0.8)
        mixer.music.play()
        with open("water.txt","a") as w:
            print("To stop music  you have to drink water 250ml and write ....DRANK....")
            while(True):  
                water_input=input()
                if(water_input.upper()=="DRANK"):
                    mixer.music.stop() 
                    water_time=datetime.now()
                    init_water=time()
                    water_drank_time=water_time.strftime("%H:%M:%S")
                    w.write(f" {water_input.upper()} time={water_drank_time} \n") 
                    break
    
    if time()-init_eyes>eyesecs:
        mixer.music.load("1eye.mp3")
        print("music start playing.......")
        mixer.music.set_volume(0.2)
        mixer.music.play()
        with open("eye.txt","a") as e:
            print("To stop music  you have to eye excercise  and afterthat write ....EYDONE....")
            while(True):   
                eye_input=input()
                if(eye_input.upper()=="EYDONE"):
                    mixer.music.stop()
                    local=datetime.now()
                    init_eyes=time()
                    local_time=local.strftime("%H:%M:%S")
                    e.write(f"{eye_input.upper()} time={local_time} \n ")
                    break
    
    if time()-init_physical>physicalsecs:
        mixer.music.load("2physical.mp3")
        mixer.music.set_volume(0.6)
        mixer.music.play()
        with open("physicalactivity.txt","a") as p:
            print("To stop music  you have to do physical  excercise  and afterthat write ....EXDONE....")
            while(True):   
                p_input=input()
                if(p_input.upper()=="EXDONE"):
                    mixer.music.stop()
                    local=datetime.now()
                    local_time=local.strftime("%H:%M:%S")
                    init_physical=time()
                    p.write(f"{p_input.upper()} time={local_time}\n")
                    break





