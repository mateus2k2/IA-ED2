import math
import random

def heuristica(node0, node1):
    return math.sqrt((node0[0]-node1[0])**2 + (node0[1]-node1[1])**2)

def bestFirst(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira=[]
    nosVisitados=[]
    fronteira.append(inicio)
    
    best_first={}

    while fronteira !=[]:
        vertice=min(fronteira, key=lambda x: heuristica(x, labirinto._goal))
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
                    best_first[vizinho]=vertice
                

    fwdPath={}
    cell=labirinto._goal
    while cell != inicio:
        fwdPath[best_first[cell]]=cell
        cell=best_first[cell]
    return fwdPath