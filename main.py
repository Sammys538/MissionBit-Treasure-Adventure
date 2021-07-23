from time import sleep
#print("TEST 1")
#sleep(2)
#print("TEST 2")
#sleep(1)
#print("Test 3")
#sleep(5)
#print("Last Test")

name = input("Before we start the adventure...\nWhat is your name?")


def intro(name):
  print("Welcome " + name + " to the start of the adventure.\nLet us begin...\n")
  sleep(2)
  print("Your name is " + name + ", and your passion is treasure hunting")
  sleep(2)
  print("You're at home one day when you receive a weird package and \ncome to find out that there is a treasure map inside")
  sleep(2)
  print("You look at the map to see that it leads to a mysterious island")
  sleep(2)
  print("There's also a message that reads be careful, may find danger\nand thieves")
  sleep(2)
  print("You think to yourself that couldn't be good, but you are confident that you can get it")
  sleep(2)
  print("You leave to the island with your supplies and with your captain\non board of a ship")
  sleep(2)
  print("You go to sleep, but suddenly wake up to find yourself and the ship\nin a storm")
  sleep(2)
  print("You see the huge waves coming, and the last thing you hear is the\ncaptain say \"Brace for impact!!!\"")


def island():
  sleep(2)
  print("\n... You wake up and find yourself in an island, but don't see any\nsign of the ship or the captain")
  sleep(3)
  print("You check your belongings and only find your map and a pocket knife")
  sleep(2)
  print("You believe this island may be the mysterious island on the map and\nsee that the treasure is in the middle of the island")
  sleep(3)
  print("You see that you have 2 paths to take right in front of you.")
  sleep(1)
  print("You check the map to find that both paths lead towards the treasure")
  sleep(1)
  print("You choose...(Print the number before the choice that you want\nto make)")
  sleep(1)
  print("\n" + "1.To go left")
  print("2.To go right")

# CHOICE 1
#answer1
def choice1():
  print("You choose to go left. You are determined to find treasure and\nquickly run in the direction of the path")
  sleep(2)
  print("After some time, you stumble across an abondoned building. You\nwonder why in the world there would be an abandoned building in\na mysterious island")
  sleep(2)
  print("You decide to check your map and see that the building isn't on the\nmap")
  sleep(1)
  print("You decide...")
  sleep(1)
  print("\n1.To investigate the building and go inside")
  print("2.To leave the building altogether")

#answer2
def path1Outcome1():
  print("\nYou decide to investigate the building and go inside")
  sleep(2)
  print("You find yourself in a big dark room")
  sleep(1)
  print("You suddenly hear the door slam shut and realize that there's no\nother way out")
  sleep(2)
  print("You try your hardest to open the door but it doesn't seem to do anything")
  sleep(1)
  print("You realize that you're stuck and can't do anything about it")
  sleep(1)
  print("GAME OVER")
  

#answer2
def path1Outcome2():
  print("\nYou decide to leave the building altogether")
  sleep(1)
  print("You stumble across a camp and find a lot of armed mean looking\npeople")
  sleep(2)
  print("You see that there is treasure in the middle of the camp")
  sleep(2)
  print("You also see that they have a pen full of animals(Which could be\nuseful)")
  sleep(3)
  print("You decide to...")
  sleep(1)
  print("\n1.Sneak into the camp and steal the treasure quietly")
  print("2.Create a distraction and wait until everyone is gone to go for it")

#answer4
def path1Outcome3():
  print("\nYou try to sneak into the camp and steal the treasure quickly")
  sleep(2)
  print("You slowly come up on the tent without any worry in the world as no\none has seen you yet")
  sleep(2)
  print("However, you get close to the treasure when you are suddenly\nspotted")
  sleep(2)
  print("You realize that you can't do anything as its only you and there's\na bunch of them")
  sleep(2)
  print("You get captured")
  sleep(2)
  print("GAME OVER")

#answer4
def path1Outcome4():
  print("\nYou decide to create a distraction and wait until everyone is gone")
  sleep(2)
  print("You decide to free the animals and see that many of the armed\npeople are going after them")
  sleep(2)
  print("You check the camp and realize that everyone left for the animals")
  sleep(2)
  print("You grab the treasure and make a run for it")
  sleep(2)
  print("You run for a while and suddenly get jolted up in the air")
  sleep(2)
  print("Your pocket knife falls on the ground")
  sleep(.5)
  print("After a while, the same armed people come by and take back the\ntreasure")
  sleep(2)
  print("They decide to throw you off a hill and you get knocked out")
  sleep(2)
  print("\nAfter some time, you wake up to see yourself in an abandoned\ncampsite")
  sleep(2)
  print("You start regretting even coming here and start regretting being a treasure hunter anymore")
  sleep(2)
  print("You start reflecting on your choices and how it was so dumb to\nbecome a treasure hunter")
  sleep(2)
  print("You've always liked it but think that many might make fun of you\nfor coming back with nothing")
  sleep(2)
  print("(Creator here, while some people feel like giving up on a passion\nthey have whenever they fail, you have to remember that it's\nbetter to fail as you learn from those mistakse and from\nthose experiences")
  sleep(3)
  print("You're never alone in that you failed. Everyone fails. Even I\nfailed while writing some of this code. But we don't give up.\nThe point is, follow your passions, and even if you fail,\nremember that the way you get back up is what makes you better)")
  sleep(3)
  print("You decide...")
  sleep(1)
  print("\n1.To try one more time and go after the treasure")
  print("2.To go home and try to find a boat to leave the island")

