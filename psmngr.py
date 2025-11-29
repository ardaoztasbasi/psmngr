import random
import string

while True:
    print("Welcome to Psmngr")
    print("Press")

    userans1 = int(input("1-Create A Password 2-Search For Existing Password 3-Exit : "))

    if userans1 == 1:
        wichpass = input("Name The Password(No Space): ")
        letters = string.ascii_letters
        digits = string.digits
        special = "!@#$%^&*-_=+;:,./?|\\`~"

        all_chars = letters + digits + special

        length = int(input("Password length: "))
 

        password = "".join(random.choice(all_chars) for _ in range(length))
        print("Generated password:", password)

        passwordsfile = open("psmngr.txt", "a")

        passwordsfile.write(f"\n{wichpass} {password}")

        passwordsfile.close()

        print("Password saved! Returning to menu...")

        input("Press Enter To Return To The Menu")

    if userans1 == 2 :
        isim = input("Password Name: ")

        found = False

        with open("psmngr.txt", "r", encoding="utf-8") as f:
            for satir in f:
                parca = satir.strip().split()

                if not parca:
                    continue

                if parca[0].lower() == isim.lower():
                    print("Found:", satir.strip())
                    found = True
                    break
        
        if not found:
            print("We couldn't find the password you're looking for. Try typing the full name.")
        
        input("Press Enter To Return To The Menu")


    if userans1 == 3 :
        break

