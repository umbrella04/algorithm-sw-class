def hanoi_tower(n,start,tmp,target):
    if n == 1: 
        print(f"원반 {n} : {start} -> {target}")
        return
    
    hanoi_tower(n-1,start,target,tmp) # 위의 n-1개를 start -> tmp로 옮김(target을 임시 보조)
    print(f"원반 {n} : {start} -> {target}") # 가장 큰 1개를 start에서 target으로 옮김
    hanoi_tower(n-1,tmp,start,target) # tmp에 놓여있는 n-1개를 타겟으로 옮김


if __name__ == "__main__":
    hanoi_tower(4,"A","B","C")