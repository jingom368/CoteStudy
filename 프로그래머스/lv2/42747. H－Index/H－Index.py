def solution(citations):
    citations.sort(reverse=True)
    # [6,5,3,1,0]
    i=0
    
    while(i+1<=citations[i]):   
        i = i+1
        # 1번 이상 인용된 논문이 1개 이상
        # [1 <= 6]
        # 2번 이상 인용된 논문이 2개 이상
        # [2 <= 5]
        # 3번 이상 인용된 논문이 3개 이상
        # [3 <= 3]
        
        if i == len(citations):
            break
    answer = i
    return answer