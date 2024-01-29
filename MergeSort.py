#MergeSort
inputList = [9,1,3,2,5,4,0,7,8,11,89,12,23,-1,23,-123783,232,24,23,13,21,312,3,12,312323,4,4,5645,75,7568,343,5,345,3,534,5]


def split(inputList, masterList):
    splitList1 = inputList[0:len(inputList)//2]
    splitList2 = inputList[len(inputList)//2:len(inputList)] 

    if len(splitList1) != 1:
        split(splitList1, masterList)
    else:
        masterList.append(splitList1)

    if len(splitList2) != 1:
        split(splitList2, masterList)
    else:
        masterList.append(splitList2)

    return masterList

def merge(list1,list2):
        outputList = []
        pointer1 = 0
        pointer2 = 0

        while len(outputList) != len(list1) + len(list2):
            if list1[pointer1] <= list2[pointer2]:
                 outputList.append(list1[pointer1])

                 if pointer1 == len(list1)-1:
                      for index in range(pointer2,len(list2)):
                           outputList.append(list2[index])

                 else:
                      pointer1 += 1

            else:
                 outputList.append(list2[pointer2])

                 if pointer2 == len(list2)-1:
                    for index in range(pointer1,len(list1)):
                        outputList.append(list1[index])

                 else: 
                      pointer2 += 1
 
        return outputList

def autoRecurse(inputList):
     masterList = []
     for index in range(0,(len(inputList)+1)//2):
          pointer1 = index
          pointer2 = len(inputList) - (index + 1)

          if pointer1 != pointer2:
               masterList.append(merge(inputList[pointer1],inputList[pointer2]))

          else:
               masterList.append(inputList[pointer1])

     if len(masterList) != 1:
        return autoRecurse(masterList)
     
     else:
        return masterList[0]

def MergeSort(inputList):
    return autoRecurse(split(inputList,[]))
                   
print(MergeSort(inputList))


     
                
      

                    


