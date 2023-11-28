from naoqi import ALProxy
import time
import argparse
import sys
import threading
import math



class Maze_finder(threading.Thread):

    def __init__(self,R_IP,R_PORT = 9559):
        threading.Thread.__init__(self)

        
    #Pour que le robot marche bien
    def change_post(self,motion):

    
        self.names = list()
    
        self.times = list()
    
        self.keys = list()
    
    
    
        self.names.append("HeadPitch")
    
        self.times.append([1.52])
    
        self.keys.append([[0.322098, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("HeadYaw")
    
        self.times.append([1.52])
    
        self.keys.append([[0.00916195, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LAnklePitch")
    
        self.times.append([1.52])
    
        self.keys.append([[-0.50311, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LAnkleRoll")
    
        self.times.append([1.52])
    
        self.keys.append([[0.00157595, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LElbowRoll")
    
        self.times.append([1.52])
    
        self.keys.append([[-1.49723, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LElbowYaw")
    
        self.times.append([1.52])
    
        self.keys.append([[-1.54776, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LHand")
    
        self.times.append([1.52])
    
        self.keys.append([[0.0108, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LHipPitch")
    
        self.times.append([1.52])
    
        self.keys.append([[-0.337522, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LHipRoll")
    
        self.times.append([1.52])
    
        self.keys.append([[-0.00924587, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LHipYawPitch")
    
        self.times.append([1.52])
    
        self.keys.append([[0.00464392, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LKneePitch")
    
        self.times.append([1.52])
    
        self.keys.append([[0.851412, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LShoulderPitch")
    
        self.times.append([1.52])
    
        self.keys.append([[1.94822, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LShoulderRoll")
    
        self.times.append([1.52])
    
        self.keys.append([[-0.162562, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("LWristYaw")
    
        self.times.append([1.52])
    
        self.keys.append([[0.131966, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RAnklePitch")
    
        self.times.append([1.52])
    
        self.keys.append([[-0.50311, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RAnkleRoll")
    
        self.times.append([1.52])
    
        self.keys.append([[-0.00157595, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RElbowRoll")
    
        self.times.append([1.52])
    
        self.keys.append([[1.49723, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RElbowYaw")
    
        self.times.append([1.52])
    
        self.keys.append([[1.54776, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RHand")
    
        self.times.append([1.52])
    
        self.keys.append([[0.0108, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RHipPitch")
    
        self.times.append([1.52])
    
        self.keys.append([[-0.337522, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RHipRoll")
    
        self.times.append([1.52])
    
        self.keys.append([[0.00924587, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RHipYawPitch")
    
        self.times.append([1.52])
    
        self.keys.append([[0.00464392, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RKneePitch")
    
        self.times.append([1.52])
    
        self.keys.append([[0.851412, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RShoulderPitch")
    
        self.times.append([1.52])
    
        self.keys.append([[1.94822, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RShoulderRoll")
    
        self.times.append([1.52])
    
        self.keys.append([[0.162562, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        self.names.append("RWristYaw")
    
        self.times.append([1.52])
    
        self.keys.append([[-0.131966, [3, -0.506667, 0], [3, 0, 0]]])
    
    
    
        motion.angleInterpolationBezier(self.names, self.times, self.keys)
    
    
    #LA fonction Securite()
    #Assurez-vous que le chemin est claire
    #Il prend comme parametres:
    #L_sonar,R_sonar: les mesures du sonar droite et gauche
    #Safe_distance: la distance de securite
    #motion: c'est l'instance d'une classe qui permet le mouvement de NAO
    def Securite(self,L_sonar, R_sonar,motion,Safe_distance):

        if L_sonar < Safe_distance or R_sonar < Safe_distance:
            motion.moveTo(-0.15, 0, 0, 0.0,[["MaxStepFrequency", 0.1], ["StepHeight", 0.06]])  #Deplacement en arriere avec 0.12 m
            print("Moving back")
   
   
    #LA fonction Evite_Obs_LR()
    #Assurez-vous qu'il n'y a pas un obstacle a droite oubien a gauche
    #angle: c'est l'angle de rotation (utilise pour connaitre le signe de l'angle)
    #L_sonar,R_sonar: les mesures du sonar droite et gauche
    #Safe_distance: la distance de securite
    #motion: c'est l'instance d'une classe qui permet le mouvement de NAO
    def Evite_Obs_LR(self,L_sonar,R_sonar,angle,motion):

        distance = 0.2  #Default valeur de deplacement a gauche ou a droite 
        Evite_valeur = 0.16 #Le min distance entre le robot et l'objet 
        Clear = 0.4     #Si la valeur de L-sonar ou R_sonar superieur a cette variable alors le chemin est clear pour ce cote 

        if L_sonar < Evite_valeur and R_sonar > Clear :
            if(angle > 0):  #Turn Right
                motion.moveTo(0, distance, 0,[["MaxStepFrequency", 0.1], ["StepHeight", 0.08]])
                print("Evite R")
                time.sleep(0.2)
            elif(angle < 0):  #Turn Left
                motion.moveTo(0, -distance, 0,[["MaxStepFrequency", 0.1], ["StepHeight", 0.08]])
                print("Evite R")
                time.sleep(0.2)

        else :
            if R_sonar < Evite_valeur and L_sonar > Clear :
                if(angle > 0):
                    motion.moveTo(0, distance, 0,[["MaxStepFrequency", 0.1], ["StepHeight", 0.08]])
                    print("Evite R")
                    time.sleep(0.2)
                elif(angle < 0):
                    motion.moveTo(0, -distance, 0,[["MaxStepFrequency", 0.1], ["StepHeight", 0.08]])
                    print("Evite R")
                    time.sleep(0.2)
    
    #LA fonction afficher_chemin() utiliser pour afficher le chemin 
    def afficher_chemin(self,chemin):
        print("")
        print("Chemin :")
        for i in chemin:
            print(i)

    #LA fonction Desision() c'est la fontion principale dans ce code
    # il fait l'appele a tous ces fonctions pour trouver un chemin entre l'entre et la sortie
    # poue cela il utilise l'algorithme de la main droite (Right Hand Algorithme) 
    # il retoune une liste (Pile) contenant le chemin a suiver sous forme de
    # "L" "R" "M" "S" "F" c'est a dire "Left Right Move Start Fin" 
    #Il prend comme parametres:
    #L_sonar,R_sonar: les mesures du sonar droite et gauche
    #Safe_distance: la distance de securite
    #sonar: c'est l'instance d'une classe qui permet de mesure la distance entre NAO et un objet
    #Obstacle_distance et clear_distance assure une distance de securite
    def Desision(self,memory ,motion, sonar,Obstacle_distance,Safe_distance,clear_chemin):
        

        chemin = list()     #La liste (Pile) pour stocker le trajet 
        chemin.append('s')              # marke le debut


        count = 0      #Pour conte le nombre des itterations    
        while(1):
            flag = 0
            count+=1
            print("[!] Debut ... count=",count)

            #place = 0
            #place2 = 0
            print("-----------------------")            

            print("Reading ...")
            
            #Calculer la distance entre les objets et le robot 
            L_sonar = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
            R_sonar = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
            
            #Ecrire les mesures dans le terminale
            print("Left :", L_sonar,"m")
            print("Right:", R_sonar,"m")
            print(" ")
            
            #Si count == 0 n'affiche pas le chemin car il est vide 
            if count != 0:
                self.afficher_chemin(chemin)
            
            #Prend une distance de securite avec les objects qui ont en avant du robot
            self.Securite(L_sonar,R_sonar,motion,Safe_distance)  
            #Afficher les mesures des sonseurs  
            self.Gyro(memory)
            


            if(L_sonar == 5.0 and R_sonar ==5.0):
                chemin.put('F')
                tts.say("j'ai trouver le chemin le plus bon")
                self.afficher_chemin(chemin)

                motion.stop()
                motion.rest()
                sonar.unsubscribe("myApplication")
                break

            if(L_sonar < Obstacle_distance and R_sonar < Obstacle_distance):   #S'il y a une obstacle en avant 
                angle = -(math.pi/2)   
                motion.moveTo(0.0, 0.0, angle, [["MaxStepFrequency", 0.1], ["StepHeight", 0.06]]) #Tourne droite
                chemin.append('R')
                flag = 1
                time.sleep(0.2)

                print("Move Right\n------------------")
            
                print("Left :", L_sonar,"m")
                print("Right:", R_sonar,"m")
                print("-----------------------")            
                print("Reading second time ..")
                print("-----------------------")            

                
                L_sonar = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
                R_sonar = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")

                if(L_sonar < Obstacle_distance and R_sonar < Obstacle_distance):  #Si obstacle touner a gauche
                    angle = math.pi/2
                    self.Securite(L_sonar, R_sonar,motion,Safe_distance)

                    motion.moveTo(0.0, 0.0, angle, [["MaxStepFrequency", 1.0], ["StepHeight", 0.06]])  #Tourne Gauche 
                    time.sleep(0.2)
                    self.Securite(L_sonar, R_sonar,motion,Safe_distance)

                    motion.moveTo(0.0, 0.0, angle, [["MaxStepFrequency", 1.0], ["StepHeight", 0.06]]) #Tourne Gauche 
                    time.sleep(0.2)

                    flag = 0    
                    self.change_post(motion)
                    
                    
                    print("-----------------------")            
                    print("turn 180")
                    print("-----------------------")            

                    
                    print("Left :", L_sonar,"m")
                    print("Right:", R_sonar,"m")
                    print(" \n")

                 # trouver un rondpoint
                   
                    print("-----------------------")            
                    print("Reading third time ...\n")
                    print("-----------------------")            


                    L_sonar = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
                    R_sonar = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")

                    if(L_sonar < Obstacle_distance and R_sonar < Obstacle_distance):
                        angle = (math.radians(90))
                        self.Securite(L_sonar,R_sonar,motion,Safe_distance)    
                        motion.moveTo(0.0, 0.0, angle, [["MaxStepFrequency", 0.1], ["StepHeight", 0.06]]) #Tourner Gauche
                        place = self.retoure(chemin,memory,motion,Safe_distance)
                        if(place != 0):
                            if(place == 'R'):    #Si il y a "R" alors que si il toune a droite il va trouver un impasse (dead-end)
                                chemin.append('L') # Donc ajouter "L" pour tourne a gauche 
                                place = 0
                            else:
                                if(place == 'L'):  #Si il y a "L" alors on a tester "R" et on a trouver un impasse 
                                                   # puis on tester "L" gauche et on a trouver un autre impasse 
                                                   # puisque on tourner a droite d'apres notre algorithme alor on va re-faire le teste 
                                    palce2= self.retoure()
                                    if(place2 == 'R'):
                                        chemin.append('L')
                                        place2 = 0 
                                    
                                    
                        else:
                            chemin.append('L')
                        
                                        
                        time.sleep(0.2)
                        print("-----------------------")            
                        print("Move Left")
                        print("-----------------------")            

                        print("Left :", L_sonar,"m")
                        print("Right:", R_sonar,"m")
                        print(" \n")
                        continue
                        
                    else: #Si il n'y a pas des obstacles deplacer en avant
                        print("----------------------")
                        print("Reading Else1 ...\n ")
                        print("-----------------------")

                        L_sonar = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
                        R_sonar = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
                        
                        print("Left :", L_sonar,"m")
                        print("Right:", R_sonar,"m")
                        print("-------------------")
                        print("Moving 1")
                        print("-------------------")
                        
                        self.Evite_Obs_LR(L_sonar,R_sonar,angle,motion)
                        self.Securite(L_sonar,R_sonar,motion,Safe_distance)    
                        self.Move(L_sonar,R_sonar,motion,chemin)
                        continue
                else:  #Si il n'y a pas des obstacles deplacer en avant
                    print("--------------------")
                    print("Reading Else2 ....")
                    print("---------------------")

                    L_sonar = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
                    R_sonar = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
                    
                    print("Left :", L_sonar,"m")
                    print("Right:", R_sonar,"m")
                    print("------------------")
                    print("Moving 2")
                    print("-------------------")
                    self.Evite_Obs_LR(L_sonar,R_sonar,angle,motion)
                    self.Securite(L_sonar,R_sonar,motion,Safe_distance)    
                    self.Move(L_sonar,R_sonar,motion,chemin)
                    continue
            else: #Si il n'y a pas des obstacles deplacer en avant
                  
                 #Toujour tester la Droite au debut  
                angle = -(math.radians(90))
                motion.moveTo(0, 0, angle, [["MaxStepFrequency", 0.1], ["StepHeight", 0.06]])
               
                print("---------------------")
                print("Reading Else3... \n")
                print("----------------------")
                L_sonar = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
                R_sonar = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
                
                print("Left :", L_sonar,"m")
                print("Right:", R_sonar,"m")
                print("-----------------")
                print(" ")
                
        
                if(L_sonar < Obstacle_distance and R_sonar < Obstacle_distance): #si il y un obstacle retourne l'emplacement initial
                    angle = (math.radians(90))
                    self.Securite(L_sonar,R_sonar,motion,Safe_distance)
                    #self.Evite_Obs_LR(L_sonar,R_sonar,angle,motion)    
                    motion.moveTo(0.0, 0.0, angle, [["MaxStepFrequency", 0.1], ["StepHeight", 0.06]])
                    time.sleep(0.2)
                    flag = 0
                    
                    self.Evite_Obs_LR(L_sonar,R_sonar,angle,motion)
                    self.Securite(L_sonar,R_sonar,motion,Safe_distance)    
                    self.Move(L_sonar,R_sonar,motion,chemin)

                else:  #si non avancer
                    if(flag):
                        time.sleep(0.2)
                        
                        self.Evite_Obs_LR(L_sonar,R_sonar,angle,motion)
                        self.Move(L_sonar,R_sonar,motion,chemin)
                    else:
                        angle = (math.radians(90))
                        self.Evite_Obs_LR(L_sonar,R_sonar,angle,motion)
                        self.Securite(L_sonar,R_sonar,motion,Safe_distance)    
                        motion.moveTo(0, 0, angle, [["MaxStepFrequency", 0.1], ["StepHeight", 0.06]])
                        time.sleep(0.2)
               

                    
                continue
          
            return chemin    
    
    #Cette fonction permet de re-organizer la liste qui contient 
    # le chemin dans le cas ou (repacer oubien un impasse) pour que 
    # le chemin soit reel et correct
    def retoure(self,chemin,memory,motion,Safe_distance):
        # supprimer jusqu'a trouve M
        valeur = chemin.pop()
        while(valeur != 'M'):
            valeur = chemin.pop()
        # marche jusqu'a trouver une branche
        while(valeur == 'M'):

            L_sonar = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
            R_sonar = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
            self.Securite(L_sonar, R_sonar,motion,Safe_distance)
            angle = 0.0
            motion.moveTo(0.4, 0.0, angle, [["MaxStepFrequency", 0.3], ["StepHeight", 0.04]])
            chemin.pop()
        return valeur  
    

    #Cette fonction permet le mouvement en avant 
    # chemin c'est la liste pour stocker les donnes concernant le trajet
    def Move(self,L_sonar, R_sonar,motion,chemin):

        angle = 0.0
        motion.moveTo(0.4, 0.0, angle, [["MaxStepFrequency", 0.3], ["StepHeight", 0.04]]) #Deplacer en avant 0.3m
        chemin.append('M')
        #print("Move1")
        print(L_sonar)
        print(R_sonar)
    
    #Cette fonction pour extracter les mesures de Gyroscope , l'accelerometre 
    #memooryProxy permet la connection avec les sonseurs  
    def Gyro(self,memoryProxy): 


        # Get the Gyrometers Values
        GyrX = memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyrX/Sensor/Value")
        GyrY = memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyrY/Sensor/Value")
        print("---------------------------------------------------")
        print ("Gyrometers value X: %.3f, Y: %.3f" % (GyrX, GyrY))
        print("---------------------------------------------------")
        # Get the Accelerometers Values
        AccX = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccX/Sensor/Value")
        AccY = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccY/Sensor/Value")
        AccZ = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccZ/Sensor/Value")
        print("---------------------------------------------------")
        print ("Accelerometers value X: %.3f, Y: %.3f, Z: %.3f" % (AccX, AccY,AccZ))
        print("---------------------------------------------------")
        # Get the Compute Torso Angle in radian
        TorsoAngleX = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AngleX/Sensor/Value")
        TorsoAngleY = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AngleY/Sensor/Value")
        print("---------------------------------------------------")
        print ("Torso Angles [radian] X: %.3f, Y: %.3f" % (TorsoAngleX, TorsoAngleY))
        print("---------------------------------------------------")
