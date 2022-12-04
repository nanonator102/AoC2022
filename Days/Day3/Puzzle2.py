UPPERCASE_OFFSET = 38
LOWERCASE_OFFSET = 96

if __name__ == '__main__':
    with open('input', 'r') as fp:
        priority = 0
        lines = []
        for line in fp:
            line = line.strip()
            lines.append(line)
            if len(lines) != 3:  # If 3 lines are not stored then continue to next loop.
                continue
            # Find badge between rucksacks
            badge = None
            for i in lines[0]:
                for j in lines[1]:
                    if i == j:
                        for ij in lines[2]:
                            if i == ij:
                                badge = i
                                break
            # Convert identifier to number and add to priority
            if badge is not None:
                if badge.isupper():
                    priority += (ord(badge)-UPPERCASE_OFFSET)
                else:
                    priority += (ord(badge)-LOWERCASE_OFFSET)
                badge = None
            lines.clear()
    print(priority)
