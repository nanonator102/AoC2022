if __name__ == '__main__':
    with open('input', 'r') as fp:
        calories = 0
        first_max_calories = 0
        second_max_calories = 0
        third_most_calories = 0
        for line in fp:
            line = str.strip(line)  # Strips the new-line character
            if line == "":
                if calories > third_most_calories:
                    third_most_calories = calories
                    if third_most_calories > second_max_calories:
                        third_most_calories, second_max_calories = second_max_calories, third_most_calories
                        if second_max_calories > first_max_calories:
                            second_max_calories, first_max_calories = first_max_calories, second_max_calories
                calories = 0
            else:
                calories += int(line)
        max_calories = first_max_calories + second_max_calories + third_most_calories
        print(first_max_calories)
        print(second_max_calories)
        print(third_most_calories)
        print(max_calories)

