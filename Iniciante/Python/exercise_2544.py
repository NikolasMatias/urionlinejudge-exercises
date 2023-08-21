while True:
    try:
        from math import log2
        num_copias = int(input())
        print(str(int(log2(num_copias))))
    except EOFError: break