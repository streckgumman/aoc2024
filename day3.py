import re


def part1():
    total = 0
    with open("input.txt") as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            muls = re.findall("mul\([0-9]*,[0-9]*\)", line)
            tot = [mul(x) for x in muls]
            total += sum(tot)
    print(total)
    
    
def part2():
    total = 0
    with open("input.txt") as f:
        lines = f.read()
        new_string = re.sub("don't\(\).*?(?=$|do\(\))", '', lines, flags=re.DOTALL)
        multiply_list = re.findall("mul\([0-9]*,[0-9]*\)", new_string)
        tot = [mul(x) for x in multiply_list]
        total += sum(tot)
    print(total)
    
    
def mul(str):
    match = re.match(r"mul\((\d+),(\d+)\)", str)
    num1 = int(match.group(1))
    num2 = int(match.group(2))
    return num1 * num2


if __name__ == "__main__":
    # part1()
    part2()