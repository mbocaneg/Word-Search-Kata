class WordSearch:
    """
    A class used to represent the state of a WordSearch puzzle

    ...

    Attributes
    ----------
    board: list of list of char
        List of lists that represents the 2D board
    words: list of str
        List of strings that holds the words we wish to find
    answers: dict of (str, list of list of int)
        answers to desired words. maps a word to a list of x,y coordinates
        that represents the position of the words characters within the board
    dims: int
        dimensions of puzzle. since we assume puzzle to be square, dims = l = w
    directions: list of int
        representation of the y cardinal directions using x and y offsets. directions
        are represented as follows:
        [-1,  0] NORTH
        [-1,  1] NORTHEAST
        [ 0,  1] EAST
        [ 1,  1] SOUTHEAST
        [ 1,  0] SOUTH
        [ 1, -1] SOUTHWEST
        [ 0, -1] WEST
        [-1. -1] NORTHWEST
    """

    board = []
    words = []
    answers = {}
    dims = 0
    directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


    def __init__(self, filename):
        """
        Parameters
        ----------
        filename: str
            filename of the text file that contains the puzzle we wish to load
        """
        self.extractPuzzleFromFile(filename)

    # function that parses puzzle text file and extracts the puzzle's words,
    # 2d board, and board dimensions
    def extractPuzzleFromFile(self, filename):
        """Extracts puzzle metadata from a text file and loads corresponding class members

        Parameters
        ----------
        filename: str
            filename of the text file that contains the puzzle whose data we wish to extract
        
        """

        # open file
        f = open(filename , "r")

        # look at first line of file, which is to contain the words. Strip it
        # of whitespace, and split it according to ',' character. Store output
        # into 'words' list
        self.words = f.readline().strip().split(',')

        # ...then look at the rest of the lines in the file, which contains the entire 2d board.
        # again, strip each line of whitespace, split according to ',' and store resulting list
        # into 'board', which is a list of lists
        for line in f:
            self.board.append(list(line.strip().split(',')))
        
        # close the file, and extract dimensions of the board by taking the length of
        # the board list(since we assume board to be square, both length and width are equal)
        f.close()
        self.dims = len(self.board)


    def solve_puzzle(self):
        """Function that attempts to solve find words horizontally and vertically 
        within the 2D board

        """

        # for each word in the words list
        # ...for each row in the game board
        # ......for each column in each row
        for word in self.words:
            for y, row in enumerate(self.board):
                for x, col in enumerate(row):
                    
                    # for each direction
                    # try to find a word in said direction
                    for dir in self.directions:
                        self.scan_word(word, y, x, dir)


    def scan_word(self, word, y, x, direction):
        """Function that given and x,y point, scans 8 directions(N, NE, E, SE, S, SW, W, NW)
        to see if a given word is present

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of the point we wish to examine
        x: int
            x coordinate of the point we wish to examine
        direction: list of int
            two value list that represents a cardinal direction that
            we wish to explore(a list of directions is defined as the class member, 'directions')
            the first element represents an offset in the y direction, and the second element represents
            an offset in the x direction. These offsets take the value -1, 0, or 1. The cardinal directions
            are represented as follows:
            [-1,  0] NORTH
            [-1,  1] NORTHEAST
            [ 0,  1] EAST
            [ 1,  1] SOUTHEAST
            [ 1,  0] SOUTH
            [ 1, -1] SOUTHWEST
            [ 0, -1] WEST
            [-1. -1] NORTHWEST
        
        """

        # extract x and y offsets from the direction list
        y_offset, x_offset = direction

        # # initialize an empty list of coordinates for the potential word location
        coordinates = []

        # for each character in the word
        for i, char in enumerate(word):

            # compute the x and y coordinates of the point we wish to explore using offsets
            x_i = x + i * x_offset
            y_i = y + i * y_offset

            # if the computed point is out of bounds, return
            if(x_i < 0 or x_i >= self.dims or y_i < 0 or y_i >= self.dims):
                return

            # if the letter at the computed point equals the letter of the word we are looking for
            # append the current point to the coordinates list
            if(self.board[y_i][x_i] == char):
                coordinates.append([x_i, y_i])

        # finally, if the length of the coordinates list is equal to length of the word
        # we were looking for, append the coordinates we found, along with the word,
        # to the answers dictionary
        if(len(coordinates) == len(word)):
            self.answers[word] = coordinates

    
    """Function that prints out the answers dictionary. It prints out the word, along
    with the coordinates of its letters found in the game board

    """
    def print_solutions(self):
        for word in self.answers:
            print(word)
            print(*self.answers[word])