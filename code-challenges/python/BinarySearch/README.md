## Binary Search
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array. 

## Whiteboard Process  

![Alt text](Imgs/Capture.PNG?raw=true "directory")  


## Approach & Efficiency

- Prompted user to pass array and value as an input.
- Find mid point of array and compared with value passed in.
- If value matches, return index of array.
- Splitted array in half and searched value in one half, if found ignore second half and vice versa. 
