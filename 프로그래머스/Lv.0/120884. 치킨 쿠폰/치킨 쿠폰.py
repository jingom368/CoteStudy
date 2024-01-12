# def solution(chicken):
#     chicken = 555554
#     answer = chicken
#     while (chicken>=10):
#         chicken = chicken//10  
#         answer += chicken
#     answer = (answer)//10
#     return answer

def solution(chicken):
    service = 0
    while chicken >= 10:
        service += chicken // 10
        chicken = chicken // 10 + chicken % 10
    return service

# 555554 
# +55555
# + 5555
# +  555
# +   55
# +    5

# 555554 / 55555 + 5555(55559) + 556(5564) + 56(560) + 5(56) + 1(11)
