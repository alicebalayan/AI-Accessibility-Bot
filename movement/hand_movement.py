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


# Move hand forward first
alphabet = {

    "A": {
        "ri0":  1, "ri1":  0.9, "ri2":  0.75, "ris":  0.1,     #index
        "rm0":  1, "rm1":  0.9, "rm2":  0.75, "rms":  0.1,     #middle
        "rr0":  1, "rr1":  0.9, "rr2":  0.75, "rrs":  0.1,     #ring
        "rp0":  1, "rp1":  0.9, "rp2":  0.75, "rps":  0.1,     #pinky
        "rt0x": 3, "rt0y": 0, "rt1x": 0, "rt1y": 0, "rt2x": 0, #thumb
    },


    "B": {
        "ri0":  0, "ri1":  0, "ri2":  0, "ris":  0,                         #index
        "rm0":  0, "rm1":  0, "rm2":  0, "rms":  0,                         #middle
        "rr0":  0, "rr1":  0, "rr2":  0, "rrs":  0,                         #ring
        "rp0":  0, "rp1":  0, "rp2":  0, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.5, "rt1x": 0.5, "rt1y": 0.5, "rt2x": 0.25, #thumb
    },

    "C": {
        "ri0":  0, "ri1":  0.8, "ri2":  0, "ris":  0,            #index
        "rm0":  0, "rm1":  0.8, "rm2":  0, "rms":  0,            #middle
        "rr0":  0, "rr1":  0.8, "rr2":  0, "rrs":  0,            #ring
        "rp0":  0, "rp1":  0.8, "rp2":  0, "rps":  0,            #pinky
        "rt0x": -2, "rt0y": 1, "rt1x": 0, "rt1y": -3, "rt2x": 0, #thumb
        "rrz": -130                                              #rotate
    },

    "D": {
        "ri0":  0, "ri1":  0.8, "ri2":  0, "ris":  0,                        #index
        "rm0":  1, "rm1":  0.8, "rm2":  0, "rms":  0,                        #middle
        "rr0":  1, "rr1":  0.8, "rr2":  0, "rrs":  0,                        #ring
        "rp0":  1, "rp1":  0.8, "rp2":  0, "rps":  0,                        #pinky
        "rt0x": -0.75, "rt0y": 0.5, "rt1x": 0.75, "rt1y": 0.5, "rt2x": 0.25, #thumb
        "rrz": -110
    },

    "E": {
        "ri0":  0, "ri1":  1, "ri2":  1, "ris":  0,                         #index
        "rm0":  0, "rm1":  1, "rm2":  1, "rms":  0,                         #middle
        "rr0":  0, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
        "rp0":  0, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.5, "rt1x": 0.5, "rt1y": 0.2, "rt2x": 0.5, #thumb
        "rrz": -100
    },

     "R": {
        "ri0":  0, "ri1":  0, "ri2":  0.3, "ris":  -.5,                         #index
        "rm0":  0, "rm1":  0, "rm2":  -.6, "rms":  1.5,                         #middle
        "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
        "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
        "rrz": -70, "rrx": 80, "rry": -40
    },

    "S": {
        "ri0":  1, "ri1":  1, "ri2":  1, "ris":  0,                         #index
        "rm0":  1, "rm1":  1, "rm2":  1, "rms":  0,                         #middle
        "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
        "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": .2, "rt2x": -.4,     #thumb
        "rrz": -70, "rrx": 80, "rry": -40
    },

    "T": {
        "ri0":  1, "ri1":  1, "ri2":  1, "ris":  0,                         #index
        "rm0":  1, "rm1":  1, "rm2":  1, "rms":  0,                         #middle
        "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
        "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": -.2, "rt2x": 0,     #thumb
        "rrz": -70, "rrx": 80, "rry": -40
    },

    "U": {
        "ri0":  0, "ri1":  0, "ri2":  0, "ris":  .5,                         #index
        "rm0":  0, "rm1":  0, "rm2":  0, "rms":  1.5,                         #middle
        "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
        "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
        "rrz": -70, "rrx": 80, "rry": -40
    },

    "V": {
        "ri0":  0, "ri1":  0, "ri2":  0, "ris":  .5,                         #index
        "rm0":  0, "rm1":  0, "rm2":  0, "rms":  0,                         #middle
        "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
        "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
        "rrz": -70, "rrx": 80, "rry": -40
    },

    "W": {
        "ri0":  0, "ri1":  0, "ri2":  0, "ris":  .5,                         #index
        "rm0":  0, "rm1":  0, "rm2":  0, "rms":  0,                         #middle
        "rr0":  0, "rr1":  0, "rr2":  0, "rrs":  1,                         #ring
        "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
        "rrz": -70, "rrx": 80, "rry": -40
    },

    "X": {
        "ri0":  0, "ri1":  .5, "ri2":  1, "ris":  0,                         #index
        "rm0":  1, "rm1":  1, "rm2":  1, "rms":  0,                         #middle
        "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
        "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
        "rrz": -70, "rrx": 60, "rry": -40
    },

    "Y": {
        "ri0":  1, "ri1":  1, "ri2":  1, "ris":  0,                         #index
        "rm0":  1, "rm1":  1, "rm2":  1, "rms":  1,                         #middle
        "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  1,                         #ring
        "rp0":  0, "rp1":  0, "rp2":  0, "rps":  1,                         #pinky
        "rt0x": -1, "rt0y": 0, "rt1x": -1, "rt1y": 0, "rt2x": 0,            #thumb
        "rrz": -70, "rrx": 80, "rry": -30
    },

    "Z": {
        "ri0":  0, "ri1":  0, "ri2":  0, "ris":  0,                         #index
        "rm0":  1, "rm1":  1, "rm2":  1, "rms":  0,                         #middle
        "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
        "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
        "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0, #thumb
        "rrz": -70, "rrx": 60, "rry": -30
    }

}