while True:     
    N = int(input())
    if N == -1:
        break
    arr = []
    for i in range(1, N + 1):
        if N % i == 0:
            arr.append(i)
    if sum(arr) - N == N:
        print(f"{N} = 1", end = " ")
        for i in range(1, len(arr) - 1):
            print(f"+ {arr[i]}", end = " ")
        print()
    else:
        print(f"{N} is NOT perfect.")