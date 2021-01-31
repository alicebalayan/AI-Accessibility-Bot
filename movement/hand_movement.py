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
def letter_animate(hand, letter) -> Dict[str, float]:
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

        "F": {
            "ri0":  0.7, "ri1": 0.5, "ri2":  0.3, "ris":  0,                 #index
            "rm0":  0, "rm1":  0, "rm2":  0, "rms":  0,                      #middle
            "rr0":  0, "rr1":  0, "rr2":  0, "rrs":  0,                      #ring
            "rp0":  0, "rp1":  0, "rp2":  0, "rps":  0,                      #pinky
            "rt0x": -2, "rt0y": 1, "rt1x": 0, "rt1y": -3.4, "rt2x": 0,       #thumb
            "rrz": -100                                                      #rotate    
        },

        "G": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  -0.1,                   #index
            "rm0":  1, "rm1":  0.9, "rm2":  0.75, "rms":  -0.1,              #middle
            "rr0":  1, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,              #ring
            "rp0":  1, "rp1":  0.9, "rp2":  0.75, "rps":  -0.1,              #pinky
            "rt0x": 3, "rt0y": 0.6, "rt1x": 0, "rt1y": 0, "rt2x": 0,         #thumb
            "rrz": -10, "rrx":  5, "rry":  -80                               #rotate
        },

        "H": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  -0.1,                    #index
            "rm0":  0, "rm1":  0, "rm2":  0, "rms":  0,                       #middle
            "rr0":  1, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,               #ring
            "rp0":  1, "rp1":  0.8, "rp2":  0.75, "rps":  -0.1,               #pinky
            "rt0x": 4, "rt0y": 0.8, "rt1x": 0.75, "rt1y": 0, "rt2x": 0,       #thumb
            "rrz": 0, "rrx":  5, "rry":  80                                   #rotate
        },

        "I": {
            "ri0":  1, "ri1":  0.9, "ri2":  0.75, "ris":  -0.1,               #index
            "rm0":  1, "rm1":  0.9, "rm2":  0.75, "rms":  -0.1,               #middle
            "rr0":  1, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,               #ring
            "rp0":  0, "rp1":  0, "rp2":  0, "rps":  0.3,                     #pinky
            "rt0x": -0.75, "rt0y": 0.5, "rt1x": 0.3, "rt1y": 0.5, "rt2x": 0,  #thumb
        },

        "J": {
            "ri0":  1, "ri1":  0.9, "ri2":  0.75, "ris":  -0.1,               #index
            "rm0":  1, "rm1":  0.9, "rm2":  0.75, "rms":  -0.1,               #middle
            "rr0":  1, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,               #ring
            "rp0":  0, "rp1":  0, "rp2":  0, "rps":  0.3,                     #pinky
            "rt0x": -0.75, "rt0y": 0.5, "rt1x": 0.3, "rt1y": 0.5, "rt2x": 0,  #thumb
            "rrz": -10, "rrx":  60, "rry":  -80                                #rotate
        },

        "K": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  -0.1,                     #index
            "rm0":  1, "rm1":  0.9, "rm2":  0.75, "rms":  -0.1,                #middle
            "rr0":  1, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,                #ring
            "rp0":  1, "rp1":  0.9, "rp2":  0.75, "rps":  -0.1,                #pinky
            "rt0x": 3, "rt0y": 0.6, "rt1x": 0, "rt1y": 0, "rt2x": 0,           #thumb
        },

        "L": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  -0.2,                     #index
            "rm0":  1, "rm1":  0.9, "rm2":  0.75, "rms":  -0.1,                #middle
            "rr0":  1, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,                #ring
            "rp0":  1, "rp1":  0.9, "rp2":  0.75, "rps":  -0.1,                #pinky
            "rt0x": -1, "rt0y": 0, "rt1x": -1, "rt1y": 0, "rt2x": 0,           #thumb
        },

        "M": {
            "ri0":  0.9, "ri1":  0.8, "ri2":  0.75, "ris":  -0.1,              #index
            "rm0":  0.8, "rm1":  0.9, "rm2":  0.75, "rms":  -0.1,              #middle
            "rr0":  0.8, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,              #ring
            "rp0":  1.3, "rp1":  0.5, "rp2":  1, "rps":  -0.1,                 #pinky
            "rt0x": 0, "rt0y": 0.6, "rt1x": 0.7, "rt1y": -0.2, "rt2x": 0,      #thumb
            "rrz": -92, "rrx":  90, "rry":  0                                  #rotate
        },

        "N": {
            "ri0":  0.9, "ri1":  0.8, "ri2":  0.75, "ris":  -0.2,              #index
            "rm0":  0.8, "rm1":  0.9, "rm2":  0.75, "rms":  -0.4,              #middle
            "rr0":  1.3, "rr1":  1, "rr2":  1, "rrs":  -0.4,                   #ring
            "rp0":  1.3, "rp1":  1.2, "rp2":  1, "rps":  -0.2,                 #pinky
            "rt0x": 0.1, "rt0y": 0.7, "rt1x": 0.5, "rt1y": -0.2, "rt2x": 0,    #thumb
        },    

        "O": {
            "ri0":  0.8, "ri1":  0.4, "ri2":  0.4, "ris":  0,                  #index
            "rm0":  0.8, "rm1":  0.4, "rm2":  0.4, "rms":  0,                  #middle
            "rr0":  0.8, "rr1":  0.4, "rr2":  0.3, "rrs":  0,                  #ring
            "rp0":  0.8, "rp1":  0.4, "rp2":  0.2, "rps":  0,                  #pinky
            "rt0x": 1.7, "rt0y": 0.8, "rt1x": 0.5, "rt1y": 0.4, "rt2x": 0,     #thumb
            "rrz": -1                                                          #rotate
        },

        "P": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  0,                        #index
            "rm0":  0.5, "rm1":  0.6, "rm2":  0.1, "rms":  0.6,                #middle
            "rr0":  1.5, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,              #ring
            "rp0":  1.5, "rp1":  0.8, "rp2":  0.75, "rps":  -0.1,              #pinky
            "rt0x": -0.3, "rt0y": 0.7, "rt1x": 0.1, "rt1y": 0.3, "rt2x": 0,    #thumb
            "rrz": -60, "rrx":  0, "rry":  90                                  #rotate
        },

        "Q": {
            "ri0":  0.8, "ri1":  0.1, "ri2":  0, "ris":  0,                    #index
            "rm0":  1.5, "rm1":  0.9, "rm2": 0.75, "rms":  -0.1,               #middle
            "rr0":  1.5, "rr1":  0.9, "rr2":  0.75, "rrs":  -0.1,              #ring
            "rp0":  1.5, "rp1":  0.8, "rp2":  0.75, "rps":  -0.1,              #pinky
            "rt0x": -2, "rt0y": 1, "rt1x": 0, "rt1y": -3, "rt2x": 0,           #thumb
            "rrz": -70, "rrx": 5, "rry":  -90                                  #rotate
        },

        "R": {
            "ri0":  0, "ri1":  0, "ri2":  0.3, "ris":  -.5,                    #index
            "rm0":  0, "rm1":  0, "rm2":  -.6, "rms":  1.5,                    #middle
            "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                        #ring
            "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                        #pinky
            "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,    #thumb
            "rrz": -70, "rrx": 80, "rry": -40
        },

        "S": {
            "ri0":  1, "ri1":  1, "ri2":  1, "ris":  0,                        #index
            "rm0":  1, "rm1":  1, "rm2":  1, "rms":  0,                        #middle
            "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                        #ring
            "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                        #pinky
            "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": .2, "rt2x": -.4, #thumb
            "rrz": -70, "rrx": 80, "rry": -40
        },

        "T": {
            "ri0":  1, "ri1":  1, "ri2":  1, "ris":  0,                         #index
            "rm0":  1, "rm1":  1, "rm2":  1, "rms":  0,                         #middle
            "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
            "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
            "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": -.2, "rt2x": 0,   #thumb
            "rrz": -70, "rrx": 80, "rry": -40
        },

        "U": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  .5,                        #index
            "rm0":  0, "rm1":  0, "rm2":  0, "rms":  1.5,                       #middle
            "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
            "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
            "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
            "rrz": -70, "rrx": 80, "rry": -40
        },

        "V": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  .5,                        #index
            "rm0":  0, "rm1":  0, "rm2":  0, "rms":  0,                         #middle
            "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
            "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
            "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
            "rrz": -70, "rrx": 80, "rry": -40
        },

        "W": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  .5,                        #index
            "rm0":  0, "rm1":  0, "rm2":  0, "rms":  0,                         #middle
            "rr0":  0, "rr1":  0, "rr2":  0, "rrs":  1,                         #ring
            "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
            "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
            "rrz": -70, "rrx": 80, "rry": -40
        },

        "X": {
            "ri0":  0, "ri1":  .5, "ri2":  1, "ris":  0,                        #index
            "rm0":  1, "rm1":  1, "rm2":  1, "rms":  0,                         #middle
            "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
            "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
            "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
            "rrz": -70, "rrx": 60, "rry": -40                                   #rotate
        },

        "Y": {
            "ri0":  1, "ri1":  1, "ri2":  1, "ris":  0,                         #index
            "rm0":  1, "rm1":  1, "rm2":  1, "rms":  1,                         #middle
            "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  1,                         #ring
            "rp0":  0, "rp1":  0, "rp2":  0, "rps":  1,                         #pinky
            "rt0x": -1, "rt0y": 0, "rt1x": -1, "rt1y": 0, "rt2x": 0,            #thumb
            "rrz": -70, "rrx": 80, "rry": -30                                   #rotate
        },

        "Z": {
            "ri0":  0, "ri1":  0, "ri2":  0, "ris":  0,                         #index
            "rm0":  1, "rm1":  1, "rm2":  1, "rms":  0,                         #middle
            "rr0":  1, "rr1":  1, "rr2":  1, "rrs":  0,                         #ring
            "rp0":  1, "rp1":  1, "rp2":  1, "rps":  0,                         #pinky
            "rt0x": -0.75, "rt0y": 0.75, "rt1x": 0.6, "rt1y": 0, "rt2x": 0,     #thumb
            "rrz": -70, "rrx": 60, "rry": -30                                   #rotate
        }
    }

    if hand == "l":
        left = {}
        for r in alphabet[letter]:
            left["l" + r[1:]] = alphabet[letter][r]
        return left
    return alphabet[letter]