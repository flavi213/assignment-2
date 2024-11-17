def maxPerimeter(s):
    s.sort()
    for i in range(len(s) - 1, 1, -1):
        if s[i-2] + s[i-1] > s[i]:
            return [s[i-2], s[i-1], s[i]]
    # If no valid triangle can be formed, return -1
    return [-1]

if __name__ == "__main__":
    n = int(input())  
    s = list(map(int, input().split())) 
    result = maxPerimeter(s)
    print(" ".join(map(str, result)))
