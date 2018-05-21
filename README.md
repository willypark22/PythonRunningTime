Programming Assignment 1
Nearest Neighbor
Dong Uk Park 861203574

** When running divide and conquer algorithm for input files 100+, the program sometimes 
displays an error stating an invalid comparison between float() and tuple(). I think the problem
is because I have to return min_distance, point1, and point2 to main in order to output 
the points onto the file. When running recursion, it finds the return value to be tuple,
and converts min_distance to a tuple when it should be a float. I don't know if a float
can be converted to a tuple without assigning it, but I think this is the problem. Because
of this, when running divide and conquer, the text file only displays the distance. When
running with regular python, the code worked. I seem to have a probem when running python3.
Brute Force works fine. **

To run the algorithms, the syntax is as follows:

>> python3 nearestNeighbor.py --<algorithm>/<verbose> <algorithm> <filename>

Example:

>> python3 nearestNeighbor.py --algorithm d input10.txt

 - To run divide and conquer algorithm for the file inuput10.txt