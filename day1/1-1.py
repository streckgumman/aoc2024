def main():
    left = []
    right = []
    total = 0
    
    with open('day1/1.txt') as f:
        lines = [line.rstrip() for line in f]
        
        for line in lines:
            numbers = list(map(int, line.split()))
            left.append(numbers[0])
            right.append(numbers[1])
            
    left.sort()
    right.sort()
        
    for l, r in zip(left, right):
        total += abs(r - l)
            
    print(total)
      
        
if __name__ == "__main__":
    main()

