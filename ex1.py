for i in range(1, 6):
    # 공백 출력
    for j in range(1, 6 - i):
        print(" ", end="")
    # 숫자 출력
    for k in range(1, 2 * i):
        print(k, end="")
    # 줄 바꿈
    print()