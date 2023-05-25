from pyamaze import maze, agent
from random import randint
from bfs import *
from dfs import *
from aStar import *
from bestFirst import *

def execucaoMaze(tamanho=30, possibilidadeCaminhos=100, algoritmo="dfs"):
    
    goalX, goalY = randint(1,tamanho), 1
    
    m=maze(tamanho,tamanho)
    m.CreateMaze(goalX, goalY, loopPercent=possibilidadeCaminhos)
    
    # Inclusao do agente no ambiente
    a=agent(m,footprints=True, shape="arrow")
    b=agent(m,footprints=True, color='red', filled=True)

    #m.run()
    
    # if algoritmo=="bfs":
    #     print("Executando a busca em largura")
    #     path1=bfs(m)
    #     path2=bfs(m)
    # elif algoritmo=="dfs":
    #     print("Executando a busca em profundidade")
    #     path1=dfs(m)
    #     path2=dfs(m)
    # elif algoritmo=="aStar":
    #     print("Executando a busca em profundidade")
    #     path1=aStar(m)
    #     path2=aStar(m)
    # elif algoritmo=="bestFirst":
    #     print("Executando a busca em profundidade")
    #     path1=bestFirst(m)
    #     path2=bestFirst(m)
    # else:
    #     path = m.path
    path1=aStar(m)
    path2=bestFirst(m)
    
    
    m.tracePath({a:path1, b:path2})
    m.run()


if __name__=='__main__':
    execucaoMaze(tamanho=20, algoritmo="bestFirst")