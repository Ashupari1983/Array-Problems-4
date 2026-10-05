def maxpoints():
    arr = [11,-4,5,2,-3,1]
    print(arr)
    current = best = 0

    for i in arr[1:]:
        if current<0: current = i
        else: current += i
        if current>best:
            best = current

    print('Current:',current,'Best:',best)

maxpoints()