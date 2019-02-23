import os, sys

os.environ["SUMO_HOME"] = "/usr/share/sumo/"
sys.path.insert(0, '/usr/share/sumo/')


if 'SUMO_HOME' in os.environ:
  tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
  sys.path.append(tools)
else:   
  sys.exit("please declare environment variable 'SUMO_HOME'")


import traci
import traci.constants as tc

ambulanceID = "ambulance"
abulanestate=False
targetID="4"

clear = lambda: os.system('clear')

###start ambulance dynamiclly after an accident occured
def startambulance():
  global abulanestate
  if abulanestate :
    return
  else:
    traci.route.add("trip", ["5672450#2", "156994961#1"])
    traci.vehicle.add("ambulance", "trip", typeID="type1")
    abulanestate=True


traci.start(["sumo-gui", "-c", "/usr/local/lib/python2.7/dist-packages/mininet_wifi-2.3-py2.7.egg/mn_wifi/sumo/data/map.sumocfg"])
#traci.vehicle.subscribe(vehID, (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
#print(traci.vehicle.getSubscriptionResults(vehID))

step=0
while(True):
  #print("step", step)
  traci.simulationStep()
  Vlist=traci.vehicle.getIDList()
  
  clear()
  #print(Vlist)
  if abulanestate :
    print("Ambulance is on the way.")
  else:
    print("Everything is OK.")
  if targetID in Vlist:
    traci.vehicle.setColor(targetID,(255,0,0))
    print("target :")
    print('\t speed: %.3f' % traci.vehicle.getSpeed(targetID))
    print('\t waiting %.3f: ' % traci.vehicle.getWaitingTime(targetID))
    print('\t isStopped %s' % traci.vehicle.isStopped(targetID))
    print('\t getStopState %s' % traci.vehicle.getStopState(targetID))
    if ( traci.vehicle.getStopState(targetID)==1):
      startambulance()

      

  if ambulanceID in Vlist:
    print('ambulance :')
    print('\t speed: %.3f' % traci.vehicle.getSpeed(ambulanceID))

  step=step+1
traci.close()
