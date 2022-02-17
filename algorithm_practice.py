random_list = [5,8,9,3,4,1,2,7,6,10,12,11]

def selectionsort(unsorted_list):
    
    print(unsorted_list)

    temp = random_list[0]

    for i in range (len(unsorted_list)):
        #if the values aren't in order, swap them
        for j in range (i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list [i]:
                temp = unsorted_list [i]
                unsorted_list[i] = unsorted_list [j]
                unsorted_list[j] = temp

    print (unsorted_list)

selectionsort(random_list)

#
def binarysearch(unsorted_list, target):
    print (unsorted_list)

    #grab indexes to aid in our search
    search_start = 0
    search_end = len(unsorted_list) - 1