def tryAgain():
  print("\n:)")
  sleep(.5)
  print("You follow your heart and passion and decide to go after the\ntreasure one more time")
  sleep(2)
  print("You decide to head back up towards the camp and see that the armed people are still dealing with the animals")
  sleep(2)
  print("You see the treasure and decide to make a run for it")
  sleep(1)
  print("Your able to get the treasure and get out on time before anyone\nspots you")
  sleep(1)
  print("You check the map and find a dock area and are able to find a boat")
  sleep(1)
  print("You joyfully sail away with the treasure at hand and even more\nself-confident about your passion as before")
  sleep(2)
  print("\nYou got the \"GOOD ENDING\"")

def goHome():
  print("\n...")
  sleep(2)
  print("Well...remember, follow your passion and don't give up on your\ndreams. We all fail in life, but it's the way we come back\nthat counts")
  sleep(3)
  print("You look at your map and see that there's a dock nearby")
  sleep(1)
  print("You go to the docks to find it empty except for one small boat")
  sleep(2)
  print("You hop on board and slowly sail away")
  sleep(1)
  print("\nYou got the \"BAD ENDING\"")







#CHOICE 1

#CHOICE 2
#answer1
def choice2():
  print("You choose to go the right. You are determined to find treasure and\nquickly run in the direction of the path")
  sleep(2)
  print("You walk for some time when you notice something weird")
  sleep(1)
  print("You see weird piles of leaves on the path")
  sleep(1)
  print("You choose...")
  sleep(.5)
  print("\n1.To ignore the leaves altogether and walk on them(Basically\nignoring what was just said)")
  print("2.To walk past them while being careful not to touch them")

#answer3
def path2Outcome1():
  print("\n...OK")
  sleep(.5)
  print("You walk through the path without caring for the leaves")
  sleep(1)
  print("Your foot gets stuck on one of the leaves and you get pulled up\nfrom the ground upside down")
  sleep(2)
  print("You're stuck and try to free yourself")
  sleep(1)
  print("You decide to...")
  sleep(.5)
  print("\n1.Use your knife to cut down the net")
  print("2.Try to free yourself with your bare hands")


def path2NetScene1():
  print("You decide to use your knife to cut down the net")
  sleep(1)
  print("The net breaks enough for you to be free")
  sleep(.5)
  print("You run away onto a path before anyone sees you")
  sleep(1)
  print("You manage to get to a safe spot and look at your map")
  sleep(1)
  print("You see that there is a treasure ship not far from where you are")
  sleep(1)
  print("You decide to go to the ship as fast as you can in order to get to the treasure")
  sleep(2)
  print("You get to the ship and see that there is no one around")
  sleep(1)
  print("From a distance, you can see the armed people coming to the ship so\nyou have to hurry")
  sleep(2)
  print("You realize you can only check one place before the armed people\nget to the ship")
  sleep(2)
  print("You decide to check...")
  sleep(.5)
  print("\n1.The Captain's Cabin")
  print("2.The storage room")


def path2CaptainCabin():
  print("You decide to check the Captain's Cabin and manage to find some\ninteresting stuff such as a map of the surrounding island and\nthe other islands")
  sleep(3)
  print("You manage to find the treasure and manage to escape, however, the armed people are able to spot you")
  sleep(2)
  print("You quickly check the map and find the docks")
  sleep(1)
  print("You find a boat and quickly make your escape with the treasure")
  sleep(1)
  print("\nYou got the \"Escaped\" ending")

def path2StorageRoom():
  print("You decide to check the storage room")
  sleep(1)
  print("You look carefully in the room but are only able to find cleaning supplies, and weapons")
  sleep(2)
  print("You realize that you probably should of checked the Captain's Cabin")
  sleep(2)
  print("You quickly try to reach it to look for the treasure, but aren't able to as you see that you are quickly being surrounded by the armed people")
  sleep(2)
  print("You realize that there's nothing you can do as they have strength in numbers")
  sleep(2)
  print("GAME OVER")

def path2NetScene2():
  print("You try your hardest with your hands to set yourself free")
  sleep(2)
  print("You aren't able to free yourself and realize that there's nothing\nyou can do")
  sleep(2)
  print("Game Over")

