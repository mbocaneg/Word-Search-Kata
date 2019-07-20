import unittest

from word_search import WordSearch

class TestWordSearch(unittest.TestCase):

    ws = WordSearch("test_puzzle.txt")

    def testIfPuzzleDataWasExtractedFromFile(self):
        expected_words = ["APE","ART","AIR","ANT","AXE","ACE","ALE","ARK"]
        expected_board = [['K','B','E','D','T'], \
                            ['F','R','P','R','G'], \
                            ['E','L','A','I','R'], \
                            ['H','C','X','N','J'], \
                            ['E','M','E','O','T']]

        self.assertListEqual(self.ws.words, expected_words)
        self.assertListEqual(self.ws.board, expected_board)

    def testIfPuzzleBoardIsSquare(self):
        board_row_len = len(self.ws.board)
        board_col_len = len(self.ws.board[0])
        self.assertEqual(board_row_len, board_col_len)

if __name__ == '__main__':
    unittest.main()