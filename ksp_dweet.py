import pyksp
import dweepy  
import time


vessel=pyksp.WrappedVessel()
vessel.subscribe("vessel_altitude")
vessel.subscribe("vessel_mission_time")
vessel.subscribe("vessel_periapsis")
vessel.subscribe("vessel_apoapsis")
vessel.subscribe("resource_ec_current")
vessel.subscribe("resource_ec_max")
vessel.subscribe("vessel_body")

def truncate(n):
    try :
        n = round(n,1)
    except:
        n = n
    return n

def timec(n):
    try:
        m, s = divmod(n, 60)
        h, m = divmod(m, 60)
    except:
        h,m,s = 0,0,0
    return "%d:%02d:%02d" % (h, m, s)
    
vessel.start()
thingId = "kspksp_dweet_test"  
while 1:
    time.sleep(0.5)
    myDweet = {}
    
    vessel_altitude = truncate(vessel.vessel_altitude)
    vessel_periapsis = truncate(vessel.vessel_periapsis)
    vessel_apoapsis = truncate(vessel.vessel_apoapsis)
    vessel_time_to_periapsis = timec(vessel.vessel_time_to_periapsis)
    vessel_time_to_apoapsis = timec(vessel.vessel_time_to_apoapsis)
    vessel_mission_time = timec(vessel.vessel_mission_time)
    
    myDweet = {
               'Mission Time' : vessel_mission_time,
               'Vessel Body' : vessel.vessel_body,
               'Vessel Altitude' : vessel_altitude,
               'Vessel Periapsis' : vessel_periapsis,
               'Vessel Apoapsis' : vessel_apoapsis,
               'Time To Periapsis' : vessel_time_to_periapsis,
               'Time To Apoapsis' : vessel_time_to_apoapsis,
               'EletricCharge Current' : truncate(vessel.resource_ec_current),
               'EletricCharge Max' : truncate(vessel.resource_ec_max),
               }
    
    
    
    dweepy.dweet_for(thingId,myDweet)
    print 'Still working alright.'