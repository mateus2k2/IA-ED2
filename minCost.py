import random


def getCostVertice(node):
    # return node.cost
    return 1

def minCost(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira=[]
    nosVisitados=[]
    fronteira.append(inicio)
    
    minCostPath={}

    while fronteira !=[]:
        vertice=min(fronteira, key=lambda x: getCostVertice(x))
        fronteira.remove(vertice)
        nosVisitados.append(vertice)

        if vertice == labirinto._goal:
            print("objetivo encontrado")
            break

        movimentos=["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d]==True:
                if d=='E':
                    vizinho=(vertice[0],vertice[1]+1)
                if d=='W':
                    vizinho=(vertice[0],vertice[1]-1)
                if d=='N':
                    vizinho=(vertice[0]-1,vertice[1])
                if d=='S':
                    vizinho=(vertice[0]+1,vertice[1])
                
                if vizinho not in nosVisitados and vizinho not in fronteira:
                    fronteira.append(vizinho)
                    minCostPath[vizinho]=vertice
                

    fwdPath={}
    cell=labirinto._goal
    while cell != inicio:
        fwdPath[minCostPath[cell]]=cell
        cell=minCostPath[cell]
    return fwdPath