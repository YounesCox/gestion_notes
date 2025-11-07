def saisie_float(message, minimum=0, maximum=20):
    """Demande une saisie sécurisée d'une note entre deux bornes."""
    while True:
        try:
            valeur = float(input(message))
            if minimum <= valeur <= maximum:
                return valeur
            else:
                print(f"⚠️ La valeur doit être comprise entre {minimum} et {maximum}.")
        except ValueError:
            print("❌ Entrée invalide, veuillez entrer un nombre.")

def confirmer_action(message="Confirmer l’action (O/N): "):
    """Demande confirmation avant d’effectuer une action."""
    choix = input(message).strip().lower()
    return choix in ('o', 'oui', 'y', 'yes')

def ligne_sep(taille=40):
    """Affiche une ligne de séparation pour plus de lisibilité."""
    print("-" * taille)
