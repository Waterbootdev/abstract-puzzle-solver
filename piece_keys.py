from piece_key_parts import int_to_significant, pad_zeros
from piece_key_constants import MAX_NUMBER_PIECE_KEYS
from typing import List, Dict, Set

PIECE_KEY_PARTS: List[str] = [int_to_significant(i) for i in range(MAX_NUMBER_PIECE_KEYS)]
PIECE_KEYS: List[str] = [pad_zeros(significant) for significant in PIECE_KEY_PARTS]

PIECE_KEYS_1: List[str] =[key[:1] for key in  PIECE_KEYS]
PIECE_KEYS_12: List[str] =[key[:2] for key in  PIECE_KEYS]
PIECE_KEYS_123: List[str] =[key[:3] for key in  PIECE_KEYS]

PIECE_KEYS_STARTS: Set[str] = set(PIECE_KEYS + PIECE_KEYS_1 + PIECE_KEYS_12 + PIECE_KEYS_123)

PIECE_KEYS_IDENTITY: Dict[str, str] = {key: key for key in PIECE_KEYS}

PIECE_KEY_TO_INDEX: Dict[str, str] = {key: f'{i:02}' for i, key in enumerate(PIECE_KEYS)}
INDEX_TO_PIECE_KEY: Dict[str, str] = {value: key for key, value in PIECE_KEY_TO_INDEX.items()}

PIECE_KEY_TO_INDEX_0: Dict[str, str] = {key: value[0] for key, value in PIECE_KEY_TO_INDEX.items()}
PIECE_KEY_TO_INDEX_1: Dict[str, str] = {key: value[1] for key, value in PIECE_KEY_TO_INDEX.items()}
PIECE_KEY_TO_BYTE: Dict[str, bytes] = {key: bytes([i])  for i, key in enumerate(PIECE_KEYS)}
BYTE_TO_PIECE_KEY: Dict[bytes, str] = {value: key for key, value in PIECE_KEY_TO_BYTE.items()}

if __name__ == '__main__':
    assert len(set(PIECE_KEYS)) == MAX_NUMBER_PIECE_KEYS
    assert len(PIECE_KEYS) == MAX_NUMBER_PIECE_KEYS

    print(PIECE_KEY_TO_BYTE)

