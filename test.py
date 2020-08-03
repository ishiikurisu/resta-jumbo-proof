from game import *
from unittest import TestCase, main


class TestGameOperations(TestCase):
    def compare_boards_after_generation(self, expected_boards, result_boards):
        expected_boards_hash = [compact_board(b) for b in expected_boards]
        result_boards_hash = [compact_board(b) for b in result_boards]
        self.assertEqual(set(expected_boards), set(result_boards))

    def test_generating_next_states_is_correct(self):
        board = [
            [None,  None,  False, False, False, None,  None ],
            [None,  None,  False, False, False, None,  None ],
            [False, False, False, False, False, False, False],
            [False, False, False, True,  False, False, False],
            [False, False, False, False, False, False, False],
            [None,  None,  False, False, False, None,  None ],
            [None,  None,  False, False, False, None,  None ],
        ]

        expected_boards = [
            [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
                [False, False, False, False, False, False, False],
                [False, False, False, True,  False, False, False],
                [False, False, False, False, False, False, False],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ], [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
                [False, False, False, False, False, False, False],
                [False, False, False, True,  False, False, False],
                [False, False, False, False, False, False, False],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ], [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
                [False, False, False, False, False, False, False],
                [False, False, False, True,  False, False, False],
                [False, False, False, False, False, False, False],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ], [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
                [False, False, False, False, False, False, False],
                [False, False, False, True,  False, False, False],
                [False, False, False, False, False, False, False],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ],
        ]

        result_boards = generate_next_boards(board)
        self.compare_boards_after_generation(expected_boards, result_boards)


if __name__ == '__main__':
    main()
