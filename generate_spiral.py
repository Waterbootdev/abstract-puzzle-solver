from spiral_helper import (
    Coordinate,
    Directions,
    Edge,
    List,
    Tuple,
    generate_backward,
    generate_coordinates_and_links,
    generate_directions,
    generate_edges,
    generate_forward,
    generate_frame_index,
    generate_rotated,
    generate_turns,
)


def generate_spiral(
    width: int, height: int
) -> Tuple[
    List[bool],
    List[int],
    List[int],
    List[List[Directions]],
    List[Coordinate],
    List[List[int | None]],
    List[int | None],
    List[int | None],
    List[int],
    List[List[Edge]],
]:
    if height > width or width < 2 or height < 2:
        raise Exception()

    rotated = generate_rotated(width, height)

    frame_index, rotation_index = generate_frame_index(rotated)

    directions = generate_directions(rotated)

    coordinates, links = generate_coordinates_and_links(
        width, height, rotated, directions
    )

    length = width * height

    forward = generate_forward(length)
    backward = generate_backward(length)

    turns = generate_turns(rotated)

    edges = generate_edges(length, turns)

    return (
        rotated,
        frame_index,
        rotation_index,
        directions,
        coordinates,
        links,
        forward,
        backward,
        turns,
        edges,
    )
