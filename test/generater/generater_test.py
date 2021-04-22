# coding:utf-8

def parse_file():
    result = []
    with open('file.txt', 'r') as fp:
        for i in range(1000000):
            eachline = fp.readline()
            print(str(i) + '\n')
            # yield eachline
            result.append(eachline)
    return result


def main():
    function_generate = parse_file()
    for i in function_generate:
        print(i)


if __name__ == '__main__':
    main()