#answer3
def path2Outcome2():
  print("You carefully walk through the path and slowly come up on a temple ")
  sleep(2)
  print("You check your map and see that the treasure is inside the temple")
  sleep(1)
  print("You head into the temple and try to look out for traps")
  sleep(1)
  print("You get inside and find it really dark with only dim lights")
  sleep(1)
  print("You manage to find two doors, however, you're able to see letters\non each door")
  sleep(1)
  print("After sometime, you're able to see that door on the right has\nthe letters \"rpcyqspc\", and the door on the left has the\nletters \"rpyn\"")
  sleep(3)
  print("You also find a sign in between the doors with the phrase,\n\"SHIFT: 24\"")
  sleep(2)
  print("(Creator here, You got this, remember to try to think of ways on\nhow to solve this")
  sleep(2)
  print("You're given a shift, which means you might have been given\na cypher")
  sleep(1)
  print("You're smart enough to figure this out, just think of how you\nmay solve this")
  sleep(2)
  print("DON'T GIVE UP)")
  sleep(1)
  print("You decide to...")
  sleep(.5)
  print("\n1.Go to the door on the right")
  print("2.Go to the door on the left")

def pathTreasure():
  print("You go to the door on the right and figure out that the puzzle uses\na Ceaser Cipher, and are able to find that it reads \"Treasure\"")
  sleep(3)
  print("You find a ton of treasure and quickly leads to your pockets and\nbackpack getting full")
  sleep(2)
  print("You quickly get out of the temple and head to the towards the water")
  sleep(1)
  print("Luckily, you are able to find a boat and happily enjoy your\ntreasure while on the way home")
  sleep(1)
  print("\nYou got the \"Cypher Ending\"")


def pathTrap():
  print("You go to the door on the left without any idea on what's going on")
  sleep(2)
  print("You think you might have picked the right door, but upon entering\nthe room, you realize you step on something and suddenly, the\ndoor behind you closes")
  sleep(3)
  print("You try to open the door, but it doesn't budge")
  sleep(1)
  print("You start to panick and reflect on how you probably shouldn't have taken a guess")
  sleep(1)
  print("GAME OVER")


#CHOICE 2

#Path 1 Split 1
def pathSplit2():
  while True:
    answer2 = input("Enter a number: ")
    answer2 = int(answer2)
    if answer2 == 1:
      path1Outcome1()
      break
    elif answer2 == 2:
      path1Outcome2()
      pathSplit4()
      break
    else:
      print("Please input a number with a choice")

#Path 1 Split 2
def pathSplit4():
  while True:
    answer4 = input("Enter a number: ")
    answer4 = int(answer4)
    if answer4 == 1:
      path1Outcome3()
      break
    elif answer4 == 2:
      path1Outcome4()
      pathSplit6()
      break
    else:
      print("Please input a number with a choice")

#Path 1 Split 3
def pathSplit6():
  while True:
    answer6 = input("Enter a number: ")
    answer6 = int(answer6)
    if answer6 == 1:
      tryAgain()
      break
    elif answer6 == 2:
      goHome()
      break
    else:
      print("You stand there...")
      sleep(1)
      print("All of a sudden you look up to see a plane flying and you manage to spot the phrase \"Hog Wild\"")
      sleep(2)
      print("You think they might be going on an Uncharted adventure...")
      sleep(2)
      print("Please input a number with a choice")


#Path 2 ESCAPE ENDING/GAME OVER

def pathSplit8():
  while True:
    answer8 = input("Enter a number: ")
    answer8 = int(answer8)
    if answer8 == 1:
      pathTreasure()
      break
    elif answer8 == 2:
      pathTrap()
      break
    else:
      print("Please input a number with a choice")


def pathSplit7():
  while True:
    answer7 = input("Enter a number: ")
    answer7 = int(answer7)
    if answer7 == 1:
      path2CaptainCabin()
      break
    elif answer7 == 2:
      path2StorageRoom()
      break
    else:
      print("Please input a number with a choice")

#Path 2 Split 2
def pathSplit5():
  while True:
    answer5 = input("Enter a number: ")
    answer5 = int(answer5)
    if answer5 == 1:
      path2NetScene1()
      pathSplit7()
      break
    elif answer5 == 2:
      path2NetScene2()
      break
    else:
      print("Please input a number with a choice")

#Path 2 Split 1
def pathSplit3():
  while True:
    answer3 = input("Enter a number: ")
    answer3 = int(answer3)
    if answer3 == 1:
      path2Outcome1()
      pathSplit5()
      break
    elif answer3 == 2:
      path2Outcome2()
      pathSplit8()
      break
    else:
      print("Please input a number with a choice")



#MAIN PATH
def pathSplit1():
  while True:
    answer1 = input("Enter a number: ")
    answer1 = int(answer1)
    if answer1 == 1:
      choice1()
      pathSplit2()
      break
    elif answer1 == 2:
      choice2()
      pathSplit3()
      break
    else:
      print("Please input a valid choice")

intro(name)
island()
pathSplit1()
