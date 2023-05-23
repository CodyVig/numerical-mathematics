"""
The trapped knight
"""


class TrappedKnight:
    def __init__(self, n: int, verbose: bool = False):
        """
        See https://www.youtube.com/watch?v=RGQe8waGJ4w and
        http://persson.berkeley.edu/math124/
        """

        self.board_root = n
        self.board_length = 2 * n + 1
        self.board_size = self.board_length**2
        self.board = self._initialize_board()
        if verbose:
            self._print_board()

    def simulate_walk(self) -> dict[str, list[int]]:
        """
        Simulates the trapped knight walk on a pre-initialized board and returns
        information about knight walk.

        :param board: a 2n+1 x 2n+1 integer array filled with spiral numbers
        :return: a dictionary whose values are:
        sequence:   integer array containing the sequence of spiral numbers
                    the knight jumped to during walk
        x_path:     integer array containing the x coordinates of each step
                    of knight walk
        y_path:     integer array containing the y coordinates of each step
                    of knight walk
        """

        x = self.board_root
        y = self.board_root

        sequence = [1]
        x_path = [x]
        y_path = [y]

        while True:
            # Get all potential locations.
            potential_scores = {
                self.board[y1][x1]: [x1, y1]
                for x1, y1 in self._list_moves(coords=[x, y])
            }
            # Now filter out the ones which we have already been to.
            new_keys = [
                keys for keys in potential_scores.keys() if keys not in sequence
            ]
            potential_scores = {k: potential_scores.get(k) for k in new_keys}
            if potential_scores == {}:
                return {
                    "sequence": sequence,
                    "x_path": x_path,
                    "y_path": y_path,
                }
            next_score = min(potential_scores.keys())
            x, y = potential_scores.get(next_score)
            sequence.append(next_score)
            x_path.append(x)
            y_path.append(y)

    def _print_board(self) -> None:
        """
        Prints the board `TrappedKnight.board()` to the console.
        """
        print()
        # Determine the length of the largest number
        max_length = max(
            len(str(self.board[0][0])),
            len(str(self.board[self.board_length - 1][0])),
            len(str(self.board[0][self.board_length - 1])),
            len(str(self.board[self.board_length - 1][self.board_length - 1])),
        )
        # Print the board and right-justfy the outputa
        for row in self.board:
            print(
                " ".join(
                    [
                        "{:>{max_length}}".format(
                            element, max_length=max_length
                        )
                        for element in row
                    ]
                )
            )
        print()

    def _initialize_board(self) -> list[list[int]]:
        """
        Initializes a chess board on a [-n:n]x[-n:n] domain with spiral numbers

        Example: initialize_board(2) returns
            17 16 15 14 13
            18  5  4  3 12
            19  6  1  2 11
            20  7  8  9 10
            21 22 23 24 25

        :return: a 2n+1 x 2n+1 integer array filled with spiral numbers
        """

        board = [[0] * self.board_length for _ in range(self.board_length)]

        xp, yp = 0, 0
        dx, dy = 1, 0
        depth = 1
        spiral = 0
        while spiral < self.board_size:
            for _ in range(depth):
                spiral += 1
                try:
                    board[yp + self.board_length // 2][
                        xp + self.board_length // 2
                    ] = spiral
                except IndexError:
                    break
                xp += dx
                yp += dy
            dx, dy = dy, dx
            if dy:
                dy = -dy
            else:
                depth += 1

        return board

    def _list_moves(self, coords: list[int]) -> list[list[int]]:
        """
        List all possible knight moves that leave the knight inside the board.

        :param coords: the inital [x, y] coordinates of the knight.
        :return: a list of all [x, y] coordinates accessible to the knight.
        """
        x, y = coords
        potential_moves = []

        for dx in range(1, 3):
            for dy in range(1, 3):
                if dx == dy:
                    continue
                for pmx in [-1, 1]:
                    for pmy in [-1, 1]:
                        x_new = x + pmx * dx
                        y_new = y + pmy * dy
                        if (x_new >= 0 and x_new < self.board_length) and (
                            y_new >= 0 and y_new < self.board_length
                        ):
                            potential_moves.append([x_new, y_new])

        return potential_moves


if __name__ == "__main__":
    tk = TrappedKnight(n=2, verbose=True)
    knight = tk.simulate_walk()
    for key in knight.keys():
        print(f"{key} : {knight.get(key)}")

    # # Uncomment the following to test for correct answer with n = 2.
    # sequence = knight.get("sequence")
    # x_path = knight.get("x_path")
    # y_path = knight.get("y_path")
    # x_path = [x - 2 for x in x_path]
    # y_path = [y - 2 for y in y_path]
    # print(sequence == [1, 10, 3, 6, 9, 4, 7, 2, 5, 8, 11, 14])
    # print(y_path == [0, 1, -1, 0, 1, -1, 1, 0, -1, 1, 0, -2])
    # print(x_path == [0, 2, 1, -1, 1, 0, -1, 1, -1, 0, 2, 1])

    # # Uncomment the following to see the full trapped knight solution.
    # tk = TrappedKnight(n=100, verbose=False)
    # knight = tk.simulate_walk()
    # print(
    #     "The last number in the trapped knight sequence is "
    #     + str(knight.get("sequence")[-1])
    # )
