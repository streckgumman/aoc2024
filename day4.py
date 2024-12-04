import re


def part1():
    total = 0
    with open("input.txt") as f:
        # all simple ones
        lines = f.read()
        total += len(re.findall('(?=(XMAS|SAMX))', lines))
        
        # transposing
        lien = lines.splitlines()
        transposed = [''.join(group) for group in zip(*lien)]
        total += sum([len(re.findall('(?=(XMAS|SAMX))', transp)) for transp in transposed])
        
        # diagonally
        diag = transpose_diagonal(lien)
        total += sum([len(re.findall('(?=(XMAS|SAMX))', dia)) for dia in diag])

        diag = transpose_diagonal_reverse(lien)
        total += sum([len(re.findall('(?=(XMAS|SAMX))', dia)) for dia in diag])
        
    print(total)
    
    
def part2():
    total = 0
    
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for i in range(1, len(lines) - 1):
            for j in range(1, len(lines[0]) - 1):
                block = [lines[x][j-1:j+2] for x in range(i-1, i+2)]
        
                masses = 0
                
                diag = transpose_diagonal(block)
                masses += sum([len(re.findall('(?=(MAS|SAM))', dia)) for dia in diag])
                
                diag = transpose_diagonal_reverse(block)
                masses += sum([len(re.findall('(?=(MAS|SAM))', dia)) for dia in diag])
                
                total += 1 if masses == 2 else 0
                
    print(total)
    

def transpose_diagonal(grid):
    diagonal = []
    for d in range(-len(grid) + 1, len(grid[0])):
        diagonal.append(''.join(grid[i][i - d] for i in range(max(d, 0), min(len(grid), len(grid[0]) + d))))
        
    return diagonal


def transpose_diagonal_reverse(grid):
    diagonal = []
    for d in range(len(grid) + len(grid[0]) - 1):
        diagonal.append( ''.join(grid[i][d - i] for i in range(max(0, d - len(grid[0]) + 1), min(len(grid), d + 1))))
        
    return diagonal


if __name__ == "__main__":
    # part1()
    part2()






