def hanoi(From, To, Other, N):
    From = [i for i in range(N, 0, -1)]
    
    if len(To) == N:
        return len(To)
    else:
        pass
