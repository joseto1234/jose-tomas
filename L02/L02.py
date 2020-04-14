'ITEM 1'
import time


'PROBLEMA NUMERO 1.A (LISTAS)'


global zona
#creo variable global zona para usarla dentro de la funcion y que los valores no se reinicien
zona=[]

def superficie_de_nivel(mapa, celda):
    numero=mapa[celda[0]][celda[1]]
    lista_superficie=[]

    #agrega a la lista de superficie solo los valores vecinos a la celda que tengan valores igual a el de la celda
    if celda not in zona:
        zona.append(celda)
    if (celda[0]+1,celda[1]+1) not in zona and celda[0]+1 <= len(mapa)-1 and celda[1]+1<= len(mapa[0])-1:
        if mapa[celda[0]+1][celda[1]+1]==numero:
            lista_superficie.append((celda[0]+1,celda[1]+1))
    if (celda[0]+1,celda[1]) not in zona and celda[0]+1 <= len(mapa)-1:
        if mapa[celda[0]+1][celda[1]]==numero:
            lista_superficie.append((celda[0]+1,celda[1]))
    if (celda[0],celda[1]+1) not in zona and celda[1]+1<= len(mapa[0])-1:
        if mapa[celda[0]][celda[1]+1]==numero:
            lista_superficie.append((celda[0],celda[1]+1))
    if (celda[0]-1,celda[1]-1) not in zona and celda[0]-1 >= 0 and celda[1]-1 >= 0:
        if mapa[celda[0]-1][celda[1]-1]==numero:
            lista_superficie.append((celda[0]-1,celda[1]-1))
    if (celda[0],celda[1]-1) not in zona and celda[1]-1 >= 0:
        if mapa[celda[0]][celda[1]-1]==numero:
            lista_superficie.append((celda[0],celda[1]-1))
    if (celda[0]-1,celda[1]) not in zona and celda[0]-1 >= 0:
        if mapa[celda[0]-1][celda[1]]==numero:
            lista_superficie.append((celda[0]-1,celda[1]))
    if (celda[0]-1,celda[1]+1) not in zona and celda[1]+1 <= len(mapa[0])-1 and celda[0]-1 >= 0:
        if mapa[celda[0]-1][celda[1]+1]==numero:
            lista_superficie.append((celda[0]-1,celda[1]+1))
    if (celda[0]+1,celda[1]-1) not in zona and celda[0]+1<= len(mapa)-1 and celda[1]-1 >= 0:
        if mapa[celda[0]+1][celda[1]-1]==numero:
            lista_superficie.append((celda[0]+1,celda[1]-1))
    #para cada una de las posiciones vecinas a la celda que sean igual al valor de la celda,
    #revisar sus vecinos llamando nuevamente a la funcion
    for i in lista_superficie:
        superficie_de_nivel(mapa,i)

    zona.sort() #ordena la lista final
    return zona




#mapa=[[1,1,1,1],[1,2,4,4],[1,1,5,7]]
#celda=(1,0)
#celdas=superficie_de_nivel(mapa,celda)
#print(celdas)


'PROBLEMA NUMERO 1.B (DICCIONARIOS)'
import unidecode
def son_anagramas(string1,string2):
    dic1=dict()
    dic2=dict()
    string1=string1.lower()
    string2=string2.lower()
    string1=unidecode.unidecode(string1)
    string2=unidecode.unidecode(string2)
    todas_las_letras_calzan=True
    t1=time.time()
    for s in range(len(string1)):
        if dic1.get(string1[s],False)==False:
            dic1[string1[s]]=1
        elif dic1.get(string1[s],False)!=False:
            dic1[string1[s]]+=1

        if dic2.get(string2[s],False)==False:
            dic2[string2[s]]=1
        elif dic2.get(string2[s],False)!=False:
            dic2[string2[s]]+=1
    t2=time.time()
    print(t2-t1)
    t3=time.time()

    for j in dic2:
        for i in dic1:
            if dic1[i]!=dic2.get(i,'no'):
                    todas_las_letras_calzan=False
            if dic2[j]!=dic1.get(j,'no'):
                    todas_las_letras_calzan=False
    t4=time.time()
    print(t4-t3)
    return todas_las_letras_calzan



#string1='solucion'
#string2='oclusion'
#s=son_anagramas(string1,string2)
#print(s)




'ITEM 2'

'PROBLEMA NUMERO 2.A (LISTAS)'

