# 203 List Maps

## Objectives
* creating a map from a list or tuple

Sometimes you may have a set of data that you want to iterate through, and then store the results for later use.  One possible way to do this would be to iterate through the list, and then do each of the tasks as you iterate through.  However, sometimes, it's more efficient to iterate through the list and store some data in a second list. If you don't need to use that second list more than once, why bother keeping a lot of memory tied up storing it?

Enter the map.  A map is created from a list or tuple, and behaves like a list or tuple, but *is only accessible once before it is cleared from memory*.

Take a look at sample1.py, and then answer the questions in your Google Doc file.

Read one of the pages that has more information about list maps:
* https://www.geeksforgeeks.org/python/python-map-function/
* https://www.freecodecamp.org/news/python-map-explained-with-examples/#:~:text=The%20map()%20function%20in,other%20parts%20of%20your%20code.


One advantage of a map is in terms of speed.  sample3.py shows you some examples of how fast a list map is compared to list comprehension or for loops.  Note here that we are using some methods for finding out how long a set of command takes, and it makes use of time tracking commands.

### How long does something take?
* record a starting time
* do your commands
* record the ending time
* the total elapsed time is the ending time minus the starting time
 
 Example:
 ```
 import time

 start = time.time()
 # commands go here
 end = time.time()

 elapsed_time = end - start
 print(f"Your task took {elapsed_time} seconds")

 Try looking at the code in sample3.py to see what is going on.  Note that when you run it, it takes approximately 6 seconds for the program to complete!