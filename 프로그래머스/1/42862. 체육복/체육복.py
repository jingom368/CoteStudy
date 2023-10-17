def solution(n, lost_, reserve_):
    reserve = sorted([x for x in reserve_ if x not in lost_])

    lost = sorted([x for x in lost_ if x not in reserve_])
    reserve_o = [[reserve[i]-1,reserve[i]+1] for i in range(len(reserve))]
    j = 0
    lost_c = lost.copy()
    length = len(lost)
    while j < length:
        if [number for number in reserve_o if lost_c[j] in number] != []:
            reserve_o.remove([number for number in reserve_o if lost_c[j] in number][0])
            lost.remove(lost_c[j])
        j = j+1
    answer = n - len(lost)
    return answer