def nuevo_muro(muro):
    muro_actual=[]
    muro_a=[]
    estado_a1=''
    estado_a2=''

    for i in range(len(muro)):
        if i==0:
                    muro_a.append(muro[i])
        elif i!=len(muro)-1:
            if muro[i]!=muro[i-1]:
                if i==1:
                    muro_a.append(muro[i])
                    if muro[i]<muro[i-1]:
                        estado_a1='bajando'
                        if muro[i+1]>muro[i]:
                            muro_actual=muro_a
                            muro_a=[]
                            muro_a.append(muro[i])
                            estado_a2='subiendo'
                        elif muro[i+1]>muro[i]:
                            estado_a2='bajando'
                    elif muro[i]>muro[i-1]:
                        estado_a1='subiendo'
                        if muro[i+1]>muro[i]:
                            estado_a2='subiendo'
                        elif muro[i+1]<muro[i]:
                            estado_a2='bajando'
                    elif muro[i]==muro[i-1]:
                        muro_a.pop()
                elif i!=0 and i!=1:
                    if estado_a1=='bajando' and estado_a2=='bajando':
                        muro_a.append(muro[i])
                        estado_a1='bajando'
                        if muro[i]<muro[i+1]:
                            estado_a2="subiendo"
                            if len(muro_a)>len(muro_actual):
                                muro_actual=muro_a
                                muro_a=[]
                                muro_a.append(muro[i])
                            elif len(muro_a)<=len(muro_actual):
                                muro_a=[]
                                muro_a.append(muro[i])
                    elif estado_a1=='subiendo' and estado_a2=='subiendo':
                        muro_a.append(muro[i])
                        estado_a1='subiendo'
                        if muro[i]>muro[i+1]:
                            estado_a2='bajando'
                    elif estado_a1=='subiendo' and estado_a2=='bajando':
                        muro_a.append(muro[i])
                        estado_a1='bajando'
                        if muro[i]<muro[i+1]:
                            estado_a2='subiendo'
                            if len(muro_a)>len(muro_actual):
                                muro_actual=muro_a
                                muro_a=[]
                                muro_a.append(muro[i])
                            elif len(muro_a)<=len(muro_actual):
                                muro_a=[]
                                muro_a.append(muro[i])
                    elif estado_a1=='bajando' and estado_a2=='subiendo':
                        muro_a.append(muro[i])
                        estado_a1='subiendo'
                        if muro[i]>muro[i+1]:
                            estado_a2="bajando"
            elif muro[i]==muro[i-1]:
                print('aqui')
                print(muro[i])
                if len(muro_a)>len(muro_actual):
                    muro_actual=muro_a
                    muro_a=[]
                    muro_a.append(muro[i])
                elif len(muro_a)<=len(muro_actual):
                    muro_a=[]
                    muro_a.append(muro[i])
                if muro[i]>muro[i+1]:
                    estado_a1="bajando"
                    estado_a2="bajando"
                elif muro[i]<muro[i+1]:
                    estado_a1="subiendo"
                    estado_a2="subiendo"
        elif i==len(muro)-1:
                if estado_a1=='subiendo':
                    muro_a.append(muro[i])
                    if len(muro_a)>len(muro_actual):
                            muro_actual=muro_a
                elif estado_a1=='bajando' and estado_a2=='bajando':
                    muro_a.append(muro[i])
                    if len(muro_a)>len(muro_actual):
                            muro_actual=muro_a
    return muro_actual




#muro_actual=[4,6,9,5,6,10,11,9,6,4,5]
#nuevo_muro=nuevo_muro(muro_actual)
#print(nuevo_muro)



'PROBLEMA NUMERO 2.B (LIBRE)'

class Nodo:
    def __init__(self,hoyos,n,k,N):
        self.n=n
        self.k=k
        self.hoyos=hoyos
        self.arco={}
        self.N=N

    def arcos(self):
        #crea un arco para cada nodo adyacente y su costo, si es agujero de gusano entonces costo es cero
        gusanos={}
        lista=[]
        for i in self.hoyos:
            gusanos[i[0]]=i[1]
        if gusanos.get(self.n,False)!=False:
            lista.append((gusanos.get(self.n,False),0))
        elif gusanos.get(self.n,False)==False:
            for j in range(self.k):
                if self.n+j+1<self.N+1:
                    lista.append((self.n+j+1,j+1))

        self.arco[self.n]=lista
        return self.arco

class Grafo:
    #se crea el grafo con cada nodo como objeto
    def __init__(self,H,K,N):
        self.H=H
        self.N=N
        self.K=K
        self.nodos={}
        for i in range(self.N+1):
            nodo=Nodo(self.H,i,self.K,self.N)
            nodo=nodo.arcos()
            self.nodos[i]=nodo[i]


def dijkstra(G, a, z):
    'sacado de: https://groups.google.com/forum/#!topic/tcomp-fich-unl/2lraAiZzc3c'
    """
    Algoritmo de Dijkstra

    Determina el camino mas corto entre los vertices 'a' y 'z' de un
    grafo ponderado y conexo 'G'.
    """
    assert a in G
    assert z in G

    # Definicion de infinito como un valor mayor
    # al doble de suma de todos los pesos
    Inf = 0
    for u in G:
        for v, w in G[u]:
            Inf += w

    # Inicializacion de estructuras auxiliares:
    #  L: diccionario vertice -> etiqueta
    #  S: conjunto de vertices con etiquetas temporales
    #  A: vertice -> vertice previo (en camino longitud minima)
    L = dict([(u, Inf) for u in G]) #py3: L = {u:Inf for u in G}
    L[a] = 0
    S = set([u for u in G]) #py3: S = {u for u in G}
    A = { }

    # Funcion auxiliar, dado un vertice retorna su etiqueta
    # se utiliza para encontrar el vertice the etiqueta minima
    def W(v):
        return L[v]
    # Iteracion principal del algoritmo de Dijkstra
    while z in S:
        u = min(S, key=W)
        S.discard(u)
        for v, w in G[u]:
            if v in S:
                if L[u] + w < L[v]:
                    L[v] = L[u] + w
                    A[v] = u

    # Reconstruccion del camino de longitud minima
    P = []
    u = z
    while u != a:
        P.append(u)
        u = A[u]
    P.append('a')
    P.reverse()

    # retorna longitud minima y camino de longitud minima
    return L[z]


def viajero_en_el_tiempo(hoyos_de_gusano, k, N):
    grafo1=Grafo(hoyos_de_gusano,k,N)
    a= dijkstra(grafo1.nodos,0,9)
    return (a)


#agujeros_de_gusano = [(1,7),(5,2),(8,0)]
#k=3
#N=9
#energia = viajero_en_el_tiempo(agujeros_de_gusano, k, N)
#print(energia)





'ITEM 3'

