while True:
    try:
        num_pessoas, num_datas = [int(x) for x in input().split()]
        datas_com_pessoas = [input().split() for x in range(num_datas)]
        for data_com_pessoas in datas_com_pessoas:
            data = data_com_pessoas.pop(0)
            num_compareceram = sum([int(pessoas) for pessoas in data_com_pessoas])
            if num_compareceram == num_pessoas:
                print(data)
                break
        else:
            print('Pizza antes de FdI')
    except EOFError: break