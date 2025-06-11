from piece_keys import PIECE_KEYS, PIECE_KEYS_IDENTITY, Dict, PIECE_KEYS_STARTS
from piece_key_constants import PIECE_KEY_BASE, PIECE_KEY_DIGITS


OPPOSITE_KEYS = [key for key in PIECE_KEYS_STARTS if len(key) == PIECE_KEY_BASE]

OPPOSITE_PIECE_KEY_DIGITS = {opposite_key: dict(zip(PIECE_KEY_DIGITS, opposite_key)) for opposite_key in OPPOSITE_KEYS}

OPPOSITE_PIECE_KEYS: Dict[str, Dict[str, str]] = {opposite_key: {key: PIECE_KEYS_IDENTITY[''.join([OPPOSITE_PIECE_KEY_DIGITS[opposite_key][digit] for digit in key])] for key in  PIECE_KEYS} for opposite_key in OPPOSITE_KEYS}

DEFAULT_OPPOSITE_KEY: str = '021' 

if __name__ == '__main__':
    assert DEFAULT_OPPOSITE_KEY in OPPOSITE_KEYS
    assert OPPOSITE_PIECE_KEY_DIGITS[DEFAULT_OPPOSITE_KEY] == {'0': '0', '1': '2', '2': '1'}

    