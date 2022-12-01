if __name__ == '__main__':
    with open('input', 'r') as fp:
        calories = 0
        max_calories = 0
        for line in fp:
            line = str.strip(line)  # Strips the new-line character
            if line == "":
                if calories > max_calories:
                    max_calories = calories
                calories = 0
            else:
                calories += int(line)
        print(max_calories)

