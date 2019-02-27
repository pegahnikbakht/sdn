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

targetID="4"
tractarget=""
oldtractarget=""
AST=0
TLP=0
ALP=0
ALI=0
PLI="PLI"
TLI="TLI"
clear = lambda: os.system('clear')


FORM={
  'HED' : '\033[95m',
  'BLU' : '\033[94m',
  'GRE' : '\033[92m',
  'ORG' : '\033[93m',
  'RED' : '\033[91m',
  'END' : '\033[0m',
  'BOL' : '\033[1m',
}

#def add_emergency_vehicle(typeI):
#    if typeI == "ambulance":
#       traci.route.add("trip", ["5672450#2", "156994961#1"])
#       traci.vehicle.add("ambulance", "trip", typeID="ambulance")
#    elif typeI == "firetruck": 
#       traci.route.add("trip", ["5672450#2", "156994961#1"])
#       traci.vehicle.add("firetruck", "trip", typeID="firetruck")
#    elif typeI == "police":
#       traci.route.add("trip", ["5672450#2", "156994961#1"])
#       traci.vehicle.add("police", "trip", typeID="police")


class ambulance():
    def set_vehicle(self):
        traci.route.add("trip", ["5672450#2", "156994961#1"])
        traci.vehicle.add("ambulance", "trip", typeID="ambulance")
      
class firetruck():
    def set_vehicle(self):
        traci.route.add("trip", ["5672450#2", "156994961#1"])
        traci.vehicle.add("firetruck", "trip", typeID="firetruck")

class police():
    def set_vehicle(self):
        traci.route.add("trip", ["5672450#2", "156994961#1"])
        traci.vehicle.add("police", "trip", typeID="police")

def emergency(obj):    
      obj.set_vehicle()

def startambulance(abulanestate,ast):
  if abulanestate :
    return abulanestate , "ambulance had started before"
  else:
    AST=ast
    if ast!=0 : emergency(ambulance())
    return True, "ambulance started"
    
    
    
def check_ambulance_arrival_time():
  global ALP,TLP,TLI,ALI
  TLPI,ALPI=int(TLP),int(ALP)
  if TLI==ALI and abs(TLPI-ALPI)<40 :
    return True
  else:
    return False


def print_target_info(targetID):
  try:
    print("target :")
    print('\t speed: %.3f' % traci.vehicle.getSpeed(targetID))
    print('\t waiting %.3f: ' % traci.vehicle.getWaitingTime(targetID))
    print('\t isStopped %s' % traci.vehicle.isStopped(targetID))
    print('\t StopState %s' % traci.vehicle.getStopState(targetID))
    print('\t Zoom %s' % traci.gui.getZoom( "View #0"))
    print('\t Schema %s' % traci.gui.getSchema( "View #0"))
    print('\t LaneID %s' % traci.vehicle.getLaneID( targetID))
    print('\t Position '+str( traci.vehicle.getPosition( targetID)))
    print('\t LanePosition '+str(traci.vehicle.getLanePosition( targetID )))
    return True
  except:
    return False


def print_ambulance_info(ambulanceID):
  try:
    print('\t speed: %.3f' % traci.vehicle.getSpeed(ambulanceID))
    print('\t LaneID %s' % traci.vehicle.getLaneID( ambulanceID)) 
    print('\t Position '+str( traci.vehicle.getPosition( ambulanceID)) )
    print('\t LanePosition '+str(traci.vehicle.getLanePosition( ambulanceID )))
    return True
  except:
    return False



def main():
  global oldtractarget,tractarget
  global ambulanceID ,targetID
  global AST,TLP,ALP,ALI,PLI,TLI
  abulanestate=False
  Done=False
  traci.start(["sumo-gui", "-c", "/usr/local/lib/python2.7/dist-packages/mininet_wifi-2.3-py2.7.egg/mn_wifi/sumo/data/map.sumocfg"])
  step=0
  traci.gui.setSchema( "View #0","real world")
  traci.gui.setZoom("View #0", 4000)
  while(~Done):
    traci.simulationStep()
    Vlist=traci.vehicle.getIDList()
    clear()
    if abulanestate :
      print ('{RED}Ambulance is on the way!{END}'.format(**FORM))
    else:
      print ('{GRE}Everything is OK{END}'.format(**FORM))
    print("CurrentTime")
    print(traci.simulation.getCurrentTime())
    if targetID in Vlist:  
      traci.vehicle.setColor(targetID,(255,0,0))
      print_target_info(targetID)
      TLI=traci.vehicle.getLaneID(targetID)
      TLP=traci.vehicle.getLanePosition( targetID ) 
      if ( traci.vehicle.getStopState(targetID)==1):
          abulanestate,_=startambulance(abulanestate,traci.simulation.getCurrentTime())
      tractarget=targetID
    if ambulanceID in Vlist: 
      print('{BOL}{RED}ambulance{END}:'.format(**FORM))
      print_ambulance_info(ambulanceID)
      ALI=traci.vehicle.getLaneID( ambulanceID)
      ALP=traci.vehicle.getLanePosition( ambulanceID)
      tractarget=ambulanceID
      Done=check_ambulance_arrival_time()
      if Done:
        print('{BOL}{GRE}ambulance is arrived{END}:'.format(**FORM))
        print('\t travel time is : '+str(traci.simulation.getCurrentTime() - AST) )
        print("mission done.")
        #traci.close()
        return True
    if tractarget!=oldtractarget:
      traci.gui.trackVehicle( "View #0", tractarget)
      oldtractarget=tractarget
    step=step+1
  


if __name__ == "__main__":
    main()
    


