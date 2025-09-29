#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 홍길동
#  작성일: 2024-09-15
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

import time

def factorial_iter(n):
    #반복문
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n):
    #재귀 호출
    if n == 0 or n == 1:
        return 1
     
    return n * factorial_rec(n-1)

def menu_1(n):
    if n >= 0:
        print(f"[반복] {n}!: {factorial_iter(n)}")
    else:
        print("정수(0이상의 숫자)만 입력해주세요")
        return False

def menu_2(n):
    if n >= 0:
        print(f"[재귀] {n}!: {factorial_rec(n)}")
    else:
        print("정수(0이상의 숫자)만 입력해주세요")
        return False

def run_with_time():
    n = (input("\nn값(정수,0 이상)을 입력하세요: ").strip())
    if  (n.isdigit()):
            n = int(n)
    else:
        print("정수(0이상의 숫자)만 입력해주세요")
        return 0,0,0,0,0
    start = time.perf_counter()
    r1 = factorial_iter(n)
    end_time = time.perf_counter()
    t1 = (end_time - start)
    start = time.perf_counter()
    r2 = factorial_rec(n)
    end_time = time.perf_counter()
    t2 = (end_time - start)
    return n,r1, r2, t1, t2

def run_test():
    for n in list:
        start = time.perf_counter()
        r1 = factorial_iter(n)
        end_time = time.perf_counter()
        t1 = (end_time - start)
        start = time.perf_counter()
        r2 = factorial_rec(n)
        end_time = time.perf_counter()
        t2 = (end_time - start)
        if r1 == r2:
            same = True
        else:
            same = False
        print(f"n = {n} | same = {same} | iter = {t1:.6f} | rec = {t2:.6f} \n {n}! = {r1}")


list = [0,1,2,3,5,10,15,20,30,50,100]

if __name__ == "__main__":
    count = ''
    while count != 'q':
        print("========== Facrotial Tester ==========")
        print("\n1) 반복문으로 n! 계산.")
        print("\n2) 재귀로 n! 계산.")
        print("\n3) 두 방법 모두 계산 후 결과/시간 비교.")
        print("\n4) 준비된 테스트 데이터 일괄 실행.")
        print("\nq) 종료.")
        count = (input("\n선택: ").strip())        
        if count == '1':
            n = (input("\nn값(정수,0 이상)을 입력하세요: ").strip())
            if  (n.isdigit()):
                n = int(n)
            else:
                print("정수(0이상의 숫자)만 입력해주세요")
                continue
            if not menu_1(n):
                continue
        if count == '2':
            n = (input("\nn값(정수,0 이상)을 입력하세요: ").strip())
            if  (n.isdigit()):
                n = int(n)
            else:
                print("정수(0이상의 숫자)만 입력해주세요")
                continue
            if not menu_2(n):
                continue
        if count == '3':
            n, r1,r2,t1,t2 = run_with_time()
            if r1 == 0:
                continue
            print(f"[반복] {n}!: {r1}")
            print(f"[재귀] {n}!: {r2}")
            if (r1) == (r2):
                 tf = "일치"
            else:
                 tf = "불일치"
            print(f"결과 일치 여부: {tf}")
            print(f"[반복] 시간: {t1:.6f} | [재귀] 시간: {t2:.6f}")
        if count == '4':
            run_test()


        
    #n = int(input("\n정수를 입력하세요: ").strip())
    #print(f"반복문 기반: {factorial_iter(n)}")
    #try:
    #    print(f"재귀 기반: {factorial_rec(n)}")
    #except RecursionError:
    #    print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

    # main()