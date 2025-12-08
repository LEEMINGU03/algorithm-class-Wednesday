# 1. DP 테이블 생성 
def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w-wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)
    
    return A

# 2. 역추적 함수 (물건 찾기)
def find_items(A, W, wt, n, item_names):
    items = []
    current_w = W
    
    # 마지막 물건 부터 꺼꾸로 추적 
    for i in range(n, 0, -1):
        # 값이 위쪽과 다르면 물건 추가
        if A[i][current_w] != A[i-1][current_w]:
            items.insert(0,item_names[i-1]) # 리스트에 추가
            current_w -= wt[i-1]              
            
    return items

# 실행

item_names = ["노트북", "카메라", "책", "옷", "휴대용 충전기"]
wt = [3, 1, 2, 2, 1]
val = [12, 10, 6, 7, 4]
n = len(val)

# 입력 및 실행
user= input("배낭 용량을 입력 하세요 : ")

if user.isdigit():
    W = int(user)
    
    # DP 테이블 생성
    A = knapSack_dp(W, wt, val, n)
    
    # 결과 계산 
    max_score = A[n][W]
    
    # 선택된 물건 가져오기 
    items =find_items(A, W, wt, n, item_names)
    
    # 결과 출력
    print(f"최대 만족도: {max_score}")
    print(f"선택된 물건: {items}")

else:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")