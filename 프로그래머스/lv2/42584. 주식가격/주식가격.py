from collections import deque

def solution(prices):
    answer = []
    price = deque(prices)
    # price = 속도 향상을 위해 deque형으로 리스트 변형 : [1,2,3,2,3]
    
    while(price):
    # price 원소가 남아있다면 True
    
        count = 0
        pri = price.popleft()
        # 첫번째 원소를 빼내서 저장 pri = 1

        for i in price:
            count += 1
            if pri > i:
                break
        # pri < i 작은 경우, 즉 주식 가격이 떨어지지 않았을 때는 계속 count +=1
        # pri > i 클 경우, 즉 주식 가격이 떨어질 때 break
        
        answer.append(count)
        # answer에 count 원소 하나씩 추가
        
    return answer


# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer