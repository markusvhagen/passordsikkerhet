import time
import itertools


def bruteforce(passord):

    # Importerer topp 500 passord-tekstfilen, samt deklarerer en tom liste.
    topp500_txt = open("top500.txt", "r")
    topp500 = []
    
    # Legger de importerte passordene i en liste så de er lettere tilgjengelig.
    for linjer in topp500_txt:
        topp500.append(linjer.strip())

    # Starter tiden.
    start_tid = time.time()

    # Sjekker om passord er i listen av de 500 mest brukte.
    for kombinasjon in topp500:
        print("Sjekker " + kombinasjon)
        if kombinasjon == passord:
            tid_brukt = str(time.time() - start_tid)
            print("Fant passord!" + " Passord: " + kombinasjon + " Brukte tiden: " + tid_brukt + " sekunder")
            break

    # Hvis koden fortsetter her er ikke passordet i topp 500
    # Sjekker da alle andre mulige kombinasjoner ved en bruteforce, maks tegn er satt til 8
    alleKombinasjoner = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    lengde = 1
    teller = 1

    for lengde in range(8):

        # Definerer testmengden
        testMengde = (itertools.product(alleKombinasjoner, repeat = lengde))
        print("\n \n")

        print("Sjekker nå mulige kombinasjoner med " + str(lengde), " tegn")
        print("\n")
        print("ANTALL FORSØK PER SEKUND: " + str((teller / (time.time() - start_tid))))
        print("ANTALL SEKUNDER SIDEN START: " + str((time.time() - start_tid)))
        print("ANTALL ULIKE KOMBINASJONER PRØVD HITTIL: " + str(teller))
              
        
        for i in testMengde:

            # Konverterer tuple til string
            i = str(i)

            # Gjør strengen ren
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")

            teller += 1

            if i == passord:
                tid_brukt = str(time.time() - start_tid)
                print("Fant passord!" + " Passord: " + forsøk + " Brukte tiden: " + tid_brukt + " sekunder")
                break

faktisk_passord = input("Skriv inn passord for å sjekke hvor lang tid det ville tatt å bruteforce det: ")
bruteforce(faktisk_passord)


