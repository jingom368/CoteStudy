from collections import Counter
from math import prod
import collections

def solution(clothes):
    sum = 1
    for x in Counter([clo for clo in zip(*clothes)][1]).values():
        sum = sum*(x+1)
    answer = prod([x+1 for x in Counter([clo for clo in zip(*clothes)][1]).values()])-1
    
    # clothes : [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    # *(unpack) : 같은 인덱스끼리 묶어줌.
    # list(zip(*clothes)) : [["yellow_hat","blue_sunglasses","green_turban"],["headgear","eyewear","headgear"]]
    
    
    # [clo for clo in zip(*clothes)] : for clo in zip(*clothes) 와 같은 의미
    # [clo for clo in zip(*clothes)][0] = ["yellow_hat","blue_sunglasses","green_turban"]
    # [clo for clo in zip(*clothes)][1] = ["headgear","eyewear","headgear"]
    
    # Counter([clo for clo in zip(*clothes)][1] = {"headgear":2,"eyewear":1}
    # list(Counter([clo for clo in zip(*clothes)][1]).values()) = [2,1]
    # [x+1 for x in Counter([clo for clo in zip(*clothes)][1]).values()] = 2를 뺴서 1을 더하고 1을 빼서 1을 더하라
    # prod() = (2+1)*(1+1) 
    
    return answer