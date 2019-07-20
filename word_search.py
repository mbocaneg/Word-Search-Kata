class WordSearch:

    board = []
    words = []
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
