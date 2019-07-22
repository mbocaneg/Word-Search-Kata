from word_search import WordSearch
import sys

if __name__ == "__main__":
    filename = "star_trek.txt"
    if len(sys.argv) > 1:
        filename = str(sys.argv[1])        
    w = WordSearch(filename)
    w.solve_puzzle()
    w.print_solutions()