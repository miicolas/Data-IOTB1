from machine import Pin # importe dans le code la lib qui permet de gerer les Pin de sortie et d'entré
import utime # importe dans le code la lib qui permet de gerer le temps

led1 = Pin(1, mode=Pin.OUT)         
pin_button = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP) # declaration d'une variable de type pin ici la 14 
                                                    #et on prescise que c'est une pine d'entré de courant (IN)

while True: # boucle infini
    led1.off()
    print(pin_button.value()) # on envoie la valeur du bouton       
    if pin_button.value() == 1 :
        led1.off()
        
    if pin_button.value() == 0 :
        led1.on()
        
    

    




