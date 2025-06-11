from base_piece import List, Coordinate, Directions, BasePiece
from edge import Edge
from itertools import starmap
from collections.abc import Callable

from typing import TypeVar

Piece = TypeVar("Piece", bound=BasePiece)


def get_link(base_pieces: List[Piece], index: int|None) -> Piece|None:
        return base_pieces[index] if index else None

def link(base_pieces: List[Piece], piece : Piece, links: List[int|None], forward: int|None, backward: int|None):
        for i, index in enumerate(links):
            piece.links[i] = get_link(base_pieces, index)
        piece.forward = get_link(base_pieces, forward)
        piece.backward = get_link(base_pieces, backward)

def generate_linked_base_pieces(get_new_base_piece: Callable[[int, int, bool, List[Directions], Coordinate, List[Edge]], Piece] , frame_index: List[int], rotation_index: List[int], rotated: List[bool], directions: List[List[Directions]], coordinates: List[Coordinate], edges: List[List[Edge]], links: List[List[int|None]], forward: List[int|None], backward: List[int|None]) -> List[Piece]:
        base_pieces = list(starmap(get_new_base_piece, zip(frame_index, rotation_index, rotated, directions, coordinates, edges)))

        def link_(base_piece: Piece, links: List[int|None], forward: int|None, backward: int|None):
            link(base_pieces, base_piece, links, forward, backward)

        list(starmap(link_, zip(base_pieces, links, forward, backward)))
        return base_pieces
