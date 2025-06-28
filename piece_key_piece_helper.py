from piece_keys_helper import Dict, List, T, piece_key_groups_counts


def piece_key_groups_counts_sum(pieces: List[T]) -> Dict[str, int]:
    return {
        first_key: sum(keys.values())
        for first_key, keys in piece_key_groups_counts(pieces).items()
    }


def print_key_groups_counts(pieces: List[T]) -> Dict[str, Dict[str, int]]:
    print()
    counts = piece_key_groups_counts(pieces)
    for group in counts.values():
        f = dict(filter(lambda t: t[1] > 0, group.items()))
        count = sum(f.values())
        if count:
            print(f"{count}\t{f}")
    return counts
