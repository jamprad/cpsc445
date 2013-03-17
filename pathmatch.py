'''
University of British Columbia, CPSC 445: Algorithms for Bioinformatics
PathMatch
'''

from pygraph.classes.graph import graph
from pygraph.algorithms.minmax import shortest_path_bellman_ford

def readQPath():
    return

def readQGraph():
    return

def readCorrespondences():
    return

def constructGPrime(G,V_i,delta,m):
    print "Constructing G'..."
    
    # PRE-COMPUTE shortest paths
    shortest_paths = {}
    for v in G:
        shortest_paths[v] = shortest_path_bellman_ford(G,v)
    #print 'shortest_paths: %s' % shortest_paths
        
    # NODES
    G_p = graph()
    G_p.DIRECTED = True
    for p_i in V_i:
        for v in V_i[p_i]:
            G_p.add_node("%s.%s" % (p_i,v), attrs=[('weight',V_i[p_i][v])])
    G_p.add_node(0,attrs=[('weight',0)]) #source
    G_p.add_node(-1,attrs=[('weight',0)]) #sink
    print "NODES: %s" % G_p.nodes()
    
    # EDGES
    for i in V_i:
        for j in V_i[i]:
            v_ij = "%s.%s" % (i,j)
            shortest_path_j = shortest_paths[j][-1]
            #print 'shortest_path_%s: %s' % (j,str(shortest_path_j))
            d = 0
            while d <= m + 1:
                for l in shortest_path_j:
                    v_idl = "%s.%s" % (i+d,l)
                    if v_ij == v_idl:
                        continue
                    d_p = shortest_path_j[l]
                    if d_p <= m + 1:
                        try:
                            G_p.add_edge((v_ij,v_idl), attrs=[('weight', max(d,d_p)*delta)])
                        except:
                            pass
                d += 1
            try:
                G_p.add_edge((0, v_ij), attrs=[('weight', (i-1)*delta)]) # from source
                G_p.add_edge((v_ij, -1), attrs=[('weight', (len(V_i)-i)*delta)]) # to sink
            except:
                pass
    print "EDGES: %s" % G_p.edges()
    
    print "... Done."
    
    return G_p

# q is the query path
# G is the query graph
# V_i is the correspondences
# d is the mismatch and indel penalty
# m is the maximum number of mismatches/indels allowed between 2 matches
def pathMatch(q, G, V_i, d, m):
    # construct G_p (G')
    G_p = constructGPrime(G,V_i,d,m)
     
    return

def main():
    
    # q is the query path
    q = readQPath()
    q = graph()
    q.DIRECTED = True
    q.add_nodes([1,2,3])
    q.add_edge((1,2))
    q.add_edge((2,3))
    print "q = %s" % q
    
    # G = (V,E) is the query graph 
    G = readQGraph()
    G = graph()
    G.DIRECTED = True
    V = [1,2,3,4,5,6]
    E = [(1,2),(2,3),(3,4),(4,5),(5,6)]
    G.add_nodes(V)
    for e in E:
        G.add_edge(e)
    print "G = %s" % G
    
    # V_i is the set of correspondences
    V_i = readCorrespondences()
    V_i = {1:{1:1,4:1},2:{2:1,5:1},3:{3:1,6:1}}
    print "V_i = %s" % V_i
    
    #d is the mismatch and indel penalty
    d = -1
    print "d = %s" % d
    
    #m is the maximum number of mismatches/indels between 2 matches
    m = 2
    print "m = %s" % m
    
    pathMatch(q, G, V_i, d, m)
    
    
    
    return

if __name__ == "__main__":
    main()