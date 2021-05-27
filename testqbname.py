import random
from random import choices
from collections import Counter
import csv

def PPG(name_filename):
        #with open("names.csv", "r") as csv_file:

        with open(name_filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            first_name = []
            last_name = []
            rand_names = []
            next(csv_reader)
            
            for line in csv_reader:
                first_name.append(line[1])
                last_name.append(line[6])
                #print(line[1], line[6])
                
            #create height for players
            ##    if pos = QB
            ##        assign height range 5'11 to 6'6 with weights: 6 10 15 19 19 15 10 6
            fiveEleven = " 5" + "'" +"11 "
            sixFt = " 6"+ "' "
            sixOne = " 6"+ "'" + "1 "
            sixTwo = " 6"+ "'" + "2 "
            sixThree = " 6"+ "'" + "3 "
            sixFour = " 6"+ "'" + "4 "
            sixFive = " 6"+ "'" + "5 "
            sixSix = " 6"+ "'" + "6 "
            height = []
            
            for i in range(30):
                height.append(fiveEleven)
            for i in range(50):
                height.append(sixFt)
            for i in range(75):
                height.append(sixOne)
            for i in range(95):
                height.append(sixTwo)
            for i in range(95):
                height.append(sixThree)
            for i in range(75):
                height.append(sixFour)
            for i in range(50):
                height.append(sixFive)
            for i in range(30):
                height.append(sixSix)
##        #create weight for players
            weight = []
            for i in range(90):
                weight.append(random.randint(170,260))

            
##            if ht == fiveEleven: #weight bt 170- 205
##                weight = random.randint(170,205)
##            if height == sixFt: #170 - 210
##                weight = randint(170,210)
##            if height == sixOne: #175 & 220
##                weight = randint(175,220)
##            if height == sixTwo: #180-220
##                weight = randint(180,220)
##            if height == sixThree: #210-230
##                weight = randint(210,230)
##            if height == sixFour: #215-240
##                weight = randint(215,240)
##            if height == sixFive: #220-250
##                weight = randint(220,250)
##            if height == sixSix: #230-260
##                weight = randint(230,260)

        #create rating for players. QB has 2-5 5*, 5* total 35-45(3+-),4* total 300-350(20+/- per pos), 3* 600-700(45+- per pos), 2* 900-1200total(80+-)
            rating = []
            fiveStarQB = random.randint(0,5)
            fourStarQB = random.randint(15,20)
            threeStarQB = random.randint(40,50)
            twoStarQB = random.randint(75,85)
            #oneStarQB =  random.randint() all players without rating are 1* or "walkons"
            for i in range(fiveStarQB):
                rating.append(" 5* ")
            for i in range(fourStarQB):
                rating.append(" 4* ")
            for i in range(threeStarQB):
                rating.append(" 3* ")
            for i in range(twoStarQB):
                rating.append(" 2* ")
            oneStarQB = 300 - len(rating)
            for i in range(oneStarQB):
                rating.append(" 1* ")

            state = []
            for i in range(5):
                state.append("Alabama")
            state.append("Alaska")
            for i in range(6):
                state.append("Arizona")
            for i in range(3):
                state.append("Arkansas")
            for i in range(37):
                state.append("California")
            for i in range(5):
                state.append("Colorado")
            for i in range(4):
                state.append("Connecticut")
            state.append("Delaware")
            for i in range(19):
                state.append("Florida")
            for i in range(10):
                state.append("Georgia")
            state.append("Hawaii")
            for i in range(2):
                state.append("Idaho")
            for i in range(13):
                state.append("Illinois")
            for i in range(7):
                state.append("Indiana")
            for i in range(3):
                state.append("Iowa")
            for i in range(3):
                state.append("Kansas")
            for i in range(4):
                state.append("Kentucky")
            for i in range(5):
                state.append("Louisiana")
            state.append("Maine")
            for i in range(6):
                state.append("Maryland")
            for i in range(7):
                state.append("Massachusetts")
            for i in range(10):
                state.append("Michigan")
            for i in range(5):
                state.append("Minnesota")
            for i in range(3):
                state.append("Mississippi")
            for i in range(6):
                state.append("Misouri")
            state.append("Montana")
            for i in range(2):
                state.append("Nebraksa")
            for i in range(3):
                state.append("Nevada")
            state.append("New Hampshire")
            for i in range(9):
                state.append("New Jersey")
            for i in range(2):
                state.append("New Mexico")
            for i in range(19):
                state.append("New York")
            for i in range(10):
                state.append("North Carolina")
            state.append("North Dakota")
            for i in range(12):
                state.append("Ohio")
            for i in range(4):
                state.append("Oklahoma")
            for i in range(4):
                state.append("Oregon")
            for i in range(13):
                state.append("Pennsylvania")
            state.append("Rhoad Island")
            for i in range(5):
                state.append("South Carolina")
            state.append("South Dakota")
            for i in range(6):
                state.append("Tennessee")
            for i in range(25):
                state.append("Texas")
            for i in range(3):
                state.append("Utah")
            state.append("Vermont")
            for i in range(8):
                state.append("Virginia")
            for i in range(7):
                state.append("Washington")
            for i in range(2):
                state.append("West Virginia")
            for i in range(6):
                state.append("Wisconsin")
            state.append("Wyoming")
        #create complete player pool; about 300 per pos
            for i in range(10):
                rand_f = random.choice(first_name)
                rand_l = random.choice(last_name)
                full_names = rand_f + " " + rand_l
                
                #rand_names.append(:full_names)
                #rand_names.append(rand_l)
                ht = random.choice(height)
                rt = random.choice(rating)
                Wt = random.choice(weight)
                wt = str(Wt)
                st = random.choice(state)
                Dict_names = {"QB ":full_names + ht + wt + rt + st}
                
                rand_names.append(Dict_names)


                      
            print(Dict_names)
            print(rand_names)
            return rand_names
        #add state, with population, players are assigned w weights based off population. when done as fn use csv
        ###make a loop that adds states to a list the number of times representative to how often they will appear on a player(?)
##            states = {"Alabama":4779736, "Alaska":710231, "Arizona":6392017, "Arkansas":2915918, "California":37253956,"Colorado":5029196,"Connecticut":3574097,"Delaware":897934,
##                      "Florida":18801310, "Georgia":9687653, "Hawaii":1360301, "Idaho":1567582, "Illinois":12830632, "Indiana":6483802, "Iowa":3046355,"Kansas":2853118,
##                      "Kentucky":4339367, "Louisiana":4533372, "Maine":1328361, "Maryland":5773552, "Massachusetts":6547629, "Michigan":9883640, "Minnesota":5303925,
##                      "Mississippi":2967297, "Missouri":5988927, "Montana":989415, "Nebraska":1826341, "Nevada":2700551, "New Hampshire":1316470, "New Jersey":8791894,
##                      "New Mexico":2059179, "New York":19378102, "North Carolina":9535483, "North Dakota":672591, "Ohio":11536504, "Oklahoma":3751351, "Oregon":3831074,
##                      "Pennsylvania":12702379, "Rhode Island":1052567, "South Carolina":4625364, "South Dakota":814180,
##                      "Tennessee":6346105, "Texas":25145561, "Utah":2763885, "Vermont":625741, "Virginia":8001024, "Washington":6724540,
##                      "West Virginia":1852994, "Wisconsin":5686986, "Wyoming":563626
##                      }
##            tot_pop = sum(states.values())
##            pop_percent = states
##            for i in pop_percent:
##                tot_pop += pop_percent[i]
##            for i in pop_percent:
##                percent = pop_percent[i]/tot_pop
##                pop_percent[i] = percent
##            state = []
##            for i in pop_percent:
##                for i in range(pop_percent[i]):
##                    state.append(i)
##            print(state)

def TeamCreate(filename):
        with open(name_filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            first_name = []
            last_name = []
            rand_names = []
            next(csv_reader)
            
            for line in csv_reader:
                first_name.append(line[1])
                last_name.append(line[6])
                #print(line[1], line[6])
