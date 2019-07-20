class WordSearch:

    board = []
    words = []
    answers = {}
    dims = 0

    def __init__(self, filename):
        self.extractPuzzleFromFile(filename)

    def extractPuzzleFromFile(self, filename):
        f = open(filename , "r")
        self.words = f.readline().strip().split(',')

        for line in f:
            self.board.append(list(line.strip().split(',')))
        f.close()
        self.dims = len(self.board)

    def solve_puzzle(self):
        for word in self.words:
            for y, row in enumerate(self.board):
                for x, col in enumerate(row):
                    self.find_word_north(word, y, x)

    def find_word_north(self, word, y, x):
        if(y == 0 ):
            return

        coordinates = []
        
        for i, char in enumerate(word):
            if(self.board[y - i][x] == char):
                coordinates.append([x, y - i])

        if len(coordinates) == len(word):
            self.answers[word] = coordinates
