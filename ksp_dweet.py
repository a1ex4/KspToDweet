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
    myDweet['Vessel Altitude'] = vessel_altitude
    
    vessel_periapsis = truncate(vessel.vessel_periapsis)
    myDweet['Vessel Periapsis'] = vessel_periapsis
    
    vessel_time_to_periapsis = timec(vessel.vessel_time_to_periapsis)
    myDweet['Time To Periapsis'] = vessel_time_to_periapsis
    
    vessel_time_to_apoapsis = timec(vessel.vessel_time_to_apoapsis)
    myDweet['Time To Apoapsis'] = vessel_time_to_apoapsis
    
    myDweet['EletricCharge Current'] = truncate(vessel.resource_ec_current)
    myDweet['EletricCharge Max'] = truncate(vessel.resource_ec_max)
    
    myDweet['Vessel Body'] = vessel.vessel_body

    
    dweepy.dweet_for(thingId,myDweet)
    print 'Still working alright.'
    # print vessel.vessel_altitude
    # print vessel.vessel_mission_time