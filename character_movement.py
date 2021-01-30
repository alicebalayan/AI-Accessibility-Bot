from typing import Dict


def close_thumb():
    """This closes thumb"""
    return {'rt0x': 1, 'rt0y': 1, 'rt1x': 1, 'rt1y': 1, 'rt2x': 1}

def move_character(instructions: Dict[str, float], time: int):
    return (f"""
    setTimeout(() => animator.setTarget({instructions}),
    {time}
    );
    """)

