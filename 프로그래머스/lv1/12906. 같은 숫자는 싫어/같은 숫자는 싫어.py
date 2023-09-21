def solution(arr):
    # k = []
    # for i in range(0,len(arr)-1):
    #     if arr[i] == arr[i+1]:
    #         k.append(i)
    # answer = [arr[i] for i in range(len(arr)) if i not in k]
    hello = [arr[i] for i in range(len(arr)-1) if arr[i]!=arr[i+1]]
    hello.append(arr[-1])
    answer = hello
    return answer