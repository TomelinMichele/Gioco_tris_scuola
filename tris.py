#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum
import time

# Dati....

__author__= "Tomelin Michele,Luca Manini"
__email__ = "tomelinmichele@gmail.com"
__version__= "1.0"
__status__= "Beta"
__date__= "23/11/2019"

# Dove sono collegate le varie componenti??
# Controller dx= master = M
# Controller sx= master = E

# Definizione componenti
# mot= motore
# lamp= lampadina
# btn= bottone/tasto
# fot = fotocellula
# cal = Calamita

class MotorsCodes(Enum):
    mot_alz_dx = 1          # motore dx M
    mot_alz_sx = 2          # motore sx M
    mot_int = 3             # M
    mot_est = 4             # M

MOTORS = None      # will be set by init

class LampsCodes(Enum):
    lamp_rossa = 5          # E
    lamp_verde = 6          # E
    lamp_pareggio = 3       # arancio E
    lamp_vince_robot = 1    # bianca sx E
    lamp_vince_umano = 2    # bianca dx E

LAMPS = None       # will be set by init

class ButtonsCodes(Enum):
    btn_inizia_robot = 7       # M
    btn_inizia_umano = 8       # M
    btn_fine_corsa_alzata = 1 # in basso M
    btn_fine_corsa_rot_int_dx = 2 # M
    btn_fine_corsa_rot_int_sx = 3 # M
    btn_fine_corsa_rot_est_dx = 5 # M
    btn_fine_corsa_rot_est_sx = 4 # M

BUTTONS = None     # will be set by init

class PhotosCodes(Enum):
    photo_11 = 6 # M
    photo_12 = 7 # M
    photo_13 = 8 # M
    photo_21 = 1 # E
    photo_22 = 2 # E
    photo_23 = 3 # E
    photo_31 = 4 # E
    photo_32 = 5 # E
    photo_33 = 6 # E

PHOTOCELLS = None  # will be set by init

pc_codes_by_pos = {
    (1,1): PhotosCodes.photo_11,
    (1,2): PhotosCodes.photo_12,
    (1,3): PhotosCodes.photo_13,
    (2,1): PhotosCodes.photo_21,
    (2,2): PhotosCodes.photo_22,
    (2,3): PhotosCodes.photo_23,
    (3,1): PhotosCodes.photo_31,
    (3,2): PhotosCodes.photo_32,
    (3,3): PhotosCodes.photo_33,
}

def get_pc_by_pos(r,c):
    k = pc_codes_by_pos[(r,c)]
    return photocells[k]

calamita_code = 6 # E
CALAMITA = None   # will be set by init

robot_ha_vinto = False
umano_ha_vinto = False
pareggio = False

inizia_robot = False
inizia_umano = False

init_finita = False
nuova_partita = False
partita_finita = False

class GridStates(Enum):
    free = 1
    full = 2

cells_state = {(r,c): GridStates.free
              for r in range(3)
              for c in range(3)}

def is_pos_free(r, c):
    return grid_state[(r,c)] ==  GridStates.free

def set_pos_state(r, c, state):
    assert state in GridStates
    grid_state[(r,c)] = state

# Tempo di attesa finito il quale la mossa passa al giocatore
# successivo es: robot > umano e viceversa quando questo scade il
# giocatore successivo vince e la partita si conclude

turno_giocatore = 50

#Lampadina e motori ON_OFF
SPEED_ON = LEVEL_ON = 512
SPEED_OFF = LEVEL_OFF = 0

#Coordinate: posizioni scacchiera e scivolo le coordinate sono 3 :
  #impulsi rot1 = interna
  #impulsi rot2 = esterna
  #impulsi alzata sempre uguale apparte per lo scivolo

#TODO!! INIT_POS (sotto)
SCI_POS = (9,9)
INIT_POS =(10,10)
movement_dic = {
    (1,1): [1,2,3],  # (row, col):[rot_interna, rot_esterna, alzata]
    (1,2): [1,2,3],  # i, e, a = grid[(2,2)]
    (1,3): [1,2,3],
    (2,1): [1,2,3],
    (2,2): [1,2,3],
    (2,3): [1,2,3],
    (3,1): [1,2,3],
    (3,2): [1,2,3],
    (3,3): [1,2,3],
    SCI_POS: [5,5,5], # scivolo
    INIT_POS:[6,7,8], #posizione iniziale braccio
}

