Author: Gazi Mahbub Morshed

CWID: 10726727

Programming language: Python3
OS : windows 10.

Code structure: In the begining I have a custom node class which I used to create each city in the map. 
Then I a function that is called when the destination city has been found. And one more function to check if I already visited a city.
After that main code starts. I check if the origin and destination city is same or not. 
If not, I create a node with the origin city, add it to the priority queue and while the queue is not empty, 
I expand on the node and don't add duplicate node in the map.

How to run the code: In the windows command line type "python find_route input_filename origin_city destionation_city".


