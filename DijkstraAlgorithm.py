import heapq
def main():
    start_point=input("where are your starting point?")
    finish_point=input("where are you going?")
    # We have identified the map in the dictionary
    graph={}
    graph['a']=[('c',30),('b',20),('d',100)]
    graph['b']=[('a',20),('f',70)]
    graph['c']=[('a',30),('f',40),('e',60)]
    graph['d']=[('a',100),('e',20),('g',50)]
    graph['e']=[('c',60),('d',20),('g',30)]
    graph['f']=[('b',70),('c',40),('h',110)]
    graph['g']=[('d',50),('e',30),('h',60)]
    graph['h']=[('f',110),('g',60)]
    graph['i']=[]

    shortest_path(graph, start_point, finish_point)
    
def shortest_path(graph, source, target):
    infinite= (9999999999999999999999999999999999999999) #infinite distance
    pred = { x:x for x in graph }
    distance = { x:infinite for x in graph } #all nodes equal to infinite
    distance[ source ] = 0 #starting point equal to 0
    priority_q = [] #priority queue
    heapq.heappush(priority_q, [distance[ source ], source]) #start point
    while(priority_q):
        #pop the from priority queue and looked at its neighbors
        n = heapq.heappop(priority_q)
        n_distance = n[0]
        n_name= n[1]
        if n_distance == distance[n_name]:
            for i in graph[n_name]:
                i_name = i[0]
                i_dis = i[1]
                if distance[n_name] +i_dis <= distance[i_name]:
                    distance[i_name] = distance[n_name] + i_dis
                    heapq.heappush(priority_q, [distance[i_name], i_name])
                    pred[i_name] = n_name
    if distance[target]==infinite:
         print("There is no path between ", source, "and", target)
    else:
        st = []
        node = target
        while(True):
            st.append(str(node))
            if(node==pred[node]):
                break
            node = pred[node]
        path = st[::-1]
        print("\n"+"The shortest path is: " + " ".join(path) + "\n")
        print("The distance from "+source+" to "+target+" is:" + str(distance[target]) + "\n\n")
main()
