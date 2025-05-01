[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VW69817Y)
# Python-algorithmic_thinking-quicksort

Implement the quicksort presented in pseudo code below in Python in the `quicksort.py` file. Then run the `app.py` file to test your implementation. The output should be "Congratulations! No error detected.".

```
BEGIN QuickSort(list, low=0, high=-1)
  IF high == -1
    high = LENGTH OF list -1
  ENDIF
  IF low < high
    pi = Partition(list, low, high)
    QuickSort(list, low, pi - 1)
    QuickSort(list, pi + 1, high)
  ENDIF
END QuickSort

BEGIN Partition(list, low, high)
  pivot = list[high]  
  i = low - 1
  FOR j FROM low TO high
    IF list[j] < pivot
      i++
      SWAP list[i] AND list[j]
    ENDIF
  ENDFOR
  SWAP list[i + 1] AND LIST[high]
  RETURN i + 1
END Partition
```
Source: https://www.geeksforgeeks.org/quick-sort/
