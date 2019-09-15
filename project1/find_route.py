from queue import PriorityQueue
import sys
#custom node class will keep track of the node name, the cost to come to this node from the initial node and the immidiate node it has been derived from, parent node so to speak
class Node:
    def __init__(self, dataval,cost, previousval="NONE"):
        self.data_val = dataval
        self.previous_val=previousval
        self.node_cost = cost
    def __str__(self):
        class_print = "Node:"+self.data_val+ " child node: "+ self.next_val + " parent node: " + self.previous_val + " cost: " + str(self.node_cost)
        return class_print
    def __lt__(x,y):
        return (x.node_cost < y.node_cost) == 1
    def __eq__(x,y):
        return (x.data_val == y.data_val) 
   
def foundGoalState(ending_node, from_city):   #process the output once the destination city has been reached
    print("distance:",ending_node.node_cost,"km")
    print("route:")
    route=[]
    while(ending_node.data_val != from_city): #go back and find the parent back to initial state
        path = ending_node.previous_val.data_val + " to " + ending_node.data_val + ", "+ str(ending_node.node_cost - ending_node.previous_val.node_cost) + " km"
        route.append(path)
        ending_node = ending_node.previous_val
    for item in reversed(route): #becasue I found the node pointer of destionation city to starting city,, I have to reverse the city's list path to go from start to end 
        print(item)
          
def alreadyVisited(visited_nodes_list, new_node): #this is to figure out if a new is equal to another node
    for item in visited_nodes_list:
        if(item == new_node):
            return True
    return False
    
        
q = PriorityQueue()  # the priority queue
minimum_cost=sys.maxsize  
from_city = sys.argv[2]
to_city = sys.argv[3]
#checking if the origin city and destionation city are the same,, if it is,, no need for further expansion
if(from_city == to_city):
    print("distance: 0")
    print("route:")
    print("none")
    sys.exit(0)

initial_state = Node(from_city,0)
q.put(initial_state) #starting the queue with the initial states node
found_path = False
final_node=Node("N/A",0)
visited_nodes_list = []
while not q.empty():
    node_to_expand=q.get()
    visited_nodes_list.append(node_to_expand)
    file_to_read=open(sys.argv[1],"r");
    for line in file_to_read: #running the input file for all node that comes out of the Priority queue
        if(line == "END OF INPUT"):
            break;
        l=[]
        for word in line.split():
            l.append(word)
        new_node = Node("N/A",0) 
        #now check if it the parent to expand
        if(node_to_expand.data_val == l[0]) : #undirected graph, so the I can have to check both direction 
            temp = Node(l[1],int(node_to_expand.node_cost) + int(l[2]), previousval=node_to_expand)
            new_node = temp
            if ( not alreadyVisited(visited_nodes_list, new_node)):
                q.put(new_node)
        elif (node_to_expand.data_val == l[1]) :
            temp = Node(l[0],int(node_to_expand.node_cost) + int(l[2]), previousval=node_to_expand)
            new_node = temp
            if ( not alreadyVisited(visited_nodes_list, new_node)):
                q.put(new_node)
        if(new_node.data_val == to_city):
            found_path=True
            if(new_node.node_cost < minimum_cost): #have to go with the minimum cost 
                minimum_cost = new_node.node_cost
                final_node = new_node
                
if(found_path):
    foundGoalState(final_node, from_city)
#if it comes over here, ,means I haven't found the to_city expanding from_city
if(not found_path):
    print("distance: infinity")
    print("route:")
    print("none")

