from game import *
from unittest import TestCase, main


class TestGameOperations(TestCase):
    def compare_boards_after_generation(self, expected_boards, result_boards):
        expected_boards_set = set(compact_board(b) for b in expected_boards)
        result_boards_set = set(compact_board(b) for b in result_boards)
        self.assertEqual(expected_boards_set, result_boards_set)

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
                [False, False, False, False, True,  True,  False],
                [False, False, False, False, False, False, False],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ], [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, True,  False, None,  None ],
                [False, False, False, True,  False, False, False],
                [False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ], [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
                [False, False, False, False, False, False, False],
                [False, True,  True,  False, False, False, False],
                [False, False, False, False, False, False, False],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ], [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
                [False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False],
                [False, False, False, True,  False, False, False],
                [None,  None,  False, True,  False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ],
        ]

        result_boards = generate_next_boards(board)
        self.compare_boards_after_generation(expected_boards, result_boards)

        board = [
            [None,  None,  True, True, True, None,  None ],
            [None,  None,  True, True, True, None,  None ],
            [True, True, True, True, True, True, True ],
            [True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True],
            [None,  None,  True, True, True, None,  None ],
            [None,  None,  True, True, True, None,  None ],
        ]
        result_boards = generate_next_boards(board)
        self.assertEqual(0, len(result_boards))

    def test_generate_next_states_from_border_is_correct(self):
        board = [
            [None,  None,  False, False, False, None,  None ],
            [None,  None,  False, False, False, None,  None ],
            [False, False, False, False, False, False, True ],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [None,  None,  False, False, False, None,  None ],
            [None,  None,  False, False, False, None,  None ],
        ]

        expected_boards = [
            [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
                [False, False, False, False, True,  True,  False],
                [False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ], [
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
                [False, False, False, False, False, False, False],
                [False, False, False, False, False, False, True ],
                [False, False, False, False, False, False, True ],
                [None,  None,  False, False, False, None,  None ],
                [None,  None,  False, False, False, None,  None ],
            ]
        ]

    def test_victory_check_is_correct(self):
        board = [
            [None,  None,  False, False, False, None,  None ],
            [None,  None,  False, False, False, None,  None ],
            [False, False, False, False, False, False, True ],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [None,  None,  False, False, False, None,  None ],
            [None,  None,  False, False, False, None,  None ],
        ]
        self.assertFalse(is_victory(board))

        board = [
            [None,  None,  True, True, True, None,  None ],
            [None,  None,  True, True, True, None,  None ],
            [True, True, True, True, True, True, True ],
            [True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True],
            [None,  None,  True, True, True, None,  None ],
            [None,  None,  True, True, True, None,  None ],
        ]
        self.assertTrue(is_victory(board))

    def test_can_play_game_properly(self):
        board = [
            [None,  None,  True, True, True, None,  None ],
            [None,  None,  True, True, True, None,  None ],
            [True, True, True, True, True, True, True ],
            [True, True, True, False, True, True, True],
            [True, True, True, False, True, True, True],
            [None,  None,  True, True, True, None,  None ],
            [None,  None,  True, True, True, None,  None ],
        ]
        result = play(board)
        self.assertFalse(result)

        board = [
            [None,  None,  True, True, True, None,  None ],
            [None,  None,  True, True, True, None,  None ],
            [True, True, True, True, True, True, True ],
            [True, True, True, False, True, True, True],
            [True, True, True, False, True, True, True],
            [None,  None,  True, False, True, None,  None ],
            [None,  None,  True, True, True, None,  None ],
        ]
        result = play(board)
        self.assertFalse(result)


if __name__ == '__main__':
    main()
