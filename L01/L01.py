import random
import itertools


class Simulacion:

    def init(self):
        self.ciudad = []

    def inicializar_ciudad(self,m,n):
        self.ciudad = Ciudad(m,n)

    def poblar_ciudad(self, x = ''): #asigna personas a las diferentes celdas
        if x == '':
            for i in range(len(self.ciudad.zonas)):
                for j in range(len(self.ciudad.zonas[i])):
                    for k in range(14):
                        if k==0:
                            self.ciudad.zonas[i][j].append(int(i))
                        elif k==1:
                            self.ciudad.zonas[i][j].append(int(j))
                        else:
                            self.ciudad.zonas[i][j].append(int(random.normalvariate(3,1)))
        else:
            self.ciudad.zonas = x

        print("Zonas")
        for a in self.ciudad.zonas:
            print(a)
        print("")
        print("-----------------------------------------------------------------------")
        for i in range(len(self.ciudad.zonas)):
            for j in range(len(self.ciudad.zonas[i])):
                zona = Zona(self.ciudad.zonas[i][j][0],self.ciudad.zonas[i][j][1],self.ciudad.zonas[i][j][2],self.ciudad.zonas[i][j][3],self.ciudad.zonas[i][j][4],self.ciudad.zonas[i][j][5],self.ciudad.zonas[i][j][6],self.ciudad.zonas[i][j][7],self.ciudad.zonas[i][j][8],self.ciudad.zonas[i][j][9],self.ciudad.zonas[i][j][10],self.ciudad.zonas[i][j][11],self.ciudad.zonas[i][j][12],self.ciudad.zonas[i][j][13])
                self.ciudad.zonas[i][j] = zona

        #print("niños sin problemas en zona(1,2)")
        #print(self.ciudad.zonas[1][2].ninos_sin_prob)
        #print("niños sin problemas en zona(0,0)")
        #print(self.ciudad.zonas[0][0].ninos_sin_prob)

    def pacientes_cero(self,corona='',influenza=''): #recibe nada o dos ubicaciones falta poder iniciar paciente
        if corona!=('','') and influenza!=('',''):
            coronax=int(corona[0])
            coronay=int(corona[1])
            influenzax=int(influenza[0])
            influenzay=int(influenza[1])

            #Para el covid-19
            paciente_cero_corona = random.randint(0, len(self.ciudad.zonas[coronax][coronay].personas)-1)
            self.ciudad.zonas[coronax][coronay].personas[paciente_cero_corona].enfermarse_coronavirus()
            print("El paciente numero {} está contagiado por covid-19".format(paciente_cero_corona))
            self.ciudad.zonas[coronax][coronay].personas[paciente_cero_corona].tiempo_persona()

            #Para la influenza
            paciente_cero_influenza = random.randint(0, len(self.ciudad.zonas[influenzax][influenzay].personas)-1)
            self.ciudad.zonas[influenzax][influenzay].personas[paciente_cero_influenza].enfermarse_influenza()
            self.ciudad.zonas[influenzax][influenzay].personas[paciente_cero_influenza].tiempo_persona()
            print("El paciente numero {} está contagiado por influenza".format(paciente_cero_influenza))
            print("-----------------------------------------------------------------------")
        elif corona==('','') and influenza==('',''):
            a=0
            for i in range(len(self.ciudad.zonas)):
                a+=1
            coronax=random.randint(0, len(self.ciudad.zonas)-1)
            coronay=random.randint(0, a-1)
            influenzax=random.randint(0, len(self.ciudad.zonas)-1)
            influenzay=random.randint(0, a-1)

            #Para el covid-19
            paciente_cero_corona = random.randint(0, len(self.ciudad.zonas[coronax][coronay].personas)-1)
            self.ciudad.zonas[coronax][coronay].personas[paciente_cero_corona].enfermarse_coronavirus()
            print("El paciente numero {} de la zona ({},{}) está contagiado por covid-19".format(paciente_cero_corona,coronax,coronay))
            self.ciudad.zonas[coronax][coronay].personas[paciente_cero_corona].tiempo_persona()

            #Para la influenza
            paciente_cero_influenza = random.randint(0, len(self.ciudad.zonas[influenzax][influenzay].personas)-1)
            self.ciudad.zonas[influenzax][influenzay].personas[paciente_cero_influenza].enfermarse_influenza()
            self.ciudad.zonas[influenzax][influenzay].personas[paciente_cero_influenza].tiempo_persona()
            print("El paciente numero {} de la zona ({},{}) está contagiado por influenza".format(paciente_cero_influenza,influenzax,influenzay))
            #print(self.ciudad.zonas[influenzax][influenzay].personas[paciente_cero_influenza].id)
            #print(self.ciudad.zonas[influenzax][influenzay].personas[paciente_cero_influenza].coronavirus)
            #print(self.ciudad.zonas[influenzax][influenzay].personas[paciente_cero_influenza].influenza)
            print("-----------------------------------------------------------------------")

    def buscar_contagiados(self, zona_x, zona_y, corona=False, influenza=False):
        lista_contagiados = []
        if corona:
            if influenza:
                for persona in self.ciudad.zonas[zona_x][zona_y].personas:
                    if persona.coronavirus and persona.influenza:
                        lista_contagiados.append(persona)
            else:
                for persona in self.ciudad.zonas[zona_x][zona_y].personas:
                    if persona.coronavirus:
                        lista_contagiados.append(persona)
        elif influenza:
            for persona in self.ciudad.zonas[zona_x][zona_y].personas:
                    if persona.influenza:
                        lista_contagiados.append(persona)
        return lista_contagiados

    def normas_de_contagio_influenza(self):
        #print("LOS CASOS DE INFLUENZA EN LA CIUDAD SON:")
        print(" ")
        self.lista_contagiados_influenza=[]
        for i in range(len(self.ciudad.zonas)):
                for j in range(len(self.ciudad.zonas[i])):
                    self.lista_contagiados_influenza=self.buscar_contagiados(i,j,False,True)
                    p0=len(self.lista_contagiados_influenza)/len(self.ciudad.zonas[i][j].personas)
                    for persona in self.ciudad.zonas[i][j].personas:
                        if persona.influenza==False:
                            if persona.inmune_influenza==False:
                                if random.random()<=p0:
                                    #persona.contagiar(i,j,persona.id,False,True)
                                    persona.enfermarse_influenza()
                                    print("<se ha contagiado de influenza el paciente numero {}>".format(persona.id))
                                else:
                                    next
                    #print("lo infectados en la zona  ({},{}) son {} de {}".format(i,j,len(self.buscar_contagiados(i,j,False,True)),len(self.ciudad.zonas[i][j].personas)))
                    #print(" ")
        #print("-----------------------------------------------------------------------")

    def normas_de_contagio_corona(self):
        #print("LOS CASOS DE CORONAVIRUS EN LA CIUDAD SON:")
        print(" ")
        self.lista_contagiados_corona=[]
        for i in range(len(self.ciudad.zonas)):
                for j in range(len(self.ciudad.zonas[i])):
                    self.lista_contagiados_corona=self.buscar_contagiados(i,j,True,False)
                    p0=len(self.lista_contagiados_corona)/len(self.ciudad.zonas[i][j].personas)
                    for persona in self.ciudad.zonas[i][j].personas:
                        if persona.categoria=="nino" and persona.problema=="ninguno":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="nino" and persona.problema=="cardiaco":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*1.1:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="nino" and persona.problema=="respiratorio":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*1.1:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="nino" and persona.problema=="ambos":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*1.1*1.1:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*1.1:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next

                        elif persona.categoria=="adulto" and persona.problema=="ninguno":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*1.3:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.3:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="adulto" and persona.problema=="cardiaco":
                            if persona.inmune_corona==False:
                                if persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*2:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*2:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="adulto" and persona.problema=="respiratorio":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*2:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*2:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="adulto" and persona.problema=="ambos":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*2*1.1:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*2*1.1:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next

                        elif persona.categoria=="anciano" and persona.problema=="ninguno":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*1.5:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.5:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="anciano" and persona.problema=="cardiaco":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*2:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*2:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="anciano" and persona.problema=="respiratorio":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*3:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*3:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                        elif persona.categoria=="anciano" and persona.problema=="ambos":
                            if persona.inmune_corona==False:
                                if persona.influenza==True:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*1.1*4:
                                            #persona.contagiar(i,j,True,True)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next
                                elif persona.influenza==False:
                                    if persona.coronavirus==False:
                                        if random.random()<=p0*4:
                                            #persona.contagiar(i,j,True,False)
                                            persona.enfermarse_coronavirus()
                                            print("<se ha contagiado de coronavirus el paciente numero {}>".format(persona.id))
                                        else:
                                            next

                    #print("los infectados en la zona ({},{}) son {} de {}".format(i,j,len(self.buscar_contagiados(i,j,True,False)),len(self.ciudad.zonas[i][j].personas)))
                    #print(" ")
        print("-----------------------------------------------------------------------")


                    #p0=len(self.ciudad.zonas[zona_x][zona_y].persona[buscar_contagiados(zona_x,zona_y,False,True)])/len(self.ciudad.zonas[zona_x][zona_y].personas)
                    #print(p0)

    def normas_de_contagio_interzonas(self):
        for i in range(len(self.ciudad.zonas)):
            for j in range(len(self.ciudad.zonas[i])):
                p1=len(self.buscar_contagiados(i,j,False,True))/len(self.ciudad.zonas[i][j].personas)
                p0=len(self.buscar_contagiados(i,j,True,False))/len(self.ciudad.zonas[i][j].personas)

                #contagiar coronavirus entre zonas
                if p0 > 0.6:
                    if i==0 and i != len(self.ciudad.zonas)-1:
                        if j==0 and j!=len(self.ciudad.zonas[i])-1:
                            if 0.1 >= random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j+1].personas)-1)
                                if self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                        elif j==len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j-1].personas)-1)
                                if self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j-1))
                        elif j != 0 and j !=len(self.ciudad.zonas[i])-1:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j+1].personas)-1)
                                if self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j-1].personas)-1)
                                if self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                        elif j ==0 and j==len(self.ciudad.zonas[i])-1:
                            infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                            if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_corona==False:
                                self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))

                    elif i!=0 and i==len(self.ciudad.zonas)-1:
                        if j==len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j-1].personas)-1)
                                if self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j-1))
                        elif j==0 and j!=len(self.ciudad.zonas[i])-1:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j+1].personas)-1)
                                if self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                        elif j!=len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j+1].personas)-1)
                                if self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j-1].personas)-1)
                                if self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))

                    elif i!=0 and i!=len(self.ciudad.zonas)-1:
                        if j==0 and j!=len(self.ciudad.zonas[i])-1:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j+1].personas)-1)
                                if self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j+1].personas)-1)
                                if self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                        elif j==len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j-1].personas)-1)
                                if self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j-1].personas)-1)
                                if self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                        elif j!=len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j+1].personas)-1)
                                if self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j-1].personas)-1)
                                if self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j-1].personas)-1)
                                if self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j+1].personas)-1)
                                if self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].coronavirus==False and self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].inmune_corona==False:
                                    self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                    print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j+1))

                    elif i==0 and i==len(self.ciudad.zonas)-1:
                        if j==0 and j!=len(self.ciudad.zonas[i])-1:
                            infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                            if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_corona==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].coronavirus==False:
                                self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_coronavirus()
                                print('se ha infectado de coronavirus el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                        elif j==0 and j==len(self.ciudad.zonas[i])-1:
                            next

                #contagiar influenza entre zonas
                if p1 > 0.6:
                    if i==0 and i != len(self.ciudad.zonas)-1:
                        if j==0 and j!=len(self.ciudad.zonas[i])-1:
                            if 0.1 >= random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j+1].personas)-1)
                                if self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                        elif j==len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j-1].personas)-1)
                                if self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j-1))
                        elif j != 0 and j !=len(self.ciudad.zonas[i])-1:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j+1].personas)-1)
                                if self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j-1].personas)-1)
                                if self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                        elif j ==0 and j==len(self.ciudad.zonas[i])-1:
                            infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                            if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))

                    elif i!=0 and i==len(self.ciudad.zonas)-1:
                        if j==len(self.ciudad.zonas[i])-1:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j-1].personas)-1)
                                if self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j-1))
                        elif j==0 and j!=len(self.ciudad.zonas[i])-1:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j+1].personas)-1)
                                if self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                        elif j!=len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j+1].personas)-1)
                                if self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j-1].personas)-1)
                                if self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))

                    elif i!=0 and i!=len(self.ciudad.zonas)-1:
                        if j==0 and j!=len(self.ciudad.zonas[i])-1:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j+1].personas)-1)
                                if self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j+1].personas)-1)
                                if self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                        elif j==len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j-1].personas)-1)
                                if self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j-1].personas)-1)
                                if self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                        elif j!=len(self.ciudad.zonas[i])-1 and j!=0:
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j-1].personas)-1)
                                if self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                                if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j].personas)-1)
                                if self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j].personas)-1)
                                if self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j+1].personas)-1)
                                if self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j+1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i+1][j-1].personas)-1)
                                if self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i+1][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i+1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j-1].personas)-1)
                                if self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j-1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j-1))
                            if 0.1 >=random.random():
                                infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i-1][j+1].personas)-1)
                                if self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                    self.ciudad.zonas[i-1][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                    print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i-1,j+1))

                    elif i==0 and i==len(self.ciudad.zonas)-1:
                        if j==0 and j!=len(self.ciudad.zonas[i])-1:
                            infectado_otra_zona = random.randint(0, len(self.ciudad.zonas[i][j+1].personas)-1)
                            if self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].influenza==False and self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].inmune_influenza==False:
                                self.ciudad.zonas[i][j+1].personas[infectado_otra_zona].enfermarse_influenza()
                                print('se ha infectado el paciente {} de la zona ({},{})'.format(infectado_otra_zona,i,j+1))
                        elif j==0 and j==len(self.ciudad.zonas[i])-1:
                            next

    def descontagiar_personas(self):
        for i in range(len(self.ciudad.zonas)):
            for j in range(len(self.ciudad.zonas[i])):
                for k in range(len(self.ciudad.zonas[i][j].personas)):
                    if self.ciudad.zonas[i][j].personas[k].coronavirus ==True:
                        if self.ciudad.zonas[i][j].personas[k].inmune_corona==False:
                            self.ciudad.zonas[i][j].personas[k].tiempo_corona+=1
                    if self.ciudad.zonas[i][j].personas[k].influenza ==True:
                        if self.ciudad.zonas[i][j].personas[k].inmune_influenza==False:
                            self.ciudad.zonas[i][j].personas[k].tiempo_influ+=1
                    if self.ciudad.zonas[i][j].personas[k].tiempo_corona>=14:
                        self.ciudad.zonas[i][j].personas[k].sanarse_coronavirus()
                        print('se descontagio de coronavirus el paciente numero {} de la zona ({},{})'.format(self.ciudad.zonas[i][j].personas[k].id,i,j))
                    if self.ciudad.zonas[i][j].personas[k].tiempo_influ>=10:
                        self.ciudad.zonas[i][j].personas[k].sanarse_influenza()
                        print('se descontagio de influenza el paciente numero {} de la zona ({},{})'.format(self.ciudad.zonas[i][j].personas[k].id,i,j))

    def iniciar_tiempo(self,ti):
        for i in range(ti):
            print(' ')
            print(' ')
            print('DIA {}'.format(i+1))
            print("-----------------------------------------------------------------------")
            print('CONTAGIOS')
            self.normas_de_contagio_influenza()
            self.normas_de_contagio_corona()
            self.normas_de_contagio_interzonas()
            print('')
            print("-----------------------------------------------------------------------")
            print('DESCONTAGIOS')
            print('')
            self.descontagiar_personas()


            for j in range(len(self.ciudad.zonas)):
                for k in range(len(self.ciudad.zonas[j])):
                    ic=[]
                    ii=[]
                    for persona in self.ciudad.zonas[j][k].personas:
                        if persona.coronavirus==True:
                            ic.append(persona)
                    print("-----------------------------------------------------------------------")
                    print('ZONA ({},{}):'.format(j,k))
                    print("-----------------------------------------------------------------------")
                    print("los infectados de coronavirus son {} de {}".format(len(ic),len(self.ciudad.zonas[j][k].personas)))
                    print(' ')

                    for persona in self.ciudad.zonas[j][k].personas:
                        if persona.influenza==True:
                            ii.append(persona)
                    print("lo infectados de influenza son {} de {}".format(len(ii),len(self.ciudad.zonas[j][k].personas)))
                    print("-----------------------------------------------------------------------")
        print('FIN DE LA SIMULACION')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(('El estado final de la ciudad es:'))
        print(' ')
        print('[f,co, s, c, i, s, c, i, s, c, i, s, c, i, s, c, i, s, c, i, s, c, i, s, c, i, s, c, i, s, c, i, s, c, i, s, c, i]')
        print("------------------------------------------------------------------------------------------------------------------")
        self.guardar_ciudad()

    def guardar_ciudad(self):
        estado_ciudad=[]
        for i in range(len(self.ciudad.zonas)):
            for j in range(len(self.ciudad.zonas[i])):
                zonax=[]
                nsps=0
                npcs=0
                nprs=0
                naps=0
                asps=0
                apcs=0
                aprs=0
                aaps=0
                ansps=0
                anpcs=0
                anprs=0
                anaps=0
                nspc=0
                npcc=0
                nprc=0
                napc=0
                aspc=0
                apcc=0
                aprc=0
                aapc=0
                anspc=0
                anpcc=0
                anprc=0
                anapc=0
                nspi=0
                npci=0
                npri=0
                napi=0
                aspi=0
                apci=0
                apri=0
                aapi=0
                anspi=0
                anpci=0
                anpri=0
                anapi=0
                for persona in self.ciudad.zonas[i][j].personas:
                    if persona.categoria=="nino" and persona.problema=="ninguno":
                        if persona.coronavirus==False:
                            nsps+=1
                        if persona.coronavirus==True:
                            nspc+=1
                        if persona.influenza==True:
                            nspi+=1
                    elif persona.categoria=="nino" and persona.problema=="cardiaco":
                        if persona.coronavirus==False:
                            npcs+=1
                        if persona.coronavirus==True:
                            npcc+=1
                        if persona.influenza==True:
                            npci+=1
                    elif persona.categoria=="nino" and persona.problema=="respiratorio":
                        if persona.coronavirus==False:
                            nprs+=1
                        if persona.coronavirus==True:
                            nprc+=1
                        if persona.influenza==True:
                            npri+=1
                    elif persona.categoria=="nino" and persona.problema=="ambos":
                        if persona.coronavirus==False:
                            naps+=1
                        if persona.coronavirus==True:
                            napc+=1
                        if persona.influenza==True:
                            napi+=1
                    elif persona.categoria=="adulto" and persona.problema=="ninguno":
                        if persona.coronavirus==False:
                            asps+=1
                        if persona.coronavirus==True:
                            aspc+=1
                        if persona.influenza==True:
                            aspi+=1
                    elif persona.categoria=="adulto" and persona.problema=="cardiaco":
                        if persona.coronavirus==False:
                            apcs+=1
                        if persona.coronavirus==True:
                            apcc+=1
                        if persona.influenza==True:
                            apci+=1
                    elif persona.categoria=="adulto" and persona.problema=="respiratorio":
                        if persona.coronavirus==False:
                            aprs+=1
                        if persona.coronavirus==True:
                            aprc+=1
                        if persona.influenza==True:
                            apri+=1
                    elif persona.categoria=="adulto" and persona.problema=="ambos":
                        if persona.coronavirus==False:
                            aaps+=1
                        if persona.coronavirus==True:
                            aapc+=1
                        if persona.influenza==True:
                            aapi+=1
                    elif persona.categoria=="anciano" and persona.problema=="ninguno":
                        if persona.coronavirus==False:
                            ansps+=1
                        if persona.coronavirus==True:
                            anspc+=1
                        if persona.influenza==True:
                            anspi+=1
                    elif persona.categoria=="anciano" and persona.problema=="cardiaco":
                        if persona.coronavirus==False:
                            anpcs+=1
                        if persona.coronavirus==True:
                            anpcc+=1
                        if persona.influenza==True:
                            anpci+=1
                    elif persona.categoria=="anciano" and persona.problema=="respiratorio":
                        if persona.coronavirus==False:
                            anprs+=1
                        if persona.coronavirus==True:
                            anprc+=1
                        if persona.influenza==True:
                            anpri+=1
                    elif persona.categoria=="anciano" and persona.problema=="ambos":
                        if persona.coronavirus==False:
                            anaps+=1
                        if persona.coronavirus==True:
                            anapc+=1
                        if persona.influenza==True:
                            anapi+=1
                zonax.append(i)
                zonax.append(j)
                zonax.append(nsps)
                zonax.append(nspc)
                zonax.append(nspi)
                zonax.append(npcs)
                zonax.append(npcc)
                zonax.append(npci)
                zonax.append(nprs)
                zonax.append(nprc)
                zonax.append(npri)
                zonax.append(naps)
                zonax.append(napc)
                zonax.append(napi)
                zonax.append(asps)
                zonax.append(aspc)
                zonax.append(aspi)
                zonax.append(apcs)
                zonax.append(apcc)
                zonax.append(apci)
                zonax.append(aprs)
                zonax.append(aprc)
                zonax.append(apri)
                zonax.append(aaps)
                zonax.append(aapc)
                zonax.append(aapi)
                zonax.append(ansps)
                zonax.append(anspc)
                zonax.append(anspi)
                zonax.append(anpcs)
                zonax.append(anpcc)
                zonax.append(anpci)
                zonax.append(anprs)
                zonax.append(anprc)
                zonax.append(anpri)
                zonax.append(anaps)
                zonax.append(anapc)
                zonax.append(anapi)
                estado_ciudad.append(zonax)
                print(zonax)
        return estado_ciudad





