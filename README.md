# Camera-Detector

The program use heap to store the discovered list. All of the toll roads would be ignored. The edge will be store in the format: ([Starting point],[End point],[Distance]). 
The flag list will store the flag of the vertex or the latest distance from the starting point to it in order to update the heap.
Applying the Dijsktra algorithm and ignoring the toll road, the program will find all the minimum distances to all the intersection and choose k nearest one.

Space complexity: O(V + E) 
Time complexity: O(V log V + E log V )
