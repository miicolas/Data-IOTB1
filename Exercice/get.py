import network   # import des fonctionnalités liées au WiFi
import urequests    # import des fonctionnalités liées aux requêtes HTTP
import utime    # import des fonctionnalités liées au temps
import ujson    # import des fonctionnalités liées à la conversion en JSON
from machine import Pin, PWM
import random

# Met la carte en mode client WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ip_address = wlan.ifconfig()[0]

print(ip_address)

# Informations de connexion WiFi
ssid = 'Nicolas B iPhone'
password = 'Nicolas78'
wlan.connect(ssid, password)

# Liste des identifiants de personnage
id_personnages = ['4c7e6819-a91a-45b2-a454-f931e4a7cce3', 'd5c4daa3-c726-426a-aa98-fb40f3fba816', '861c4cde-2f0f-4796-8d8f-9492e74b2573', '1cd6dc64-01a9-4379-9cfd-1a7167ba1bb1', '8f9aa40b-5d7c-441e-ad32-4564ecda3b70', 'af95bd8a-dfae-45bb-bc69-533860d34129', 'e32dd37c-91cd-4950-8ef2-e2ba1b87bd75']

# Dictionnaire des maisons de Poudlard avec les valeurs de LED correspondantes [Rouge, Vert, Bleu]
maisons_poudlard = { 
    "Gryffindor": [30000, 5, 5],
    "Slytherin": [5, 30000, 5],
    "Ravenclaw": [5, 5, 30000],
    "Hufflepuff": [30000, 30000, 5]
}

# Configuration des broches pour les LEDs RGB
pwm_ledR = PWM(Pin(13, mode=Pin.OUT))
pwm_ledR.freq(1_000)
pwm_ledG = PWM(Pin(14, mode=Pin.OUT))
pwm_ledG.freq(1_000)
pwm_ledB = PWM(Pin(15, mode=Pin.OUT))
pwm_ledB.freq(1_000)

# Attente de la connexion au réseau WiFi
while not wlan.isconnected():
    print("Pas connecté au réseau WiFi...")
    utime.sleep(1)

# Boucle principale
while True:
    try:
        # Sélection aléatoire d'un identifiant de personnage
        id_personnage = random.choice(id_personnages)
        
        # Construction de l'URL de l'API avec l'identifiant du personnage
        url = "https://hp-api.onrender.com/api/character/" + id_personnage
        
        # Requête GET pour obtenir les informations sur le personnage
        reponse = urequests.get(url)
        
        # Extraction du nom du personnage et de sa maison à partir de la réponse JSON
        nom_personnage = reponse.json()[0]["name"]
        maison = reponse.json()[0]["house"]
        
        # Fermeture de la requête
        reponse.close()
        
        # Affichage du nom du personnage et de sa maison
        print("Nom du personnage:", nom_personnage)
        print("Maison:", maison)
        
        # Attribution des valeurs de LED correspondantes à la maison
        pwm_ledR.duty_u16(maisons_poudlard[maison][0])
        pwm_ledG.duty_u16(maisons_poudlard[maison][1])
        pwm_ledB.duty_u16(maisons_poudlard[maison][2])
        
        # Attente avant de réinitialiser les LEDs
        utime.sleep(2)
        
        # Réinitialisation des LEDs
        pwm_ledR.duty_u16(0)
        pwm_ledG.duty_u16(0)
        pwm_ledB.duty_u16(0)
    
        
    except Exception as erreur:
        print("Erreur:", erreur)

