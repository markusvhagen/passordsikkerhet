import time
import itertools

def bruteforce(passord):
    print("Starter søk")

    # Importerer topp 500 passord-tekstfilen, samt deklarerer en tom liste.
    topp500_txt = open("top500.txt", "r")
    topp500 = []

    # Legger de importerte passordene i en liste så de er lettere tilgjengelig.
    for linjer in topp500_txt:
        topp500.append(linjer.strip())

    # Starter tiden, ved å finne ut hva tiden er nå
    start_tid = time.time()

    # Sjekker om passord er i listen av de 500 mest brukte.
    for kombinasjon in topp500:
        if kombinasjon == passord:
            tid_brukt = str(time.time() - start_tid)
            print("Fant passord!" + " Passord: " + kombinasjon + " Brukte tiden: " + tid_brukt + " sekunder")
            time.sleep(5)
            raise SystemExit

    # Hvis koden fortsetter her er ikke passordet i topp 500
    # Sjekker da alle andre mulige kombinasjoner ved en bruteforce, maks tegn er satt til 8
    alleKombinasjoner = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    lengde = 1
    teller = 1

    for lengde in range(8):

        # Definerer testmengden
        testMengde = (itertools.product(alleKombinasjoner, repeat = lengde))

        for i in testMengde:

            teller += 1
            # Konverterer tuple til string
            i = "".join(i)

            if i == passord:
                tid_brukt = str(time.time() - start_tid)
                passordsek = str(teller / (time.time() - start_tid))
                print("Fant passord!" + " Passord: " + i + " Brukte tiden: " + tid_brukt + " sekunder")
                filnavn = "resultat/" + passord + ".txt"
                resultat = open(filnavn, "w")
                resultat.write("Strengen " + passord + " ble funnet på " + tid_brukt + " sekunder, og etter " + str(teller) + " forsøk \n \n")
                resultat.write("I gjennomsnitt ble det undersøkt " + passordsek + " strenger per sekund.")
                time.sleep(5)
                raise SystemExit


faktisk_passord = input("Skriv inn passord for å sjekke hvor lang tid det ville tatt å bruteforce det: ")
bruteforce(faktisk_passord)
