#!/usr/bin/python
# -*- coding: utf-8 -*-

import ftrobopy
import time
import numpy

#Dati....

__author__= "Tomelin Michele,Luca Manini"
__email__ = "tomelinmichele@gmail.com"
__version__= "1.0"
__status__= "Sviluppamento"
__date__= "23/11/2019"

#Connessione al controller
USB = '192.168.7.2'
txt = ftrobopy.ftrobopy('auto')

# Dove sono collegate le varie componenti??
    #Controller dx= master = M
    #Controller sx= master = E
    
#Definizione componenti
    # mot= motore
    # lamp= lampadina
    # btn= bottone/tasto    
    # fot= fotocellula
    # cal= Calamita

mot_alz_dx=1 #motore dx M
mot_alz_sx=2 #motore sx M
mot_int= 3 # M
mot_est= 4 # M

lamp_rossa=5 # E
lamp_verde=6 # E
lamp_pareggio=3 #arancio E
lamp_vince_robot=1 #bianca sx E
lamp_vince_umano=2 #bianca dx E

btn_vince_robot=7 # M
btn_vince_umano=8 # M
btn_fine_corsa_alzata=1 #in basso M
btn_fine_corsa_rot_int_dx=2 # M
btn_fine_corsa_rot_int_sx=3 # M
btn_fine_corsa_rot_est_dx=5 # M
btn_fine_corsa_rot_est_sx=4 # M


fot_11= 6 # M
fot_12= 7 # M
fot_13= 8 # m
fot_21= 1 # E
fot_22= 2 # E
fot_23= 3 # E
fot_31= 4 # E
fot_32= 5 # E
fot_33= 6 # E

calamita= 6 # E

#Dichiarazione

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

fotocellula_pos11 = txt.input(fot_11)
fotocellula_pos12 = txt.input(fot_12)
fotocellula_pos13 = txt.input(fot_13)
fotocellula_pos21 = txt.input(fot_21)
fotocellula_pos22 = txt.input(fot_22)
fotocellula_pos23 = txt.input(fot_23)
fotocellula_pos31 = txt.input(fot_31)
fotocellula_pos32 = txt.input(fot_32)
fotocellula_pos33 = txt.input(fot_33)

calamita=txt.output(calamita)

#Variabili booleane

robot_ha_vinto=false
umano_ha_vinto=false
pareggio=false

inizia_robot=false
inizia_umano=false

init_finita= false
nuova_partita= false
partita_finita= false

posizioneDa11_a_13Libera=[false,false,false]
posizioneDa21_a_23Libera=[false,false,false]
posizioneDa31_a_33Libera=[false,false,false]


#Tempo di attesa finito il quale la mossa passa al giocatore successivo
#es: robot > umano e viceversa 
#quando questo scade il giocatore successivo vince e la partita si conclude

turno_giocatore= 50

#Lampadina e motori ON_OFF
on=512
off=0

#Coordinate: posizioni scacchiera e scivolo le coordinate sono 3 :
  #impulsi rot1 = interna
  #impulsi rot2 = esterna
  #impulsi alzata sempre uguale apparte per lo scivolo
    
scivoloPalline = [0,0] #manca impulsi alzata
posizione11 = [] posizione12 = [] posizione13 = []
posizione21 = [] posizione22 = [] posizione23 = []
posizione31 = [] posizione32 = [] posizione33 = []

#Implementazione funzioni

def accendiLampadina(lampadina l)
    l.setLevel(on)
    
def spegniLampadina(lampadina l)
    l.setLevel(off)
    
def lampeggioLampadina(lampadina l,lampeggi_max)
    #Questa funzione passatogli un numero di lampeggi massimo e la lampadina
    #fa lampeggiare quella lampadina n volte dove è il numero di lampeggi massimo
     n= lampeggi_max
    #inizio cliclo for...
    for i in n
        #ivocazione funzione
        accendiLampadina(l)
        #attesa
        time.sleep(0.5)
        spegniLampadina(l)
        time.sleep(0.5)
        
#----------------------------------------------------------------------------------------             

def motOff(motore m)
   #FERMO MOTORE
   m.stop()
    
def motOn(motore m)
   #ACCENDO MOTORE
   m.setSpeed(on) 
    
def muoviRotInt(impulsi i)
   #MUOVO ROT INTERNA (ancora da fare)
    
def muoviRotEst(impulsi i)
   #MUOVO ROT ESTERNA ( ancora da fare)
    
def muoviAlzata(impulsi i)
   #MUOVO ALZATA (ancora da fare)
    
#----------------------------------------------------------------------------------------             
    
def attivaCalamita()
    calamita.setLevel(on)

def spegniCalamita()
    calamita.setLevel(off)
    
#----------------------------------------------------------------------------------------             
    
def prendiPallinaDalloScivolo()
     #COMPRENDE IL POSIZIONAMENTO DEL BRACCIO (ancora da fare)
     #RACCOGLIMENTO PALLINA (ancora da fare)
     attivaCalamita()
#----------------------------------------------------------------------------------------   
def isPosOccupata(x [])
    return x []
#----------------------------------------------------------------------------------------  
def posizionaPallina()
     prendiPallinaDalloScivolo()
     #CONTROLLO CHE LA POS NON SIA OCCUPATA..
     if(!isPosOccupata())
        #SE "NO" POSIZIONAMENTO DEL BRACCIO (ancora da fare)
         #DEPOSITO PALLINA
         spegniCalamita()
         #POSIZIONE OCCUPATA (ancora da fare)       
         #CONTROLLO SE PARTITA FINITA (ancora da fare)
     #ALTRIMENTI SCELGO NUO POS
     elif()  
#----------------------------------------------------------------------------------------             
def init()
    #EMETTE UN SUONO PER SEGNALARE L'INIZIO DI QUESTA FASE
    
    #ALL'INIZIO I MOTORI SONO SPENTI
    motOff(motoreInterno)
    motOff(motoreEsterno)
    motOff(motoreAlzataDx)
    motOff(motoreAlzataSx)
    #COMPRENDE IL POSIZIONAMENTO DEL BRACCIO (ancora da fare)
    #ACCENSIONE E SPEGNIMENTO LAMPADINA PER TOT SECONDI
    lampeggioLampadina(lamp_rossa,10)
    lampeggioLampadina(lamp_verde,10)
    lampeggioLampadina(lamp_arancio,10)
    lampeggioLampadina(lamp_bianca1,10)
    lampeggioLampadina(lamp_bianca2,10)
    #FINITA QUESTA FASE IL PROGRAMMA ATTENDE CHE L'UTENTE INIZI UNA NUOVA PARTITA...
    init_finita= true
#----------------------------------------------------------------------------------------    
 def richiestNuovaPartita()  
    #( ancora da fare)
#----------------------------------------------------------------------------------------    
 def strategia() 
    #(ancora da fare)
#------------------------------inizio programma------------------------------------------            
