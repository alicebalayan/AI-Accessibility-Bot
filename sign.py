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

    word_to_asl(hello)
    
    driver.execute_script(move.move_character(hand_movement.bring_right_hand_forward(), 1500))
    driver.execute_script(move.move_character(hand_movement.close_right_thumb(), 1500))
    # driver.execute_script(move.move_character(move.set_default_pose(), 1500))

def word_to_asl(word: DataFrame) -> None:
    position = {}
    if word["SignType.2.0"].item() == ("OneHanded"):
        if word["ThumbPosition.2.0"].item() == "Closed":
            position.update(hand_movement.close_right_thumb())
        for finger in word["SelectedFingers.2.0"].item():
            position.update(hand_movement.extend_finger(finger, 'r'))

            
    driver.execute_script(move.move_character(position, 1500))
    



if __name__ == "__main__":
    main()
