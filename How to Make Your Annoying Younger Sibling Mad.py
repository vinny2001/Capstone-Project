import time
Behavior = input('How has Carmelina been behaving today? ')

if Behavior == 'bad':
    print("You're going to jail!")
    print("And I'm calling the police!")
    from playsound import playsound
    playsound('phone.mp3')
    playsound('phone_ring.mp3')
    playsound('dispatch.mp3')
    playsound('radio.mp3')
    playsound('police.mp3')
if not Behavior == 'bad':
    print("""You're such good girl!
Mommy loves you sooooooooo much!!!""")

time.sleep(2)
print("Coded by Vincenzo D'Aria")
time.sleep(2)