class Ciudad:
    def __init__(self,m,n):
        self.zonas = []
        self.m = m
        self.n = n
        for i in range(m):
            self.zonas.append([])
            for j in range(n):
                self.zonas[i].append([])

class Zona:
    def __init__(self,fila,columna,ninos_sin_prob,ninos_prob_card,ninos_prob_resp,ninos_ambos_prob,adultos_sin_prob,adultos_prob_card,adultos_prob_resp,adultos_ambos_prob,ancianos_sin_prob,ancianos_prob_card,ancianos_prob_resp,ancianos_ambos_prob):
        self.fila = fila
        self.columna = columna
        self.ninos_sin_prob = ninos_sin_prob
        self.ninos_prob_card = ninos_prob_card
        self.ninos_prob_resp = ninos_prob_resp
        self.ninos_ambos_prob = ninos_ambos_prob
        self.adultos_sin_prob = adultos_sin_prob
        self.adultos_prob_card = adultos_prob_card
        self.adultos_prob_resp = adultos_prob_resp
        self.adultos_ambos_prob = adultos_ambos_prob
        self.ancianos_sin_prob = ancianos_sin_prob
        self.ancianos_prob_card = ancianos_prob_card
        self.ancianos_prob_resp = ancianos_prob_resp
        self.ancianos_ambos_prob = ancianos_ambos_prob
        self.personas = []
        self.crear_personas()

    def crear_personas(self):
        id_p = 0
        for i in range(0, self.ninos_sin_prob):
            persona = Persona()
            persona.categoria = 'nino'
            persona.problema = 'ninguno'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.ninos_prob_card):
            persona = Persona()
            persona.categoria = 'nino'
            persona.problema = 'cardiaco'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.ninos_prob_resp):
            persona = Persona()
            persona.categoria = 'nino'
            persona.problema = 'respiratorio'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.ninos_ambos_prob):
            persona = Persona()
            persona.categoria = 'nino'
            persona.problema = 'ambos'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.adultos_sin_prob):
            persona = Persona()
            persona.categoria = 'adulto'
            persona.problema = 'ninguno'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.adultos_prob_card):
            persona = Persona()
            persona.categoria = 'adulto'
            persona.problema = 'cardiaco'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.adultos_prob_resp):
            persona = Persona()
            persona.categoria = 'adulto'
            persona.problema = 'respiratorio'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.adultos_ambos_prob):
            persona = Persona()
            persona.categoria = 'adulto'
            persona.problema = 'ambos'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.ancianos_sin_prob):
            persona = Persona()
            persona.categoria = 'anciano'
            persona.problema = 'ninguno'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.ancianos_prob_card):
            persona = Persona()
            persona.categoria = 'anciano'
            persona.problema = 'cardiaco'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.ancianos_prob_resp):
            persona = Persona()
            persona.categoria = 'anciano'
            persona.problema = 'respiratorio'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

        for i in range(0, self.ancianos_ambos_prob):
            persona = Persona()
            persona.categoria = 'anciano'
            persona.problema = 'ambos'
            persona.id = id_p
            id_p += 1
            self.personas.append(persona)

