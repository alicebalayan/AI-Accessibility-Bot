from movement.hand_movement import bring_right_hand_forward
from pandas.core.frame import DataFrame
from selenium.webdriver.firefox.webdriver import WebDriver
from movement import move, hand_movement
from selenium import webdriver

import pandas as pd

driver = webdriver.Firefox()

def main(): 
    p = pd.read_csv("signdata.csv", encoding='ISO-8859-1')
    hello = p.loc[p["EntryID"] == "hello"] 
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

    
    # driver.execute_script(move.move_character([hand_movement.close_right_thumb()], 1500))
    while True:
        driver.execute_script(move.move_character([move.set_default_pose()], 1000))
        word = p.loc[p["EntryID"] == input()] 
        word_to_asl(word)
    # driver.execute_script(move.move_character(move.set_default_pose(), 1500))

def word_to_asl(word: DataFrame) -> None:
    begin, to = dict(), dict()
    if word["SignType.2.0"].item() == ("OneHanded"):
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
            raise Exception(f"IMPLEMENT {word['MinorLocation.2.0'].item()}")
        if not pd.isnull(word["SecondMinorLocation.2.0"].item()):
            if word["SecondMinorLocation.2.0"].item() in hand_movement.right_hand_location:
                values = hand_movement.right_hand_location[word["SecondMinorLocation.2.0"].item()]
                to.update({'rhx': values[0], 'rhy': values[1], 'rhz': values[2], 'rh': values[3]})
            else:
                raise Exception(f"IMPLEMENT {word['SecondMinorLocation.2.0'].item()}")
        
    if word["RepeatedMovement.2.0"].item() == 1:
        driver.execute_script(move.move_character([begin, to] * 3, 1000))
    else:
        driver.execute_script(move.move_character([begin, to], 1000))



if __name__ == "__main__":
    main()
