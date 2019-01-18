def split_and_join(line):
    newl=line.split(" ")
    newl="-".join(newl)
    return newl

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)