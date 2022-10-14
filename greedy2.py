def solution1(number, k):
    arr = list(number)
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    MAX =[arr[0]]
    num_i = 1
    if len(number) == 2:
        return max(arr)
    while (k > 0 and len(MAX) < len(number) - k):
        if (MAX[-1] > arr[num_i]):
            if num_i != len(arr) -1:
                if (arr[num_i] > arr[num_i + 1]):
                    MAX.append(arr[num_i])
                    num_i += 1

                else:
                    num_i += 1
                    k -= 1
            else:
                return "".join(map(str,MAX))

                
        elif (MAX[-1] < arr[num_i]):
            while MAX[-1] < arr[num_i] and k > 0:
                MAX.pop()
                k -= 1
                if not MAX or k <= 0:
                    break
            MAX.append(arr[num_i])
            num_i += 1

        else:
            MAX.append(arr[num_i])
            num_i += 1
    if (len(MAX) < len(number) - k):    
        for i in range(num_i, len(arr)):
            MAX.append(arr[i])
            
    return "".join(map(str,MAX))


print(solution1("111111", 2))



def solution2(number, k):
    answer = []

    for i in number:
        if not answer:
            answer.append(i)
            continue
        while answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)

print(solution2("111111", 2))

'''def solution(number, k):
    arr = list(number)
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    
    min_num = 0
    while(k > 0):
        find = False
        for i in range(len(arr) - 1):
            if (arr[i] == min_num and find == False):
                arr.pop(i)
                k -= 1
                find = True
        if (find == False):
            min_num += 1
    return "".join(map(str,arr))'''