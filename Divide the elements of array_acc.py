def split_array(arr):
    mid = len(arr) // 2
    
    if len(arr) % 2 == 0: 
        return arr[:mid], arr[mid:]
    else: 
        return arr[:mid + 1], arr[mid + 1:]
    
input_array = input()

array = eval(input_array)
if not isinstance(array, list):
    raise ValueError("Input is not a list")

if len(array) < 2:
    print("Cannot determine, the minimum size of the array must be 2.")
elif all(isinstance(x, (int)) for x in array):
    part1, part2 = split_array(array)
    print(part1)
    print(part2)
else: 
    print("Cannot determine, as there is a list.")