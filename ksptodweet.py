from Tkinter import * 
import os
import ttk
global thingID



def find_id():
    fenetre1 = Tk()
    
    label = Label(fenetre1, text="Dweet.io Thing Id:")
    label.grid(row=0, columnspan=2)
    
    value = StringVar() 
    entree = ttk.Entry(fenetre1, width=30)
    entree.grid(row=1, columnspan=2)
    def yolo():
        global thingID
        thingID = entree.get()
        fenetre1.destroy()
        print thingID
        
    bouton=ttk.Button(fenetre1, text="Done !", command=yolo)
    bouton.grid(row=2, column=1)
    
    
    rememberme = IntVar()
    case=ttk.Checkbutton(fenetre1, variable=rememberme, text="Remember this ?")
    case.grid(row=2, column=0)
    
    fenetre1.mainloop()

    if rememberme.get():
        print thingID
        config= open('settings', 'w')
        config.write(str(thingID))
        config.close()
    
    return thingID
    

if not os.path.isfile('settings'):
    thingID = find_id()
    
elif open('settings', 'r').readline() is '':

    thingID = find_id()
    open('settings', 'r').close()
else:
    config = open('settings', 'r')
    thingID = config.readline()
    config.close()
    
def dict_orbit():
    

def orbitWindow():
    global orbit
    orbit =Tk()
    orbitbFrame= Frame(orbit)
    orbitbFrame.pack()
    vessel_periapsis_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_periapsis_int, text='Vessel Periapsis').grid(row=0, column = 1)
    vessel_inclination_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_inclination_int, text='Vessel Inclination').grid(row = 0, column =2) 
    vessel_mean_anomaly_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_mean_anomaly_int, text='Vessel Mean Anomaly').grid(row = 0, column =3)
    vessel_eccentricity_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_eccentricity_int, text='Vessel Eccentricity').grid(row = 0, column =4) 
    vessel_time_to_periapsis_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_time_to_periapsis_int, text='Vessel Time To Periapsis').grid(row = 1, column =1) 
    vessel_true_anomaly_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_true_anomaly_int, text='Vessel True Anomaly').grid(row = 1, column =2) 
    vessel_longitude_ascending_node_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_longitude_ascending_node_int, text='Vessel Longitude Ascending Node').grid(row = 1, column =3)
    vessel_semimajor_axis_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_semimajor_axis_int, text='Vessel Semimajor Axis').grid(row = 1, column =4) 
    vessel_period_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_period_int, text='Vessel Period').grid(row = 2, column =1)
    vessel_argument_of_periapsis_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_argument_of_periapsis_int, text='Vessel Argument Of Periapsis').grid(row = 2, column =2) 
    vessel_time_to_apoapsis_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_time_to_apoapsis_int, text='Vessel Time To Apoapsis').grid(row = 2, column =3) 
    vessel_apoapsis_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_apoapsis_int, text='Vessel Apoapsis').grid(row = 2, column =4)
    vessel_transition_2_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_transition_2_int, text='Vessel Transition 2').grid(row = 3, column =2) 
    vessel_transition_1_int = IntVar() 
    ttk.Checkbutton(orbitbFrame, variable=vessel_transition_1_int, text='Vessel Transition 1').grid(row = 3, column =3)
    orbitc = Frame(orbit)
    orbitc.pack()
    ttk.Button(orbitc, text = 'Ok').pack()



main = Tk()

labelt = Label(main, text=thingID)
labelt.pack()

mainFrame = Frame(main,borderwidth=2, relief=GROOVE)
mainFrame.pack()

orbitFrame = Frame(mainFrame, borderwidth=2, relief=GROOVE)
vesselFrame = Frame(mainFrame, borderwidth=2, relief=GROOVE)
targetFrame = Frame(mainFrame, borderwidth=2, relief=GROOVE)
otherFrame = Frame(mainFrame, borderwidth=2, relief=GROOVE)

orbitFrame.grid(row =1, column = 1)
vesselFrame.grid(row =1, column = 2)
targetFrame.grid(row =1, column = 3)
otherFrame.grid(row =1, column = 4)

ttk.Button(orbitFrame, text="orbit", command=orbitWindow).pack(padx=10, pady=10)
main.mainloop()