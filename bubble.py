def bubble_sort(List):

    for i in range(len(List) - 1):
        i = 0
        j = 1
        for i in range(len(List) - 1):
            if List[i] > List[j]:
                num1 = List[i]
                List[i] = List[j]
                List[j] = num1
            i += 1
            j += 1
    return List

List = [6,2,1,4,5,3]

bubble_sort(List)

#print(List)