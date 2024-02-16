
import pyxel, time

class Labyrinthe():
    def __init__(self,vie):
        pyxel.init(128,128,fps=30)
        pyxel.load("theme.pyxres",True,False,False,False)
        self.vie_interne=vie
        self.perso=[False,False] # 1er bool si le personnage à l'explosif / 2ème bool si le personnages à poser l'explosif sur le socle
        self.perso_info=[19,105,13] # liste qui contient les coordonnées x et y du personnage et sa couleur.
        self.explo=[True,False] # 1er bool si l'explosif est sur le terrain / 2ème bool si l'explosif est sur le socle
        co=[(21,17),(85,111),(18,69),(67,18),(110,75),(110,33)] # liste des coordonnées de l'explosif
        entier=pyxel.rndi(0,5)
        self.co_explo=[co[entier][0],co[entier][1]] # liste qui contient les coordonnées x et y de l'explosif.
        self.socle_info=7 # couleur du socle
        self.minau=[True,0]
        pyxel.run(self.update,self.draw)

    def minautore(self):
        if int(self.perso_info[0])==self.co_minau[0] and int(self.perso_info[1])==self.co_minau[1]:
            self.vie_interne-=1
            self.perso_info[0]=19
            self.perso_info[1]=105
        if self.explo[1]==True and self.minau[0]==True:
            if self.co_minau[0]>51 and self.co_minau[0]<73 and self.co_minau[1]>57 and self.co_minau[1]<79:
                self.minau[0]=False
        if self.explo[1]==True and self.minau[0]==True:
            if not(self.co_minau[0]>51 and self.co_minau[0]<73 and self.co_minau[1]>57 and self.co_minau[1]<79):
                self.explo=[True,False]
                co=[(21,17),(85,111),(18,69),(67,18),(110,75),(110,33)]
                entier=pyxel.rndi(0,5)
                self.co_explo=[co[entier][0],co[entier][1]]

    def socle(self):
        if int(self.perso_info[0])==62 and int(self.perso_info[1])==68 and self.perso[0]==True:
            self.socle_info=8
            self.perso=[False,True]
            self.perso_info[2]=13

    def boutton(self):
        if int(self.perso_info[0])==108 and int(self.perso_info[1])==109 and self.perso[1]==True:
            self.socle_info=7
            self.explo[1]=True
            self.perso[1]=False

    def explosif(self):
        '''
            Regarde si le personnage et sur l'explosif.
        '''
        if int(self.perso_info[0])==self.co_explo[0] and int(self.perso_info[1])==self.co_explo[1]:
            self.co_explo=[1000,1000]
            self.explo[0]=False
            self.perso[0]=True
            self.perso_info[2]=14

    def mouvement(self):
        if pyxel.btn(pyxel.KEY_LEFT) and pyxel.pget(self.perso_info[0]-0.5,self.perso_info[1])!=2:
            self.perso_info[0]-=0.5
        if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.pget(self.perso_info[0]+0.5,self.perso_info[1])!=2:
            self.perso_info[0]+=0.5
        if pyxel.btn(pyxel.KEY_UP) and pyxel.pget(self.perso_info[0],self.perso_info[1]-0.5)!=2:
            self.perso_info[1]-=0.5
        if pyxel.btn(pyxel.KEY_DOWN) and pyxel.pget(self.perso_info[0],self.perso_info[1]+0.5)!=2:
            self.perso_info[1]+=0.5

    def update(self):
        '''
            Commande de déplacement du personnage.
        '''
        self.mouvement()
        #self.minautore()
        self.explosif()
        self.socle()
        self.boutton()

    def draw(self):
        '''
            Affichage.
        '''
        pyxel.cls(0)

        # fond
        for i in range(0,128,8):
            for j in range(0,128,8):
                pyxel.blt(i,j,0,i,j,8,8)

        pyxel.rect(108,109,1,1,10) # boutton
        pyxel.rect(62,68,1,1,self.socle_info) # socle
        pyxel.rect(self.co_explo[0],self.co_explo[1],1,1,8) # explosif
        if self.minau[0]==True:
            if self.minau[1]==0:
                pyxel.rect(61,72,1,1,3) # minautore
        pyxel.rect(self.perso_info[0],self.perso_info[1],1,1,self.perso_info[2]) # personnage
        if self.explo[1]==True:
            pyxel.rect(52,58,20,20,0)

Labyrinthe(12)