class Persona:
    def __init__(self):
        self.coronavirus = False
        self.influenza = False
        self.categoria = ''
        self.problema = ''
        self.id = None
        self.tiempo_corona=0
        self.tiempo_influ=0
        self.inmune_corona=False
        self.inmune_influenza=False

    def enfermarse_coronavirus(self):
        if self.inmune_corona==False:
            self.coronavirus = True
        else:
            pass

    def sanarse_coronavirus(self):
        self.inmune_corona=True
        self.coronavirus = False

    def enfermarse_influenza(self):
        if self.inmune_influenza==False:
            self.influenza = True
        else:
            pass

    def sanarse_influenza(self):
        self.inmune_influenza=True
        self.influenza = False

    def tiempo_persona(self):
        if self.coronavirus ==True and self.influenza==False:
            if self.inmune_corona!=False:
                self.tiempo_corona+=1
                print('el paciente {} lleva {} dias enfermo cin coronavirus'.format(self.id,self.tiempo_corona))
        if self.influenza ==True and self.coronavirus==False:
            if self.inmune_influenza!=False:
                self.tiempo_influ+=1
                print('el paciente {} lleva {} dias enfermo con influenza'.format(self.id,self.tiempo_corona))
        if self.influenza == True and self.coronavirus == True:
            if self.inmune_corona!=False:
                self.tiempo_corona+=1
                print('el paciente {} lleva {} dias enfermo cin coronavirus'.format(self.id,self.tiempo_corona))




