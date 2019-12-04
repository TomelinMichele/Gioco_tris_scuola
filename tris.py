#!/usr/bin/python
# -*- coding: utf-8 -*-

import ftrobopy
import time

#Dati....

__author__= "Tomelin Michele,Luca Manini"
__email__ = "tomelinmichele@gmail.com"
__version__= "1.0"
__status__= "Sviluppamento"
__date__= "23/11/2019"

# Dove sono collegate le varie componenti??
    #Controller dx= master = M
    #Controller sx= master = E
    
#Definizione componenti
    # mot= motore
    # lamp= lampadina
    # btn= bottone/tasto    
    # fot = fotocellula
    # cal = Calamita

mot_alz_dx = 1 #motore dx M
mot_alz_sx = 2 #motore sx M
mot_int = 3 # M
mot_est = 4 # M

lamp_rossa = 5 # E
lamp_verde = 6 # E
lamp_pareggio = 3 #arancio E
lamp_vince_robot = 1 #bianca sx E
lamp_vince_umano = 2 #bianca dx E

btn_vince_robot = 7 # M
btn_vince_umano = 8 # M
btn_fine_corsa_alzata = 1 #in basso M
btn_fine_corsa_rot_int_dx = 2 # M
btn_fine_corsa_rot_int_sx = 3 # M
btn_fine_corsa_rot_est_dx = 5 # M
btn_fine_corsa_rot_est_sx = 4 # M

fot_11 = 6 # M
fot_12 = 7 # M
fot_13 = 8 # m
fot_21 = 1 # E
fot_22 = 2 # E
fot_23 = 3 # E
fot_31 = 4 # E
fot_32 = 5 # E
fot_33 = 6 # E

calamita = 6 # E

# Dichiarazione

motoreInterno = txt.motor(mot_int)
motoreEsterno = txt.motor(mot_est)
motoreAlzataDx = txt.motor(mot_alz_dx)
motoreAlzataSx = txt.motor(mot_alz_sx)

btnAlzata = txt.input(btn_fine_corsa_alzata)
btnFCIntDx = txt.input(btn_fine_corsa_rot_int_dx)
btnFCIntSx = txt.input(btn_fine_corsa_rot_int_sx)
btnFCIEstDx = txt.input(btn_fine_corsa_rot_est_dx)
btnFCIEstSx = txt.input(btn_fine_corsa_rot_est_sx)

lamp_rossa = txt.ouput(lamp_rossa)
lamp_verde = txt.ouput(lamp_verde)
lamp_arancio = txt.ouput(lamp_arancio)
lamp_bianca1 = txt.ouput(lamp_bianca1)
lamp_bianca2 = txt.ouput(lamp_bianca2)

fotocellule = {
    (1,1): txt.input(fot_11),
    (1,2): txt.input(fot_12),
    (1,3): txt.input(fot_13),
    (2,1): txt.input(fot_21),
    (2,2): txt.input(fot_22),
    (2,3): txt.input(fot_23),
    (3,1): txt.input(fot_31),
    (3,2): txt.input(fot_32),
    (3,3): txt.input(fot_33),
}

calamita = txt.output(calamita)

#Variabili booleane

robot_ha_vinto = False
umano_ha_vinto = False
pareggio = False

inizia_robot = False
inizia_umano = False

init_finita = False
nuova_partita = False
partita_finita = False

ALL_STATES = FREE, FULL = 0, 1

grid_state = {(r,c): FREE
              for r in range(3)
              for c in range(3)}

def is_pos_free(r, c):
    return grid_state[(r,c)] =  =  FREE 

def set_pos_state(r, c, state):
    assert state in ALL_STATES
    grid_state[(r,c)] = state

# Tempo di attesa finito il quale la mossa passa al giocatore
# successivo es: robot > umano e viceversa quando questo scade il
# giocatore successivo vince e la partita si conclude

turno_giocatore = 50

#Lampadina e motori ON_OFF
on = 512
off = 0

#Coordinate: posizioni scacchiera e scivolo le coordinate sono 3 :
  #impulsi rot1 = interna
  #impulsi rot2 = esterna
  #impulsi alzata sempre uguale apparte per lo scivolo

SCI_POS = (9,9)
movement_dic = dict(
    (1,1): [1,2,3],  # (row, col):[rot_interna, rot_esterna, alzata]
    (1,2): [1,2,3],  # i, e, a = grid[(2,2)]
    (1,3): [1,2,3],
    (2,1): [1,2,3],
    (2,2): [1,2,3],
    (2,3): [1,2,3],
    (3,1): [1,2,3],
    (3,2): [1,2,3],
    (3,3): [1,2,3],
    SCI_POS: [5,5,5],) # scivolo

def get_movement(r, c):
    return movement_dic[(r, c)]

#Implementazione funzioni

def accendi_lampadina(lamp):
    lamp.setLevel(on)
    
def spegni_lampadina(lamp):
    lamp.setLevel(off)
    
def lampeggio_lampadina(lamp, lamp_max, sleep_time=0.5):
    # Questa funzione passatogli un numero di lampeggi massimo e la
    # lampadina fa lampeggiare quella lampadina n volte dove è il
    # numero di lampeggi massimo
    for _ in range(lamp_max):
        accendi_lampadina(lamp)
        time.sleep(sleep_time)
        spegni_lampadina(lamp)
        time.sleep(sleep_time)
        
def motOff(m):
   m.stop()
    
def motOn(m):
   m.setSpeed(on) 

def muovi_to_row_col(r, c):
    i, e, a = get_movement(r,c)
    muovi_rot_to_pos(i, e, a)
    
def muovi_rot_to_pos(i, e, a):
    muovi_rot_int(i)
    muovi_rot_est(e)
    muovi_alzata(a)
    
def muovi_rot_int(i):
    # MUOVO ROT INTERNA (ancora da fare)
    pass
    
def muovi_rot_est(i):
    # MUOVO ROT ESTERNA ( ancora da fare)
    pass
    
def muovi_alzata(i):
    # MUOVO ALZATA (ancora da fare)
    pass
    
#----------------------------------------------------------------------------------------             
    
def attiva_calamita():
    calamita.setLevel(on)

def spegni_calamita():
    calamita.setLevel(off)
    
#----------------------------------------------------------------------------------------             
    
def prendi_pallina_dallo_scivolo():
    muovi_to_row_col(SCI_POS)
    attiva_calamita()
    
def posiziona_pallina(r, c):
    prendi_pallina_dallo_scivolo()
    muovi_to_row_col(r, c)
    spegni_calamita()
    set_pos_state(r, c, FULL)

def init():
    # Connessione al controller
    txt = ftrobopy.ftrobopy('auto')

    # emette un suono per segnalare l'inizio di questa fase
    # TODO
    
    # all'inizio i motori sono spenti
    for o in (motoreInterno, motoreEsterno, motoreAlzataDx, motoreAlzataSx):
        motOff(o)
    
    # comprende il posizionamento del braccio
    # TODO
    
    # accensione e spegnimento lampadina per tot secondi
    for o in (lamp_rossa, lamp_verde, lamp_arancio, lamp_bianca1, lamp_bianca2):
        lampeggioLampadina(o, 10)
    
    # finita questa fase il programma attende che l'utente inizi una nuova partita...
    init_finita = true
    
def richiestNuovaPartita():
    #( ancora da fare)
    pass

def strategia():
    #(ancora da fare)
    pass
-----------------------------inizio programma------------------------------------------            
