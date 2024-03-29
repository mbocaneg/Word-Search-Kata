import unittest

from word_search import WordSearch

class TestWordSearch(unittest.TestCase):

    ws = WordSearch("test_puzzle.txt")
    ws.solve_puzzle()

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

    def testFindWordNorth(self):
        test_word = "APE"
        expected_output = [[2,2], [2,1], [2,0]]

        actual_output = self.ws.answers[test_word]
        self.assertListEqual(actual_output, expected_output)

    def testFindWordSouth(self):
        test_word = "AXE"
        expected_output = [[2,2], [2,3], [2,4]]

        actual_output = self.ws.answers[test_word]
        self.assertListEqual(actual_output, expected_output)

    def testFindWordEast(self):
        test_word = "AIR"
        expected_output = [[2,2], [3,2], [4,2]]

        actual_output = self.ws.answers[test_word]
        self.assertListEqual(actual_output, expected_output)

    def testFindWordWest(self):
        test_word = "ALE"
        expected_output = [[2,2], [1,2], [0,2]]

        actual_output = self.ws.answers[test_word]
        self.assertListEqual(actual_output, expected_output)

    def testFindWordNorthEast(self):
        test_word = "ART"
        expected_output = [[2,2], [3,1], [4,0]]

        actual_output = self.ws.answers[test_word]
        self.assertListEqual(actual_output, expected_output)

    def testFindWordSouthEast(self):
        test_word = "ANT"
        expected_output = [[2,2], [3,3], [4,4]]

        actual_output = self.ws.answers[test_word]
        self.assertListEqual(actual_output, expected_output)

    def testFindWordSouthWest(self):
        test_word = "ACE"
        expected_output = [[2,2], [1,3], [0,4]]

        actual_output = self.ws.answers[test_word]
        self.assertListEqual(actual_output, expected_output)

    def testFindWordNorthWest(self):
        test_word = "ARK"
        expected_output = [[2,2], [1,1], [0,0]]

        actual_output = self.ws.answers[test_word]
        self.assertListEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()