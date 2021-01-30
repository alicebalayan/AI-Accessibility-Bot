from typing import Dict

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
