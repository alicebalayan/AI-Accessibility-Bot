from typing import Dict

right_hand_location = {
    "Forehead": [0,-2,0,3],
    "Mouth": [0,0,0,3],
    "Chin": [-.5,.8,-2,2],
    "Clavicle": [.5,0,-3,1],
    "HeadAway": [2,-1,2,3],
    "Eye": [-.8,-3,-1,1],
    "Neutral":[1,-2,0,1],
    "Other": [0,0,0,3],
    "UnderChin": [-.5,.8,-2,2],
    "CheekNose": [0,-1,-3,1],
    "TorsoTop": [0,1,-3,1],
    "HandAway": [-4,-1,1,1],
    "FingerDown": [-2,2,0,1],
    "TorsoMid": [0,3,-3,1],
    "Waist": [1,5,-3,1],
    "ForearmUlnar": [-3,2,-2,1],
    "Hips": [2,6,-3,1]
}

def close_right_thumb() -> Dict[str, float]:
    """This closes thumb"""
    return {'rt0x': -0.75, 'rt0y': 0.5, 'rt1x': 0.5, 'rt1y': 0.5, 'rt2x': 0.25}

def bring_forward() -> Dict[str, float]:
    """???"""
    return {
        'rby'  : 0,
        'rbz'  : 1,
        'rrz'  : -90,
        'rrx'  : 90,
        'lby'  : 0,
        'lbz'  : 1,
        'lrz'  : -90,
        'lrx'  : 90,
        'e0y'  : 1,
        'e1y'  : 1,
        'ez'  : 1
    }

def curve_finger(finger, hand):
    return {
        f"{hand}{finger}{i}": j
        for i,j in [
                ('0', 1),
                ('1', 0.9),
                ('2', 0.75),
                ('s', -0.1)
        ]
    }

def extend_finger(finger, hand):
    return {
        f"{hand}{finger}{i}": j
        for i,j in [
                ('0', 0),
                ('1', 0),
                ('2', 0),
                ('s', 0)
        ]
    }


def bring_right_hand_forward() -> Dict[str, float]:
    return {
        'rby'  : 0,
        'rbz'  : 1,
        'rrz'  : -90,
        'rrx'  : 90,
    }

