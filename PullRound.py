# -*- coding: cp1254 -*-
from snap import *
import random
import sys
import math
import os

#random edge pull

def graph():
    global G2,uninfectedNodesList, edgeList, rNodeId, rEdge,infNCount,nOfRounds
    uninfectedNodesList = []
    G1 = GenRndGnm(PNGraph, 10, 30)
    G2 = ConvertGraph(PNEANet, G1)
    print "Edges List:\n"
    for EI in G2.Edges():
          print "edge: (%d, %d); edge id:%d" % (EI.GetSrcNId(), EI.GetDstNId(),G2.GetEId(EI.GetSrcNId(),EI.GetDstNId())) 
    print "--------------------------------------------------\n"
  
    #define integer attribute on the node
    G2.AddIntAttrN("NValInt", 0)
    
    
    global nList
    nList = []
    
    for NI in G2.Nodes():
        xList = findNeighborList(NI.GetId())
        nList.append([NI.GetId(),xList])

    for NI in G2.Nodes():
        uninfectedNodesList.append(NI.GetId())
    print "Uninfected Nodes List:"
    print uninfectedNodesList
    

def pull(rumor):
    infNCount = 0
    nOfRounds = 0
    infNCount = firstPush(55)
    print "Uninfected node list after first push:"
    print uninfectedNodesList
    print "Infected node number:%d\n"%(infNCount)

    while infNCount != G2.GetNodes():
        for NI in G2.Nodes():
            if NI.GetId() in uninfectedNodesList:
                print "Neighbor nodes of %d. node: "% NI.GetId()
                print nList[NI.GetId()][1]
                nval = G2.GetIntAttrDatN(NI.GetId(), "NValInt")
                randomEdge= random.choice(nList[NI.GetId()][1])
                print "Random neighbor node of %d. node  : %d\n" %(NI.GetId(), randomEdge)
                randomNVal = G2.GetIntAttrDatN(randomEdge, "NValInt")
                print "Random neigbor value: %d" %(randomNVal)
                if randomNVal > nval : 
                        print "Pull process executes...\n"
                        G2.AddIntAttrDatN(NI.GetId(), rumor, "NValInt")
                        postNodeVal = G2.GetIntAttrDatN(NI.GetId(), "NValInt") 
                        print "random neighbor value after pull process: %d\n" %(postNodeVal)
                        uninfectedNodesList.remove(NI.GetId())
                        print "Uninfected Nodes List:"
                        print uninfectedNodesList
                        infNCount += 1
                        printNodes()
                        #if infNCount == 10:
                         #   break
                      
                        #elif infNCount == 30:
                         #   break
                        #elif infNCount == 40:
                         #   break
                        #elif infNCount == 50:
                         #   break
                        #elif infNCount == 60:
                         #   break
                        #elif infNCount == 70:
                         #   break
                        #elif infNCount == 80:
                         #   break
                        #elif infNCount == 90:
                         #   break
                        
                else:
                        print "No need pull!\n" 
                       
                       
                
        nOfRounds += 1
        print "Infected Node Number: %d\n" %(infNCount)
        print "Number of rounds: %d\n" %(nOfRounds)
        print "--------------------------------------------------\n" 
        
        
       
            
def firstPush(rumor):
    
    infNCount = 0
    rNodeId = random.randint(0, (G2.GetNodes()-1))
    for NI in G2.Nodes():
        if NI.GetId() == rNodeId:
            print "Random node Id: %d\n" %(rNodeId)
            rNodeVal = G2.GetIntAttrDatN(NI.GetId(), "NValInt")
            G2.AddIntAttrDatN(NI.GetId(), rumor, "NValInt")
            rNodeVal = G2.GetIntAttrDatN(NI.GetId(), "NValInt")
            print "After giving rumor, new value of %d. node :%d\n"%(rNodeId, rNodeVal)
            infNCount += 1
            uninfectedNodesList.remove(NI.GetId())
    return infNCount
       
def findNeighborList(node):
    nbList = []
    for NI in G2.Nodes(): 
        if NI.GetId() == node:
            for eid in NI.GetOutEdges():
                nbList.append(eid)
    return nbList

def printNodes():                    
    print "--------------------------------------------------\n"
    print "After Pull Process:\n"
    print "--------------------------------------------------\n"
    for NI in G2.Nodes():
        nVal = G2.GetIntAttrDatN(NI.GetId(), "NValInt")
        print "Node Id: %d, Node Value: %d\n" % (NI.GetId(), nVal)
    print "--------------------------------------------------\n"
  
if __name__ == '__main__':
    graph()
    pull(55)
  

