def BinarySearch(list,key):

    low = 0
    high = len(list)-1

    while(low <= high):
        
        mid = low + ((high-low)>>1)

        if (list[mid] < key):
            low = mid + 1
        elif (list[mid] > key):
            high = mid - 1
        else:
            return mid

if __name__ == "__main__":

    list = [1,4,5,12,33,45,58,74,93]

    print (list)
    print ("search 93:",BinarySearch(list,93))
    print ("search 1:",BinarySearch(list,1))
    print ("search 33:",BinarySearch(list,33))
    print ("search 5:",BinarySearch(list,5))
