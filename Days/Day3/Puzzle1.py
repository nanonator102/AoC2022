UPPERCASE_OFFSET = 38
LOWERCASE_OFFSET = 96

if __name__ == '__main__':
    with open('input', 'r') as fp:
        priority = 0
        for line in fp:
            line = str.strip(line)
            first, second = line[:len(line)//2], line[len(line)//2:]
            print(f'First: {first}, Second: {second}')
            duplicate = None
            for i in first:
                for j in second:
                    if i == j:
                        duplicate = i
            if duplicate is not None:
                if duplicate.isupper():
                    priority += (ord(duplicate)-UPPERCASE_OFFSET)
                else:
                    priority += (ord(duplicate)-LOWERCASE_OFFSET)
                duplicate = None
    print(priority)
