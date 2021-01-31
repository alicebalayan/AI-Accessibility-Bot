from movement.hand_movement import bring_right_hand_forward
from pandas.core.frame import DataFrame
from selenium.webdriver.firefox.webdriver import WebDriver
from movement import move, hand_movement
from selenium import webdriver
import time
# from data_points import *

import pandas as pd

driver = webdriver.Firefox()

threshold = 40


def startup(): 
    driver.get("http://aslfont.github.io/sign-puppet/demo/#forward")
    driver.execute_script("""
    var animator = puppet.getAnimator();
    //set up animation loop (in production use a requestAnimationFrame shim)
    setInterval(
    function () {
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
    animator.tween();
    //if omitted, 'channels' defaults to the animator object's channels
    puppet.draw(canvas, canvas.width, canvas.height, 0, 0);
    },
    100 // 10 frames per second
    );
    """)
    
    #driver.close() TODO add this at some point

def read_points(file_name: str):
    points = [[]]
    try:
        with open(file_name, 'r') as f:
            for line in f:
                (x, y) = line.split(',')
                x, y = int(x), int(y)
                if x < threshold and y < threshold:
                    points.append([])
                else:
                    points[-1].append((x, y))
    except FileNotFoundError as e:
        print("Put the file here")

    # Separate hands
    for i, clicks in enumerate(points):
        left, right = [], []
        finished_left = False
        for j, (x, y) in enumerate(clicks):
            if x > (400 - threshold) and y > (300 - threshold):
                finished_left = True
            else:
                if finished_left:
                    right.append((x,y))
                else:
                    left.append((x,y))
        if finished_left:
            points[i] = (left, right)
        else:
            points[i] = (left, )
    return points

# [] - list of tuples
#   - () - tuple of RH, LH
#       - [] list of coords
#            - () coords

p = pd.read_csv("signdata.csv", encoding='ISO-8859-1')

points = read_points("files/points.txt")
p["Positions"] = None
for i, k in enumerate(points):
    p["Positions"][100 + i] = k

def make_moves(words):
    # driver.execute_script(move.move_character([hand_movement.close_right_thumb()], 1500))
    

    for to_parse in words:
        driver.execute_script(move.move_character([move.set_default_pose()], 1000))
        # to_parse = input()
        
        # if len(word.index) > 0:
        #     word_to_asl(word)

        legal_words = p['EntryID'].tolist()

        if to_parse in legal_words:
            word = p.loc[p["EntryID"] == to_parse] 
            word_to_asl(word)
        else:
            fingerspell(to_parse)
        time.sleep(2)
    # driver.execute_script(move.move_character(move.set_default_pose(), 1500))


def word_to_asl(word: DataFrame) -> None:
    #TODO add LH positions
    print(word["EntryID"].item())
    if word["Positions"].item() == None:
        print("here")
        begin, to = dict(), dict()
        begin.update(hand_movement.bring_right_hand_forward())
        if word["ThumbPosition.2.0"].item() == "Closed":
            begin.update(hand_movement.close_right_thumb())
        for finger in "imrp":
            begin.update(hand_movement.curve_finger(finger, 'r')) 
        if word["Flexion.2.0"].item() == "FullyOpen":
            for finger in word["SelectedFingers.2.0"].item():
                begin.update(hand_movement.extend_finger(finger, 'r')) 
        if word["MinorLocation.2.0"].item() in hand_movement.right_hand_location:
            values = hand_movement.right_hand_location[word["MinorLocation.2.0"].item()]
            begin.update({'rhx': values[0], 'rhy': values[1], 'rhz': values[2], 'rh': values[3]})
        else:
            #raise Exception(f"IMPLEMENT {word['MinorLocation.2.0'].item()}")
            print("Unknown position")
        if not pd.isnull(word["SecondMinorLocation.2.0"].item()):
            if word["SecondMinorLocation.2.0"].item() in hand_movement.right_hand_location:
                values = hand_movement.right_hand_location[word["SecondMinorLocation.2.0"].item()]
                to.update({'rhx': values[0], 'rhy': values[1], 'rhz': values[2], 'rh': values[3]})
            else:
                #raise Exception(f"IMPLEMENT {word['SecondMinorLocation.2.0'].item()}")
                to.update({'rhx': -1, 'rhy': 2, 'rhz': 0, 'rh': 1})
                print("Unknown position")
        if word["RepeatedMovement.2.0"].item() == 1:
            driver.execute_script(move.move_character([begin, to] * 3, 1000))
        else:
            driver.execute_script(move.move_character([begin, to], 1000))
    else:
        positions = word["Positions"].item()
        locations = [dict()]*len(positions[0])

        #TODO add approximate shapes, such as "O" for "baby_o"
        rhand_shape = word["Handshape.2.0"].item()
        if str(rhand_shape).upper() in hand_movement.alphabet:
            locations[0].update(hand_movement.letter_animate('r', rhand_shape.upper()))
        else:
            locations[0].update(hand_movement.letter_animate('r', 'B'))
        
        lhand_shape = word["NonDominantHandshape.2.0"].item()
        if str(lhand_shape).upper() in hand_movement.alphabet:
            locations[0].update(hand_movement.letter_animate('r', lhand_shape.upper()))
        else:
            locations[0].update(hand_movement.letter_animate('l', 'B'))
        
        for i in range(len(positions[0])):
            rhposition = positions[0][i]
            locations[i].update({'rhx':(-1*(rhposition[0] - 187)/26.66), 'rhy':((rhposition[1]-133)/26.66), 'rhz': 0, 'rh': 1})
            if len(positions) > 1 and i < len(positions[1]):
                lhposition = positions[1][i]
                locations[i].update({'lhx':(1*(lhposition[0] - 187)/26.66), 'lhy':((lhposition[1]-133)/26.66), 'lhz': 0, 'lh': 1})
        
        time_interval = 1000/len(locations)

        #TODO ARIAN PLEASE MAKE THIS WORK THE RIGHT WAY
        driver.execute_script(move.move_character(locations, 1000))

def fingerspell(word):
    #TODO move hand to outstretched position
    print(word + " here")
    letters = [dict()]*(len(word))

    if word == "?":
        letters[0] = {'eby':2, 'ey':0.5}
    elif word == ".":
        letters[0] = {'eby':0, 'ey':0}
    elif word.isalpha():
        letters[0].update({'rh':1, 'rhx':0, 'rhy':2 })
        for i in range(len(word)):
            letters[i] = hand_movement.alphabet[word[i].upper()]
    
    driver.execute_script(move.move_character(letters, 500))
    

        
    


# ======================================================================================


# Read points


if __name__ == "__main__":
    startup()
