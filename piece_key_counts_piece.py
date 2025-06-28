from array import array
from typing import Dict, List, Self, Tuple

from base_piece import BasePiece, Coordinate, Directions
from edge import LEFT_UP_RIGHT_DOWN, OPPOSITE_EDGE, Edge
from insert_nodes import InsertNode, InsertNodes
from opposite_piece_keys import OPPOSITE_PIECE_KEYS
from piece_key_constants import ASTERISK, ASTERISK_PIECE_KEY
from piece_key_count import PieceKeyCount
from rotation_matrix import INDEX_ROTATION_MATRIX


class PieceKeyCountsPiece(BasePiece):
    def __init__(
        self,
        piece_key_counts: Dict[str, Dict[str, List[PieceKeyCount]]],
        opposite_key: str,
        frame_index: int,
        rotation_index: int,
        rotated: bool,
        directions: List[Directions],
        coordinate: Coordinate,
        edges: List[Edge],
    ) -> None:
        super().__init__(
            frame_index, rotation_index, rotated, directions, coordinate, edges
        )
        self.opposite_piece_keys = OPPOSITE_PIECE_KEYS[opposite_key]
        self.piece_key = ASTERISK_PIECE_KEY
        self.opposite_piece_key = ASTERISK_PIECE_KEY
        rotation_matrix = INDEX_ROTATION_MATRIX[rotation_index]
        self.rotation_matrix = rotation_matrix
        self.rotation = rotation_matrix[0]
        self.piece_key_counts = piece_key_counts[str(self.edges)]
        self.asterisk_piece_key_list: List[str] = list(ASTERISK_PIECE_KEY)
        self.pre_trie_index = 0
        self.down_keys: array[int]
        self.pieces: List[PieceKeyCountsPiece]
        self.root: InsertNodes

    def __repr__(self) -> str:
        return self.rotated_piece_key()

    def pre_insert_nodes(self) -> None:
        for i, piece in enumerate(self.pieces):
            self.down_keys[i] = piece.part(Edge.DOWN)
        self.pre_trie_index = self.root.pre_insert(self.down_keys)

    def insert_node(self) -> Tuple[bool, InsertNode]:
        if self.rotated:
            return self.root.insert_last_digit(
                self.pre_trie_index, self.part(Edge.DOWN)
            )
        else:
            return self.root.insert_last_digit(
                self.root.insert_digit(self.pre_trie_index, self.part(Edge.DOWN)),
                self.part(Edge.RIGHT),
            )

    def part(self, edge: Edge) -> int:
        return int(self.piece_key[edge])

    def rotated_piece_key(self) -> str:
        return "".join([self.piece_key[i] for i in self.rotation])

    def get_opposite_key_part(self, rotation_index: int, edge: Edge) -> str:
        return self.opposite_piece_key[
            self.rotation_matrix[rotation_index][OPPOSITE_EDGE[edge]]
        ]

    def set_piece_key(self, piece_key: str) -> None:
        self.piece_key = piece_key
        self.opposite_piece_key = self.opposite_piece_keys[piece_key]

    def oppsites_opposite_key_part(self, opposite_pice: Self | None, edge: Edge) -> str:
        if opposite_pice:
            return opposite_pice.get_opposite_key_part(self.rotation_index, edge)
        else:
            raise Exception()

    def check(self) -> bool:
        asterisk_piece_key_list: List[str] = list(ASTERISK_PIECE_KEY)

        for edge in LEFT_UP_RIGHT_DOWN:
            asterisk_piece_key_list[edge] = self.oppsites_opposite_key_part(
                self.links[edge], edge
            )

        return "".join(asterisk_piece_key_list) == self.piece_key

    def asterisk_piece_key(self) -> str:
        self.asterisk_piece_key_list = list(ASTERISK_PIECE_KEY)

        for edge in self.edges:
            self.asterisk_piece_key_list[edge] = self.oppsites_opposite_key_part(
                self.links[edge], edge
            )

        asterisk_piece_key = "".join(self.asterisk_piece_key_list)

        for edge in self.edges:
            self.asterisk_piece_key_list[edge] = ASTERISK

        return asterisk_piece_key

    def current_piece_key_counts(self) -> List[PieceKeyCount]:
        return self.piece_key_counts[self.asterisk_piece_key()]