'probar automatico (apto para no pythonjupyter)'
print(' ')
print('Inserte numero de filas que desee para la ciudad')
fila=int(input())
print(' ')
print('Inserte numero de columnas que desee para la ciudad')
columna=int(input())
print(' ')
print('Inserte numero de fila en donde va a estar el paciente cero de coronavirus (si no quiere dar ubicación presione ENTER)')
coronavirusx=input()
print(' ')
print('Inserte numero de columna en donde va a estar el paciente cero de coronavirus (si no quiere dar ubicación presione ENTER)')
coronavirusy=input()
print(' ')
print('Inserte numero de fila en donde va a estar el paciente cero de coronavirus (si no quiere dar ubicación presione ENTER)')
influenzax=input()
print(' ')
print('Inserte numero de columna en donde va a estar el paciente cero de coronavirus (si no quiere dar ubicación presione ENTER)')
influenzay=input()

print('Inserte numero de dias que quiere simular')
dias=int(input())

simulacion=Simulacion()
simulacion.inicializar_ciudad(fila,columna)
simulacion.poblar_ciudad()
simulacion.pacientes_cero((coronavirusx,coronavirusy),(influenzax,influenzay))
simulacion.iniciar_tiempo(dias)

'prueba manual para python jupyter'
#simulacion=Simulacion()
#simulacion.inicializar_ciudad(3,3)
#simulacion.poblar_ciudad()
#simulacion.pacientes_cero((0,0),(1,1))
#simulacion.iniciar_tiempo(30)
