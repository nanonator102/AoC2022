import os

if __name__ == '__main__':
    days = 25
    puzzles = 2
    for x in range(1, (days + 1)):
        directory = 'Day' + str(x)
        puzzle_name = 'Puzzle'
        extension = '.py'

        if not os.path.exists(directory):  # Make the directory if it does not exist.
            os.makedirs(directory)

        input_path = directory + '/' + 'input'
        test_input_path = directory + '/' + 'test_input'

        if not os.path.exists(input_path):  # Make the input file if it does not exist.
            with open(input_path, 'w'):
                pass

        if not os.path.exists(test_input_path):  # Make the test input file if it does not exist.
            with open(test_input_path, 'w'):
                pass

        for y in range(1, (puzzles + 1)):  # Make the files for the puzzles
            file_path = directory + '/' + puzzle_name + str(y) + extension
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write('if __name__ == \'__main__\':\n    pass\n')
