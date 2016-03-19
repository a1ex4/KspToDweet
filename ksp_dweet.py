from __future__ import print_function
import pyksp
import dweepy  
import time
import requests
import os


requests.utils.DEFAULT_CA_BUNDLE_PATH = os.path.join(os.path.abspath('.'), 'cacert.pem')
# os.environ["REQUESTS_CA_BUNDLE"] = os.path.join(os.path.abspath('.'), 'cacert.pem')



vessel=pyksp.WrappedVessel()

vessel.subscribe("vessel_altitude")
vessel.subscribe("vessel_mission_time")
vessel.subscribe("vessel_periapsis")
vessel.subscribe("vessel_apoapsis")
vessel.subscribe("vessel_asl_height")
vessel.subscribe("terrain_height")
vessel.subscribe("vessel_name")

vessel.subscribe("vessel_vertical_speed")
vessel.subscribe("vessel_surface_speed")

vessel.subscribe("resource_ec_current")
vessel.subscribe("resource_ec_max")
vessel.subscribe("resource_ox_current")
vessel.subscribe("resource_ox_max")
vessel.subscribe("resource_mp_current")
vessel.subscribe("resource_mp_max")
vessel.subscribe("resource_lf_current")
vessel.subscribe("resource_lf_max")
vessel.subscribe("resource_sf_current")
vessel.subscribe("resource_sf_max")
vessel.subscribe("vessel_body")

vessel.start()

##

print ('##########################################')
print ('#                                        #')
print ('#  KSP To Mars Mission Control Software  #')
print ('#              by HeyYouNow              #')
print ('#                                        #')
print ('##########################################')
print ('\n')
print ('Dweet.io Thing Id : kspksp_dweet_test')
print ('Mission Control Dashboard @ https://supertramp.noho.st/site/')
print ('\n')

def truncate(n):
    if n is not None:
        n = round(n,1)

    return n

def timec(n):
    if n is not None:
        m, s = divmod(n, 60)
        h, m = divmod(m, 60)
    else:
        h,m,s = 0,0,0
    return "%d:%02d:%02d" % (h, m, s)
    
# vessel.start()
thingId = "kspksp_dweet_test"  
i =0
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
               'Vessel': {
                    'Vessel Name' : vessel.vessel_name,
                    'Mission Time' : vessel_mission_time,
                    'Vessel Body' : vessel.vessel_body,
                    'Vessel Altitude' : vessel_altitude,
                    'Altitude From Terrain' : truncate(vessel.vessel_asl_height),
                    # 'Terrain Height' : truncate(vessel.terrain_height),
                    'Surface Speed' : truncate(vessel.vessel_surface_speed),
                    'Vertical Speed' : truncate(vessel.vessel_vertical_speed),
                    }
                    
                'Orbit':{
                    'Vessel Periapsis' : vessel_periapsis,
                    'Vessel Apoapsis' : vessel_apoapsis,
                    'Time To Periapsis' : vessel_time_to_periapsis,
                    'Time To Apoapsis' : vessel_time_to_apoapsis,
                    }
                    
                'Resources':{
                    'EletricCharge Current' : truncate(vessel.resource_ec_current),
                    'EletricCharge Max' : truncate(vessel.resource_ec_max),
                    'Oxidizer Current' : truncate(vessel.resource_ox_current),
                    'Oxidizer Max' : truncate(vessel.resource_ox_max),
                    'MonoPropellant Current' : truncate(vessel.resource_mp_current),
                    'MonoPropellant Max' : truncate(vessel.resource_mp_max),
                    'LiquidFuel Current' : truncate(vessel.resource_lf_current),
                    'LiquidFuel Max' : truncate(vessel.resource_lf_max),
                    'SolidFuel Current' : truncate(vessel.resource_sf_current),
                    'SolidFuel Max' : truncate(vessel.resource_sf_max),
                    }
               
               
               }
    
    
    
    dweepy.dweet_for(thingId,myDweet)
    i += 1
    print ('\r'+'Still working alright, '+ str(i) + ' packets sent', end ='')