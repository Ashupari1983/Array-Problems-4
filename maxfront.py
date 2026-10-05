def max(n):
    arr = [1]*n + [-1]
    print(arr)
    current = best = arr[0]

    for i in arr[1:]:
        if current<0: current = i
        else: current += i
        if current>best: best = current
    return best

n = int(input('Enter number: '))
print('Best Score:',max(n))