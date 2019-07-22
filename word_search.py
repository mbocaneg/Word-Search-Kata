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
    """

    board = []
    words = []
    answers = {}
    dims = 0


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
        for word in self.words:

            # ...for each row in the game board
            for y, row in enumerate(self.board):

                # ...for each column in each row
                for x, col in enumerate(row):

                    # try to find words in the:

                    # north direction
                    self.find_word_north(word, y, x)

                    # south direction
                    self.find_word_south(word, y, x)

                    # east direction
                    self.find_word_east(word, y, x)

                    # west direction
                    self.find_word_west(word, y, x)

                    # northeast direction
                    self.find_word_northeast(word, y, x)

                    # southeast direction
                    self.find_word_southeast(word, y, x)

                    # southwest direction
                    self.find_word_southwest(word, y, x)

                    # northwest direction
                    self.find_word_northwest(word, y, x)


    def find_word_north(self, word, y, x):
        """Function that tries to find a single word in the north direction. If it is 
        found, it produces a list of x/y coordinates that correspond to the position
        of each character within the word, and it populates the 'answers' dictionary 
        with the word as its key and the list as its value

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of point we wish to examine
        x: int
            x coordinate of point we wish to examine

        """

        # if we are at the topmost row, we cannot go further north, so return
        if(y == 0 ):
            return

        # initialize an empty list of coordinates for the potential word location
        coordinates = []

        # for each character in the word
        for i, char in enumerate(word):

            # if the character on the board at position {y-i, x} equals the current character of the word
            if(self.board[y - i][x] == char):

                # append the coordinates of this character to the coordinates list
                coordinates.append([x, y - i])

        # if the length of the coordinates list equals the length of the word, then
        # we succesfully found the position of the word
        if len(coordinates) == len(word):

            # ...so add the word and its coordinates to the answers dictionary
            self.answers[word] = coordinates


    def find_word_south(self, word, y, x):
        """Function that tries to find a single word in the south direction. If it is 
        found, it produces a list of x/y coordinates that correspond to the position
        of each character within the word, and it populates the 'answers' dictionary 
        with the word as its key and the list as its value

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of point we wish to examine
        x: int
            x coordinate of point we wish to examine

        """

        # if we are at the bottomost row or if the y position plus the length
        # of the word is greater than the length of the board, then return
        if(y == self.dims or y + len(word) > self.dims):
            return

        # initialize an empty list of coordinates for the potential word location
        coordinates = []
        
        # for each character in the word
        for i, char in enumerate(word):

            # if the character on the board at position {y+i, x} equals the current character of the word
            if(self.board[y + i][x] == char):

                # append the coordinates of this character to the coordinates list
                coordinates.append([x, y + i])

        # if the length of the coordinates list equals the length of the word, then
        # we succesfully found the position of the word
        if len(coordinates) == len(word):

            # ...so add the word and its coordinates to the answers dictionary
            self.answers[word] = coordinates


    def find_word_east(self, word, y, x):
        """Function that tries to find a single word in the east direction. If it is 
        found, it produces a list of x/y coordinates that correspond to the position
        of each character within the word, and it populates the 'answers' dictionary 
        with the word as its key and the list as its value

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of point we wish to examine
        x: int
            x coordinate of point we wish to examine

        """

        # if we are at the rightmost column or if the x position plus the length
        # of the word is greater than the length of the board, then return
        if(x == self.dims or x + len(word) > self.dims):
            return

        # initialize an empty list of coordinates for the potential word location
        coordinates = []
        
        # for each character in the word
        for i, char in enumerate(word):

            # if the character on the board at position {y, x+i} equals the current character of the word
            if(self.board[y][x + i] == char):

                # append the coordinates of this character to the coordinates list
                coordinates.append([x + i, y])

        # if the length of the coordinates list equals the length of the word, then
        # we succesfully found the position of the word
        if len(coordinates) == len(word):

            # ...so add the word and its coordinates to the answers dictionary
            self.answers[word] = coordinates


    def find_word_west(self, word, y, x):
        """Function that tries to find a single word in the west direction. If it is 
        found, it produces a list of x/y coordinates that correspond to the position
        of each character within the word, and it populates the 'answers' dictionary 
        with the word as its key and the list as its value

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of point we wish to examine
        x: int
            x coordinate of point we wish to examine

        """

        # if we are at the leftmost column or if the x position plus the length
        # of the word is less than 0, then return
        if(x == 0 or x - len(word) + 1 < 0):
            return

        # initialize an empty list of coordinates for the potential word location
        coordinates = []
        
        # for each character in the word
        for i, char in enumerate(word):

            # if the character on the board at position {y, x-i} equals the current character of the word
            if(self.board[y][x - i] == char):

                # append the coordinates of this character to the coordinates list
                coordinates.append([x - i, y])

        # if the length of the coordinates list equals the length of the word, then
        # we succesfully found the position of the word
        if len(coordinates) == len(word):

            # ...so add the word and its coordinates to the answers dictionary
            self.answers[word] = coordinates


    def find_word_northeast(self, word, y, x):
        """Function that tries to find a single word in the northeast direction. If it is 
        found, it produces a list of x/y coordinates that correspond to the position
        of each character within the word, and it populates the 'answers' dictionary 
        with the word as its key and the list as its value

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of point we wish to examine
        x: int
            x coordinate of point we wish to examine

        """

        # if we are at the topmost row, or at the rightmost column or if the x position plus the length
        # of the word is greater than the length of the board, then return
        if(y == 0 or y - len(word) + 1 < 0 or x == self.dims or x + len(word) > self.dims):
            return

        # initialize an empty list of coordinates for the potential word location
        coordinates = []

        # for each character in the word
        for i, char in enumerate(word):

            # if the character on the board at position {y-i, x+i} equals the current character of the word
            if(self.board[y - i][x + i] == char):

                # append the coordinates of this character to the coordinates list
                coordinates.append([x + i, y - i])

        # if the length of the coordinates list equals the length of the word, then
        # we succesfully found the position of the word
        if len(coordinates) == len(word):

            # ...so add the word and its coordinates to the answers dictionary
            self.answers[word] = coordinates

    def find_word_southeast(self, word, y, x):
        """Function that tries to find a single word in the southeast direction. If it is 
        found, it produces a list of x/y coordinates that correspond to the position
        of each character within the word, and it populates the 'answers' dictionary 
        with the word as its key and the list as its value

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of point we wish to examine
        x: int
            x coordinate of point we wish to examine

        """

        # if we are at the bottomost row or if the y position plus the length
        # of the word is greater than the length of the board, or if we are at 
        # the rightmost column or if the x position plus the length of the word 
        # is greater than the length of the board, then return
        if(x == self.dims or x + len(word) > self.dims or y == self.dims or y + len(word) > self.dims):
            return

        # initialize an empty list of coordinates for the potential word location
        coordinates = []

        # for each character in the word
        for i, char in enumerate(word):

            # if the character on the board at position {y+i, x+i} equals the current character of the word
            if(self.board[y + i][x + i] == char):

                # append the coordinates of this character to the coordinates list
                coordinates.append([x + i, y + i])

        # if the length of the coordinates list equals the length of the word, then
        # we succesfully found the position of the word
        if len(coordinates) == len(word):

            # ...so add the word and its coordinates to the answers dictionary
            self.answers[word] = coordinates

    def find_word_southwest(self, word, y, x):
        """Function that tries to find a single word in the southwest direction. If it is 
        found, it produces a list of x/y coordinates that correspond to the position
        of each character within the word, and it populates the 'answers' dictionary 
        with the word as its key and the list as its value

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of point we wish to examine
        x: int
            x coordinate of point we wish to examine

        """

        # if we are at the bottomost row or if the y position plus the length
        # of the word is greater than the length of the board, or if we are at 
        # the leftmost column or if the x position plus the length of the word 
        # is less than 0, then return
        if(y == self.dims or y + len(word) > self.dims or x == 0 or x - len(word) + 1 < 0):
            return

        # initialize an empty list of coordinates for the potential word location
        coordinates = []

        # for each character in the word
        for i, char in enumerate(word):

            # if the character on the board at position {y+i, x+i} equals the current character of the word
            if(self.board[y + i][x - i] == char):

                # append the coordinates of this character to the coordinates list
                coordinates.append([x - i, y + i])

        # if the length of the coordinates list equals the length of the word, then
        # we succesfully found the position of the word
        if len(coordinates) == len(word):

            # ...so add the word and its coordinates to the answers dictionary
            self.answers[word] = coordinates

    def find_word_northwest(self, word, y, x):
        """Function that tries to find a single word in the northwest direction. If it is 
        found, it produces a list of x/y coordinates that correspond to the position
        of each character within the word, and it populates the 'answers' dictionary 
        with the word as its key and the list as its value

        Parameters
        ----------
        word: str
            word we wish to find
        y: int
            y coordinate of point we wish to examine
        x: int
            x coordinate of point we wish to examine

        """

        # if we are at the topmost row, we cannot go further north, or if we are at the 
        # leftmost column or if the x position plus the length of the word is less than 0, then return
        if(y == 0 or y - len(word) + 1 < 0 or x == 0 or x - len(word) + 1 < 0):
            return

        # initialize an empty list of coordinates for the potential word location
        coordinates = []

        # for each character in the word
        for i, char in enumerate(word):

            # if the character on the board at position {y-i, x-i} equals the current character of the word
            if(self.board[y - i][x - i] == char):

                # append the coordinates of this character to the coordinates list
                coordinates.append([x - i, y - i])

        # if the length of the coordinates list equals the length of the word, then
        # we succesfully found the position of the word
        if len(coordinates) == len(word):

            # ...so add the word and its coordinates to the answers dictionary
            self.answers[word] = coordinates

