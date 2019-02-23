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


clear = lambda: os.system('clear')



ambulanceID = "9"

targetID="4"

traci.start(["sumo", "-c", "/usr/local/lib/python2.7/dist-packages/mininet_wifi-2.3-py2.7.egg/mn_wifi/sumo/data/map.sumocfg"])
#traci.vehicle.subscribe(vehID, (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
#print(traci.vehicle.getSubscriptionResults(vehID))

#Route an ambulance to accident spot

traci.route.add("trip", ["5672450#2", "156994961#1"])
traci.vehicle.add("newVeh", "trip", typeID="type1")

step=0
while(True):
  #print("step", step)
  traci.simulationStep()
  Vlist=traci.vehicle.getIDList()
  
  clear()
  print(Vlist)
  if targetID in Vlist:
    print("target :")
    print('\t speed: %.3f' % traci.vehicle.getSpeed(targetID))
    print('\t waiting %.3f: ' % traci.vehicle.getWaitingTime(targetID))
    print('\t isAtContainerStop %s' % traci.vehicle.isAtContainerStop(targetID))

  if targetID in Vlist:
    print('ambulance :')
    print('\t speed: %.3f' % traci.vehicle.getSpeed(ambulanceID))

  step=step+1
traci.close()