def get_movement(r, c):
    return movement_dic[(r, c)]

def accendi_lampadina(lamp):
    lamp.setLevel(LEVEL_ON)

def spegni_lampadina(lamp):
    lamp.setLevel(LEVEL_OFF)

def lampeggio_lampadina(lamp, lamp_max, sleep_time=0.5):
    # Questa funzione fa lampeggiare LAMP per LAMP_MAX volte ad
    # intervalli di SLEEP_TIME secondi.
    for _ in range(lamp_max):
        accendi_lampadina(lamp)
        time.sleep(sleep_time)
        spegni_lampadina(lamp)
        time.sleep(sleep_time)

def mot_off(m):
   m.stop()

def mot_on(m):
   m.setSpeed(SPEED_ON)

def muovi_to_row_col(r, c):
    i, e, a = get_movement(r,c)
    muovi_rot_to_pos(i, e, a)

def muovi_rot_to_pos(i, e, a):
    muovi_rot_int(i)
    muovi_rot_est(e)
    muovi_alzata(a)

def muovi_rot_int(i):
    # MUOVO ROT INTERNA TODO
    pass

def muovi_rot_est(i):
    # MUOVO ROT ESTERNA TODO
    pass

def muovi_alzata(i):
    # MUOVO ALZATA TODO
    pass

def attiva_calamita():
    calamita.setLevel(on)

def spegni_calamita():
    calamita.setLevel(off)

def prendi_pallina_dallo_scivolo():
    muovi_to_row_col(SCI_POS)
    attiva_calamita()

def posiziona_pallina(r, c):
    prendi_pallina_dallo_scivolo()
    muovi_to_row_col(r, c)
    spegni_calamita()
    set_pos_state(r, c, FULL)

def init():
    # emette un suono per segnalare l'inizio di questa fase
    # TODO

    import ftrobopy
    txt = ftrobopy.ftrobopy('auto')    # MASTER
    # txt2 = ftrobopy.ftrobopy('auto') EXTENSION
    
    global MOTORS
    MOTORS = {e:txt.motor(e.value) for e in MotorsCodes}

    global LAMPS
    LAMPS = {e:txt.output(e.value) for e in LampsCodes}

    global BUTTONS
    BUTTONS = {e:txt.input(e.value) for e in ButtonsCodes}

    global PHOTOCELLS
    PHOTOCELLS = {e:txt.input(e.value) for e in PhotosCodes}

    global CALAMITA
    CALAMITA = txt.output(calamita_code)

    return

    # all'inizio i motori sono spenti
    for o in MOTORS.items():
        mot_off(o)

    # comprende il posizionamento del braccio ???
    # TODO
    # mow_to_row_col(SCI_POS)

    # accensione e spegnimento lampadina per tot secondi
    for o in LAMPS.items():
        lampeggio_lampadina(o, 10)

    # finita questa fase il programma attende che l'utente inizi una
    # nuova partita...
    init_finita = True
def avvio_partita():
    #Controlla che qualcuno schiacci il pulsante del robot o dell'utente
    #per avviare una nuova partita
    if init_finita:
        if BUTTON[btn_inizia_robot].state () == 1:
            #INIZIA A GIOCARE TODO
            strategia()
        else:
            time.sleep(sleep_time)

def strategia():
    #TODO
    pass
def blocca_mossa_avversario():
    #TODO
    pass
def fai_la_tua_mossa():
    #TODO
    pass

def attendi_il_tuo_turno():
    time.sleep(turno_giocatore)
#--------------------- funzioni da usare dalla Cli per provare il braccio.. --------------------------------------------

def alza(value):
    #TODO
    print(f"Alza {value}")

def abbassa(value):
    #TODO
    print(f"Abbassa {value}")

def ruota_interno(value):
    #TODO
    print(f"Ruota interno {value}")

def ruota_esterno(value):
    #TODO
    print(f"Ruota esterno {value}")

def lamp_by_name(name):
    return LAMPS[LampsCodes[name]]

def motor_by_name(name):
    return MOTORS[MotorsCodes[name]]

def lamp(lamp, state):
    lamp = lamp_by_name(lamp)
    if state == "on":
        accendi_lampadina(lamp)
    else:
        spegni_lampadina(lamp)
#----------------------------------------------------------------------------------------
