from naoqi import ALProxy
import time
import argparse
import sys
import threading
import math
from Maze_Finder import Maze_finder



def main(R_IP, R_PORT=9559):

    #Une liste pour stocker le trajet/chemin
    Le_chemin = list()


    # Creation des connections avec le robot NAO

    global tts
    global motion
    global memory
    global postureProxy
    try:
        tts = ALProxy("ALTextToSpeech", R_IP, R_PORT)
        motion = ALProxy("ALMotion", R_IP, R_PORT)    #Pour les mouvements
        memory = ALProxy("ALMemory", R_IP, R_PORT)    
        sonar = ALProxy("ALSonar", R_IP, R_PORT)      #Pour le Sonar de detection
        postureProxy = ALProxy("ALRobotPosture", R_IP, R_PORT)
    except BaseException as err:
        print(err)

 
    mf = Maze_finder(R_IP,R_PORT=9559)    #Creation d'une instance du classe Maze_finder
    
    #Initialisation du robot 
    motion.wakeUp()    #L'activation du Robot 
    postureProxy.goToPosture("Stand", 1.0) 
    postureProxy.goToPosture("StandInit", 1.0)
    motion.walkInit()
    time.sleep(2)
    mf.change_post(motion)     #Pour que le robot marche bien
    sonar.subscribe("myApplication")   #Activer le sonar de detection
    motion.setMoveArmsEnabled(True, True) #Activer le mouvement des bras
    motion.setFallManagerEnabled(True)

    #L'appele du fonction Desision pour trouver le chemin
    # et retouner le sous forme d'une liste
    Safe_distance = 0.15
    Obstacle_distance = 0.35
    Clear_chemin = 0.5

    Le_chemin = mf.Desision(memory ,motion, sonar,Obstacle_distance,Safe_distance,Clear_chemin)
    sonar.unsubscribe("myApplication")   #Desactiver le sonar de detection


if __name__ == "__main__":

    #Pour extracter les donnes appartir de terminal
    parser = argparse.ArgumentParser()
	
    parser.add_argument("--ip", type=str, default="192.168.3.142", help="Robot ip address")
	
    parser.add_argument("--port", type=int, default=9559, help="Robot port")
    args = parser.parse_args()
    main(args.ip, args.port)



