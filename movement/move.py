from typing import Dict

def move_character(instructions: Dict[str, float], time: int):
    return (
        f"""
        setTimeout(() => animator.setTarget({instructions}),
        {time}
        );
        """
    )

