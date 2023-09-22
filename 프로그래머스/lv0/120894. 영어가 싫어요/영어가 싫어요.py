def solution(numbers):
    # number_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    # i=0
    # num=[]
    # while(len(numbers)!=0):
    #     i+=1
    #     if numbers[:i] in number_dict:
    #         num.append(numbers[:i])
    #         numbers = numbers[i:]
    #         i=0
    # answer = int(''.join([number_dict[i] for i in num]))
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng,str(num))
    return int(numbers)