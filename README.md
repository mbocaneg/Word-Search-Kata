# Word-Search Kata
A python based solution to Pillar/Accenture's word search excercise. This project consists of 3 python source files, and 3 'puzzle' txt files.

The file `word_search.py` holds the class `WordSearch`, an OOP class that models a running wordsearch instance and any associated logic.

The file `test_word_search.py` holds the unit tests for validating my `WordSearch` class. 

The file `main.py` is the entry point by which the user interacts with the `WordSearch` object.

# Dependencies
This project was written using python 3.6.8. No external dependencies are needed. The only modules that were ever used are built in. These are Python's `unittest` module, used in `test_word_search.py` and `sys` module, used in `main.py` to use command line arguments.

# Running
To run the unit test, one simply needs to run:
```
python3 test_word_search.py
```
This unit test fixture uses the simple puzzle `test_puzzle.txt` for validation.

The actual solution logic is ran as follows:
```
python3 main.py <puzzle-filename.txt>
```
where an optional arguments, `<puzzle-filename.txt>`, denotes the name of a txt file that
contains a word search puzzle, as described in the original problem statement. If no
argument is given, then the application defaults to using the txt file `star_trek.txt` as
in the original problem statement. An additional puzzle file, `pokemon.txt` was added for
your convenience for further validation.