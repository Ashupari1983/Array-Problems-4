def max_after(n):
    arr = [-n] + [1]*n
    print(arr)

    current = best = arr[0]

    for i in arr[1:]:
        if current<0: current = i
        else: current += i
        if current>best: best = current

    return best

n = int(input('Enter number: '))
print('MaxAfter:',max_after(n))