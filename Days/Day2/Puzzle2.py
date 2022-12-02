if __name__ == '__main__':
    with open('input', 'r') as fp:
        score = 0
        for line in fp:
            line = str.strip(line)  # Strips the new-line character
            moves = line.split()
            # Add score for my move
            # A = Rock, 1 point
            # B = Paper, 2 points
            # C = Scissors, 3 points
            # X = Lose, 0 points
            # Y = Draw, 3 points
            # Z = Win, 6 points
            match moves[1]:
                case 'X':
                    match moves[0]:
                        case 'A':  # My move is Scissors
                            score += 3
                        case 'B':  # My move is Rock
                            score += 1
                        case 'C':  # My move is Paper
                            score += 2
                case 'Y':
                    match moves[0]:
                        case 'A':  # My move is Rock
                            score += 4
                        case 'B':  # My move is Paper
                            score += 5
                        case 'C':  # My move is Scissors
                            score += 6
                case 'Z':
                    match moves[0]:
                        case 'A':  # My move is Paper
                            score += 8
                        case 'B':  # My move is Scissors
                            score += 9
                        case 'C':  # My move is Rock
                            score += 7
            print(moves)
        print(score)
