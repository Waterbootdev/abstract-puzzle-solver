from piece_keys import List, Dict, PIECE_KEYS

def piece_keys_counts(piece_keys: List[str]) -> Dict[str, int]:
    counts = {key: 0 for key in PIECE_KEYS}
    for piece_key in piece_keys:
        counts[piece_key]+=1
    return counts

if __name__ == '__main__':
    assert len(piece_keys_counts(PIECE_KEYS)) == len(PIECE_KEYS)
    assert set(piece_keys_counts(PIECE_KEYS).keys())==set(PIECE_KEYS)
    assert set(piece_keys_counts(PIECE_KEYS).values())=={1} 
    assert set(piece_keys_counts(PIECE_KEYS+PIECE_KEYS).values())=={2}
    