import copy


def part1():
    total = 0
    
    with open("input.txt") as f:
        lines = [line.rstrip() for line in f]
        
        for line in lines:
            numbers = list(map(int, line.split()))
            safe = solve_left(numbers)
            safe2 = solve_left(numbers[::-1])
            
            if safe or safe2:
                total += 1
                
    print(total)
    
    
def part2():
    total = 0
    
    with open("input.txt") as f:
        lines = [line.rstrip() for line in f]
        
        for line in lines:
            safe = []
            numbers = list(map(int, line.split()))
            
            for i in range(len(numbers)):
                new_numbers = copy.deepcopy(numbers)
                new_numbers.pop(i)
                safe.append(solve_left(new_numbers))
                safe.append(solve_left(new_numbers[::-1]))
                
            if any(safe):
                total += 1
                
    print(total)
    
    
def solve_left(numbers):
    prev_number = numbers[0] - 1
    safe = True
    
    for number in numbers:
        if number <= prev_number or number - prev_number > 3:
            safe = False
            
        prev_number = number
        
    return safe


if __name__ == "__main__":
    part1()
    part2()
