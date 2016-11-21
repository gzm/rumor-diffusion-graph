# -*- coding: cp1254 -*-
from snap import *
import random
import sys
import math
import os

#random edge push-pull

def graph():
    global G2, edgeList, rNodeId, rEdge,infNCount,nOfRounds, nList
   
    nList = []
    G1 = GenRndGnm(PNGraph, 10, 30)
    G2 = ConvertGraph(PNEANet, G1)
    
    print "Edges List:\n"
    for EI in G2.Edges():
          print "edge: (%d, %d); edge id:%d\n" % (EI.GetSrcNId(), EI.GetDstNId(),G2.GetEId(EI.GetSrcNId(),EI.GetDstNId()))
    print "--------------------------------------------------\n"
  
    #define integer attribute on the node
    G2.AddIntAttrN("NValInt", 0)
    
    #Node-Neighbor List
    for NI in G2.Nodes():
        xList = findNeighborList(NI.GetId())
        nList.append([NI.GetId(),xList])
    #print "nList: %d" % (NI.GetId())

   
def pushPull(rumor):
    infNCount = 0
    nOfRounds = 0
    infNCount = firstPush(55)
    print "Number of infected node :%d\n"%(infNCount)
    while infNCount != G2.GetNodes():
        
        for NI in G2.Nodes():
            print "Neighbor list of %d. node: "%(NI.GetId())
            print nList[NI.GetId()][1]
            nval = G2.GetIntAttrDatN(NI.GetId(), "NValInt")
            randomEdge= random.choice(nList[NI.GetId()][1])
            print "Random neighbor of %d. node: %d\n" %(NI.GetId(),randomEdge)
            randomNVal = G2.GetIntAttrDatN(randomEdge, "NValInt")
            print "Random neigbor value: %d" %(randomNVal)  

            #push process    
            if nval > randomNVal:
                print "Push process executes!\n"
                G2.AddIntAttrDatN(randomEdge, rumor, "NValInt")
                      
                postNodeVal = G2.GetIntAttrDatN(randomEdge, "NValInt") 
                print "Source value after push process: %d\n" %(postNodeVal)
                        
                infNCount += 1
                printNodes()
                      
            #pull process
            elif nval < randomNVal:
                print "Pull process executes!\n"
                G2.AddIntAttrDatN(NI.GetId(), rumor, "NValInt")
                
                postNodeVal = G2.GetIntAttrDatN(NI.GetId(), "NValInt")
                print "Destination value after pull process: %d\n" %(postNodeVal)
                
                infNCount += 1
                printNodes()
               
            else:
                print "No need push or pull!\n"
            
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
    print "After Push-Pull Process:\n"
    print "--------------------------------------------------\n"
    for NI in G2.Nodes():
        nVal = G2.GetIntAttrDatN(NI.GetId(), "NValInt")
        print "Node Id: %d, Node Value: %d\n" % (NI.GetId(), nVal)
    print "--------------------------------------------------\n"
  
if __name__ == '__main__':
    graph()
    pushPull(55)
  
    

