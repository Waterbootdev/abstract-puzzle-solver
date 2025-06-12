from piece_key_constants import PIECE_KEY_BASE, PIECE_KEY_NUMBER_DIGITS, MAX_NUMBER_PIECE_KEYS, PIECE_KEY_DIGITS

def int_to_significant(value: int) -> str:
    if value < 0 or value >= MAX_NUMBER_PIECE_KEYS:
        raise ValueError()
    
    if value < PIECE_KEY_BASE:
        return str(value)
    
    digits: list[str] = []
    
    while value:
        digits.append(PIECE_KEY_DIGITS[value % PIECE_KEY_BASE])
        value //= PIECE_KEY_BASE

    return ''.join(reversed(digits))
    
def pad_zeros(significant: str) -> str:

    if len(significant) > PIECE_KEY_NUMBER_DIGITS:
        raise ValueError()
    
    return ''.join(['0']*(PIECE_KEY_NUMBER_DIGITS - len(significant))) + significant
    
if __name__ == '__main__':
    pass