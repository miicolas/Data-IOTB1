from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps


led1 = Pin(1, mode=Pin.OUT)                                 
led2 = Pin(5, mode=Pin.OUT)
led3 = Pin(9, mode=Pin.OUT)
led4 = Pin(13, mode=Pin.OUT)

while True:          # boucle infini
    
    led4.off()
    led1.on()# change l'etat de la led
    utime.sleep(0.5)
    led1.off()
    led2.on()# change l'etat de la led
    utime.sleep(0.5)
    led2.off()
    led3.on()# change l'etat de la led
    utime.sleep(0.5)
    led3.off()
    led4.on()        #allume la led
    utime.sleep(0.5)
    led4.off()


