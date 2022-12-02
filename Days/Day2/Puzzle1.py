if __name__ == '__main__':
    with open('input', 'r') as fp:
        score = 0
        for line in fp:
            line = str.strip(line)  # Strips the new-line character
            moves = line.split()
            # Add score for my move
            # A, X = Rock
            # B, Y = Paper
            # C, Z = Scissors
            match moves[1]:
                case 'X':
                    score += 1
                    match moves[0]:
                        case 'A':
                            score += 3
                        case 'B':
                            pass
                        case 'C':
                            score += 6
                case 'Y':
                    score += 2
                    match moves[0]:
                        case 'A':
                            score += 6
                        case 'B':
                            score += 3
                        case 'C':
                            pass
                case 'Z':
                    score += 3
                    match moves[0]:
                        case 'A':
                            pass
                        case 'B':
                            score += 6
                        case 'C':
                            score += 3
        print(score)
