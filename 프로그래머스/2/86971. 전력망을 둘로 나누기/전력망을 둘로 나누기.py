from itertools import combinations
from collections import deque
import copy

def solution(n, wires):

    return min([connection(n, wire) for wire in combinations(wires, len(wires)-1)])
# 하나를 끊었을 때 모든 조합
# combinations(wires, len(wires)-1) -> 리스트중 len(wires)-1 길이로 만들 수 있는 모든 조합
# [[1,2],[2,3]], [[1,2],[3,4]], [[2,3],[3,4]]
# 모든 조합 중 connection(n,wire)이 가장 작은 것
 
    # 시험용
    # wire = [[1,3],[4,6],[7,8],[2,3],[3,4],[4,5],[7,9]]
    # wire = [[1,2],[3,4]]
    # wire = [[2,3],[3,4]]
    # wire = [[1,2],[2,7],[3,4],[4,5],[6,7]]
    # wire = [[1,2], [1,3]]
def connection(n,wire):
    
    # 초기 설정
    # 깊은 복사 안하면 오류남.
    # 얕은 복사를 하면 자료의 주소를 가져다 쓰기 때문에 pop할 때 원본 리스트에도 영향을 줌.
    # deque로 O(N) 줄이려고
    
    wire = copy.deepcopy(wire)
    wire = deque(wire)
    rot = 0
    seta = wire.popleft()
    # [1,2]
    setb = []
    
    # 연결된 노드를 연결해줘서 모두 seta에 들어가는 반복문
    # seta와 wire[0]의 교집합이 있다면
    # wire = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    # seta = [1,3]
    # wireA = [2,3]
    # seta = [1,3,2,3]
    # set(seta) = [1,2,3]
    # wire = [[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    
    while(wire):
        rot += 1
        if list(set(seta) & set(wire[0])) != []:
            wireA= wire.popleft()
            seta.append(wireA[0]), seta.append(wireA[1])
            seta = list(set(seta))
            rot = 0
        wire.rotate(-1)
        # print(wire, seta, rot)
        if rot == len(wire):
            break
    
    # 연결된 상태가 아니기에 남은 wire을 setb에 추가해줌
    # [7,8] [8,9] -> setb ; [7,8,8,9]
    # 반복되는 값이 있기에 set(집합) 함수를 주어서 반복을 없애고 
    # set함수는 set구조기 때문에 list형태로 바꿔줌
    for i in wire:
        setb.append(i[0])
        setb.append(i[1])
    setb = list(set(setb))
    
    # seta와 setb의 차의 절댓값
    # 예외처리 : setb의 길이가 0. 즉, 값이 없다면 모든 연결이 끊어진 후 1개만 남은 형태
    if len(setb) != 0:
        answer = abs(len(seta)-len(setb))
    else:
        answer = abs(len(seta)-1)
    return answer