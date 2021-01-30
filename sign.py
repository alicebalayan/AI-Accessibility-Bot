from movement import move, hand_movement
from selenium import webdriver

import pandas as pd

def main(): 
    driver = webdriver.Firefox()
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
    
    driver.execute_script(move.move_character(hand_movement.bring_forward(), 1500))
    driver.execute_script(move.move_character(hand_movement.close_right_thumb(), 1500))
    driver.execute_script(move.move_character(move.set_default_pose(), 1500))

if __name__ == "__main__":
    main()
