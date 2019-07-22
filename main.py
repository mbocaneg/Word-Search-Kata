from word_search import WordSearch
import sys

if __name__ == "__main__":

    # default puzzle filename. If user provides no puzzle name, load
    # puzzle from this filename
    filename = "star_trek.txt"

    # if user provides a command line argument, assume it to be the filename
    # for a puzzle file
    if len(sys.argv) > 1:
        filename = str(sys.argv[1])

    # initialize a WordSearch instance, using filename as an argument
    # solve the puzzle, and then print its solutions 
    w = WordSearch(filename)
    w.solve_puzzle()
    w.print_solutions()