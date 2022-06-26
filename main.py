from time import *
import random

def errors(sentence,userinput):
    error_count=0
    for i in range(len(sentence)):
        try:
            if sentence[i]!=userinput[i]:
                error_count+=1
        except:
            error_count+=1
    return error_count
def speedtime(starttime,endtime,inputuser):
    timetaken=round(endtime-starttime,2)
    speedws=len(inputuser)/timetaken
    speed=round(speedws,2)
    return speed
words=["He returned home anxiously because he forgot the keys at home","Groom and wedding guests have reached the hall and the bride is not ready yet",

 "Her habit is to leave the door ajar whenever she leaves","She got her ankle sprained","Why do you get angry at every single matter?",
 "You found this house for us to live in","I do not know where family doctors acquired illegibly perplexing handwriting", 
 "nevertheless extraordinary pharmaceutical intellectuality counterbalancing", "indecipherability transcendentalizes intercommunication's", "incomprehensibleness"]
select=random.choice(words)
print(select)
time1=time()
inputu=input("Start typing ->Enter above sentence :")
time2=time()

print("Time taken :",round(time2-time1,2))
print("Speed :", speedtime(time1,time2,inputu),"w/s")
print("Errors :", errors(select,inputu))

            

