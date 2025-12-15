def stair_dp_tab(n):
    # 1차원 테이블 준비
    table = [0] * (n + 1)

    table[1] = 1
    table[2] = 2

    # Bottom-up 방식으로 테이블 채우기
    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table


A = int(input("계단의 개수를 입력하시오 : "))
table = stair_dp_tab(A)
print(f"{A}개의 계단을 오르는 방법의 수는 {table[A]}가지입니다.") 
