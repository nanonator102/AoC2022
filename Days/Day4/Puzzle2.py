if __name__ == '__main__':
    with open('input', 'r') as fp:
        overlap = 0
        for line in fp:
            line = str.strip(line)
            elf1, elf2 = line.split(',')
            elf1 = elf1.split('-')
            elf_temp = elf1
            elf1 = [int(elf_temp[0]), int(elf_temp[1])]
            elf2 = elf2.split('-')
            elf_temp = elf2
            elf2 = [int(elf_temp[0]), int(elf_temp[1])]

            # if start and end of elf 1 are before/after elf2 there is no overlap
            if elf1[0] < elf2[0] and elf1[1] < elf2[0]:
                print('Start/end less than')
            else:
                if elf1[0] > elf2[1]:
                    print('Start/end greater than')
                else:
                    overlap += 1
    print(overlap)
