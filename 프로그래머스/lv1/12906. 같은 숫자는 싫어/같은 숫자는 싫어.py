def solution(arr):
    # hello = [arr[i] for i in range(len(arr)-1) if arr[i]!=arr[i+1]]
    # hello.append(arr[-1])
    # answer = hello
    # 
    # return answer  

    hello = []
    # ->
    # len(arr) : arr의 길이
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]: # 앞에 있는 것이 뒤에 있는 것과 같지 않을 경우에만 넣어주기
            hello.append(arr[i])
    hello.append(arr[-1]) # 마지막 원소 넣어주기
    answer = hello
    return answer  
    
    # a = []
    # answer = a[-1:]
    # for i in arr:
    #     if a[-1:] == [i]: continue
    #     a.append(i)
    # return a