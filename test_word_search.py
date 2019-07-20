import unittest

from word_search import WordSearch

class TestWordSearch(unittest.TestCase):

    def setUp(self):
        self.ws = WordSearch("test_puzzle.txt")

    def testIfPuzzleDataWasExtractedFromFile(self):
        expected_words = ["APE","ART","AIR","ANT","AXE","ACE","ALE","ARK"]
        expected_board = [['K','B','E','D','T'], \
                            ['F','R','P','R','G'], \
                            ['E','L','A','I','R'], \
                            ['H','C','X','N','J'], \
                            ['E','M','E','O','T']]

        self.assertListEqual(self.ws.words, expected_words)
        self.assertListEqual(self.ws.board, expected_board)

if __name__ == '__main__':
    unittest.main()