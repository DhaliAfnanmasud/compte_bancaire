#calendar project
#import calendar
#year=int(input("Enter year: "))
#month=int(input("Enter month: "))
#print("\n",calendar.month(year, month))

# password project
#password=input("Enter your password: ")
#if password=="Minato94":
#    print("Access granted\nWelcome !")
#else:
#    print("Access denied")  


# bank account management project -----------------------------------------------------------------------------------------------------------

def connexion():
    code_connexion = input("Veuillez entrer votre code secret de connexion pour accéder à votre compte : ")
    if code_connexion == "123456":
        print("\nBienvenue ! -------------------------------------------------------------------------------------------------------\n")
    else:
        print("Code incorrect ! 3 tentatives restantes.")
        
def menu():
    print("\nQue souhaitez-vous faire ?\n")
    print("1. Consulter votre solde")
    print("2. Consulter votre solde après un achat")
    print("3. Effectuer un dépôt")
    print("4. Effectuer un retrait")
    print("5. Quitter l'application\n")


def afficher_solde(solde):
    print(f"\nVotre solde est de : {solde:.2f} €")

def solde_achat():
    montant = float(input("Quel est le montant de votre achat ? : "))        
    return montant


def depot():
    montant_depot = float(input("Quel est le montant de votre dépot ? : "))
    if montant_depot < 0:
        print("\nLe montant du dépôt ne peut pas être négatif.")
        return 0
    return montant_depot

def retrait(solde):
    montant_retrait = float(input("Quel est le montant de votre retrait ? : "))
    if montant_retrait > solde:
        print("\nVous ne pouvez pas retirer plus que votre solde actuel.")
        return 0
    return montant_retrait


def merci():
    print("\nMerci d'avoir utilisé notre application. À bientôt !")


def main():
    print("\nProjet d'application de gestion de compte bancaire ----------------------------------------------------------\n")
    solde = 550.60
    connexion()
    while True:
        menu()

        choix = input("Veuillez entrez votre choix : ")
        match choix:
            case "1":
                afficher_solde(solde)
            case "2":
                solde -= solde_achat()
                afficher_solde(solde)
            case "3":
                solde += depot()
                afficher_solde(solde)
            case "4":
                solde -= retrait(solde)
                afficher_solde(solde)
            case "5":
                merci()
                break
            case _:
                print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()