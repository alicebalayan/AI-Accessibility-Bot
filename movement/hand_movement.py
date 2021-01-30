from typing import Dict

def close_right_thumb() -> Dict[str, float]:
    """This closes thumb"""
    return {'rt0x': 1, 'rt0y': 1, 'rt1x': -1, 'rt1y': 2, 'rt2x': 0}

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

