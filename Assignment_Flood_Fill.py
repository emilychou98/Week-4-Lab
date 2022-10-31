from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    # Implement your code here.
    if input_board[x][y] == old:
        input_board[x] = f'{input_board[x][:y]}{new}{input_board[x][y+1:]}'
        if y > 0:
            input_board = flood_fill(input_board,old,new,x,y-1)
        if y < len(input_board[0]) - 1:
            input_board = flood_fill(input_board,old,new,x,y+1)
        if x > 0:
            input_board = flood_fill(input_board,old,new,x-1,y)
        if x < len(input_board) - 1:
            input_board = flood_fill(input_board,old,new,x+1,y)

    return input_board

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....