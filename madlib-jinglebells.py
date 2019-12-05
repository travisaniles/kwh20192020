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
  print("Okay, here comes your Madlib. Be forewarned: it's about to get random!")
  print("'To the tune of Jingle Bells':")
  print(random.choice(noun_list)+" through the "+random.choice(noun_list))
  print(", in a one-"+random.choice(noun_list)+" open "+random.choice(noun_list)) 
  print("O'er the "+random.choice(noun_list)+" we go "+random.choice(verb_list)+ ", all the way. ")
  print(random.choice(noun_list)+" on "+random.choice(noun_list)+"-tails"+random.choice(verb_list)+", making "+random.choice(noun_list)+ "s bright.") 
  print("What fun it is to "+random.choice(verb_list)+" and "+random.choice(verb_list)+" a "+random.choice(noun_list)+"ing song tonight!")
print ("This silly tune was written by "+yourname+" on "+str(d))
