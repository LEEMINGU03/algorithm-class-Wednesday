def climb_stairs(n):
    mem = [0] * (n+1) # mem[1]일떄도 접근가능하게 n+1로 배열 크기 정했습니다.

    # 인덱스 0 이 첫번째 계단
    mem[0] = 1

    #인덱스 1이 두 번째 계단
    mem[1] = 2

    # 점화식 
    for i in range(2, n):
        mem[i] = mem[i-1] + mem[i-2]

    #결과 반환
    return mem[n-1]

#t실행
user = input("계단의 개수를 입력하시오: ")

if user.isdigit():
    n = int(user)
    
    if n > 0:
        result = climb_stairs(n)
        print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")
    else:
        print("1 이상의 자연수를 입력해주세요.")
else:
    print("잘못된 입력입니다.")