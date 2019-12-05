##print ("Hello world")
#message = "This note will self-destruct in 5...4...3...2..1"
#print (message)
#message = "Boom!"
#print (message)
#dictionary = keyword and value
#print (4*5)
#print ("4"+"5")
#message = (29-105)
#print (message)
# yourdate = input("What is todays date")
#calc_date = (29-int(yourdate))

#if calc_date >= 1:
  #print ("Get excited - Thanksgiving is "+str(calc_date)+" days away")
  #if calc_date < -10:
    #print ("Hmm...I think you're messing with me")
#else: print("Yikes - Thanksgiving has passed") '''
import datetime
import random
d = datetime.datetime.today()
noun_list=[]
noun_target=5
verb_list=[]
verb_target=5
adjective_list=[]
adjective_target=5
cheers=['Sweet','Great','Superb','Magical']
yourname=input("Welcome - what's your name? ")
print("Let's begin the Madlib.")
noun_list.append(input("Let's have a noun: "))
while len(noun_list) < noun_target:
    noun_item = input( random.choice(cheers)+", let's have another noun: ")
    noun_list.append(noun_item)
if len(noun_list)== noun_target:
  print("Right, now we're on to verbs")

verb_list.append(input("Let's have a verb: "))
while len(verb_list) < verb_target:
    verb_item = input( random.choice(cheers)+", let's have another verb: ")
    verb_list.append(noun_item)
if len(verb_list)== verb_target:
  print("Lastly, the adjectives")

adjective_list.append(input("Let's have an adjective: "))
while len(adjective_list) < adjective_target:
    adjective_item = input( random.choice(cheers)+", let's have another adjective: ")
    adjective_list.append(adjective_item)
if len(adjective_list)== adjective_target:
  print("Okay, here comes your Madlib.")
  print("'To the tune of Jingle Bells':")
  print(random.choice(noun_list)+" through the "+random.choice(noun_list))
  print(", in a one-"+random.choice(noun_list)+" open "+random.choice(noun_list)) 
  print("O'er the "+random.choice(noun_list)+" we go "+random.choice(verb_list)+ ", all the way. ")
  print(random.choice(noun_list)+" on "+random.choice(noun_list)+"-tails"+random.choice(verb_list)+", making "+random.choice(noun_list)+ "s bright.") 
  print("What fun it is to "+random.choice(verb_list)+" and "+random.choice(verb_list)+" a "+random.choice(noun_list)+"ing song tonight!")
print ("This silly tune was written by "+yourname+" on "+str(d))


#shopList = [] 
#maxLengthList = 6
#while len(shopList) < maxLengthList:
    #item = input("Enter your Item to the List: ")
    #shopList.append(item)
#print ("That's your Shopping List")
#print (shopList)
#yourname = input("Let's begin with your name: ")
#noun = input("Now let's have a noun: ")
#proper-noun = input("")
#adjective = input("How about an adjective? ")
#verb = input("Gimme a verb in the past-tense! ")

#print ("There once was a "+noun+" from Valhalla, who "+verb+" with "+adjective+". This silly story was composed by "+yourname+ " on "+str(d))