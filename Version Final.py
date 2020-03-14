from operator import attrgetter

try:
    nombre_de_choix = int(input("Combien y a t'il de candidats ? : "))
    decompte_jugement = nombre_de_choix

    print("")

    nombre_de_votant = int(input("Combien de personne vont voter ? : "))

    classement = []
    liste_des_choix = []

    print("")
    print("Entrez les noms des candidats les uns à la suite des autres.")
    print("")

    for i in range(nombre_de_choix):
        liste_des_choix.append(input("Nom des candidats: "))

    print("")
    print("Candidats enregistré :")

    n = 0
    for i in range(nombre_de_choix):
        print("{}".format(liste_des_choix[n]))
        n += 1

    ''' ICI COMMENCE LE JUGEMENT '''

    class Candidat:
        def __init__(self, Nom, Mention, Pourcentage):
            self.Nom = Nom
            self.Mention = Mention
            self.Pourcentage = Pourcentage

    def __repr__(self):
        return repr((self.Nom, self.Mention, self.Pourcentage))


    class Jugement:
        def __init__(self, A_rejeter, Insuffisant, Passable, Assez_bien, Bien, Tres_bien, Exellent):
            self.A_rejeter = A_rejeter
            self.Insuffisant = Insuffisant
            self.Passable = Passable
            self.Assez_bien = Assez_bien
            self.Bien = Bien
            self.Tres_bien = Tres_bien
            self.Exellent = Exellent

    while decompte_jugement > 0:

        print("")

        voix = Jugement(int(input("Combien de voix 'A rejeter' ? : ")),
                        int(input("Combien de voix 'Insuffisant' ? : ")),
                        int(input("Combien de voix 'Passable' ? : ")),
                        int(input("Combien de voix 'Assez bien' ? : ")),
                        int(input("Combien de voix 'Bien' ? : ")),
                        int(input("Combien de voix 'Très bien' ? : ")),
                        int(input("Combien de voix 'Excellent' ? : ")))

        Au_moins_A_rejeter = voix.A_rejeter
        Au_moins_Insuffisant = voix.A_rejeter + voix.Insuffisant
        Au_moins_Passable = voix.A_rejeter + voix.Insuffisant + voix.Passable
        Au_moins_Assez_bien = voix.A_rejeter + voix.Insuffisant + voix.Passable + voix.Assez_bien
        Au_moins_Bien = voix.A_rejeter + voix.Insuffisant + voix.Passable + voix.Assez_bien + voix.Bien
        Au_moins_Tres_bien = voix.A_rejeter + voix.Insuffisant + voix.Passable + voix.Assez_bien + voix.Bien + voix.Tres_bien
        Au_moins_Exellent = voix.A_rejeter + voix.Insuffisant + voix.Passable + voix.Assez_bien + voix.Bien + voix.Tres_bien + voix.Exellent

        Total_des_voix = voix.A_rejeter + voix.Insuffisant + voix.Passable + voix.Assez_bien + voix.Bien + voix.Tres_bien + voix.Exellent
        Mediane = Total_des_voix / 2

        Plus_que_Insuffisant = voix.Passable + voix.Assez_bien + voix.Bien + voix.Tres_bien + voix.Exellent
        Plus_que_Passable = voix.Assez_bien + voix.Bien + voix.Tres_bien + voix.Exellent
        Plus_que_Assez_bien = voix.Bien + voix.Tres_bien + voix.Exellent
        Plus_que_Bien = voix.Tres_bien + voix.Exellent
        Plus_que_Tres_bien = voix.Exellent

        if Au_moins_A_rejeter >= Mediane:
            Mention = 0
            Pourcentage = round(Au_moins_A_rejeter / Total_des_voix * 100, 2)

        elif Au_moins_Insuffisant >= Mediane:
            if Plus_que_Insuffisant < Au_moins_A_rejeter:
                Mention = 1
                Pourcentage = 1 - round(Au_moins_A_rejeter / Total_des_voix * 100, 2)
            else:
                Mention = 2
                Pourcentage = round(Plus_que_Insuffisant / Total_des_voix * 100, 2)

        elif Au_moins_Passable >= Mediane:
            if Plus_que_Passable < Au_moins_Insuffisant:
                Mention = 3
                Pourcentage = 1 - round(Au_moins_Insuffisant / Total_des_voix * 100, 2)
            else:
                Mention = 4
                Pourcentage = round(Plus_que_Passable / Total_des_voix * 100, 2)

        elif Au_moins_Assez_bien >= Mediane:
            if Plus_que_Assez_bien < Au_moins_Passable:
                Mention = 5
                Pourcentage = 1 - round(Au_moins_Passable / Total_des_voix * 100, 2)
            else:
                Mention = 6
                Pourcentage = round(Plus_que_Assez_bien / Total_des_voix * 100, 2)

        elif Au_moins_Bien >= Mediane:
            if Plus_que_Bien < Au_moins_Assez_bien:
                Mention = 7
                Pourcentage = 1 - round(Au_moins_Assez_bien / Total_des_voix * 100, 2)
            else:
                Mention = 8
                Pourcentage = round(Plus_que_Bien / Total_des_voix * 100, 2)

        elif Au_moins_Tres_bien >= Mediane:
            if Plus_que_Tres_bien < Au_moins_Bien:
                Mention = 9
                Pourcentage = 1 - round(Au_moins_Bien / Total_des_voix * 100, 2)
            else:
                Mention = 10
                Pourcentage = round(Plus_que_Tres_bien / Total_des_voix * 100, 2)

        elif Au_moins_Exellent >= Mediane:
            Mention = 11
            Pourcentage = 1 - round(voix.Exellent / Total_des_voix * 100, 2)

        else:
            Mention = None
            Pourcentage = None

        classement.append(Candidat(liste_des_choix[0], Mention, Pourcentage))  # enregistrement des choix à classer

        del liste_des_choix[0]

        decompte_jugement -= 1

except ValueError:
    print("")
    print("Une erreur c'est est survenue !")
    print("Aucune valeur n'a été entré ou alors elle n'a pas été rentré sous forme de nombre.")
    print("Veillez relancer le programme.")
    classement = []
    nombre_de_votant = None
    exit()

''' ICI COMMENCE LE CLASSEMENT '''

try:
    classement = (sorted(classement, key=attrgetter('Mention', 'Pourcentage'), reverse=True))

    print("")
    vote_blanc = int(input("Combien de personne n'on pas du tout rempli leur bulletin ? : "))

    n = 0
    for i in classement:

        if classement[n].Mention == 0:
            classement[n].Mention = "A rejeter"
        elif classement[n].Mention == 1:
            classement[n].Mention = "Insuffisant -"
        elif classement[n].Mention == 2:
            classement[n].Mention = "Insuffisant +"
        elif classement[n].Mention == 3:
            classement[n].Mention = "Passable -"
        elif classement[n].Mention == 4:
            classement[n].Mention = "Passable +"
        elif classement[n].Mention == 5:
            classement[n].Mention = "Assez bien -"
        elif classement[n].Mention == 6:
            classement[n].Mention = "Assez bien +"
        elif classement[n].Mention == 7:
            classement[n].Mention = "Bien -"
        elif classement[n].Mention == 8:
            classement[n].Mention = "Bien +"
        elif classement[n].Mention == 9:
            classement[n].Mention = "Très bien -"
        elif classement[n].Mention == 10:
            classement[n].Mention = "Très bien +"
        elif classement[n].Mention == 11:
            classement[n].Mention = "Exellent"

        n += 1

    print("")
    print("")

    if classement[0].Mention == "A rejeter" \
            or classement[0].Mention == "Insuffisant +" \
            or classement[0].Mention == "Passable +" \
            or classement[0].Mention == "Assez bien +" \
            or classement[0].Mention == "Bien +" \
            or classement[0].Mention == "Très bien +":
        print("")
        print("Les candidats élus sont {} avec la mention majoritaire {}, avec {}% de mention au dessus de la mention majoritaire."
              .format(classement[0].Nom, classement[0].Mention, classement[0].Pourcentage))

    elif classement[0].Mention == "Insuffisant -" \
            or classement[0].Mention == "Passable -" \
            or classement[0].Mention == "Assez bien -" \
            or classement[0].Mention == "Bien -" \
            or classement[0].Mention == "Très bien -" \
            or classement[0].Mention == "Exellent":
        print("")
        print("Les candidats élus sont {} avec la mention majoritaire {}, avec {}% de mention en dessous de la mention majoritaire."
              .format(classement[0].Nom, classement[0].Mention, 1 - classement[0].Pourcentage))

    print("")

    n = 0
    for i in classement:
        if classement[n].Mention == "A rejeter" \
                or classement[n].Mention == "Insuffisant +" \
                or classement[n].Mention == "Passable +" \
                or classement[n].Mention == "Assez bien +" \
                or classement[n].Mention == "Bien +" \
                or classement[n].Mention == "Très bien +":
            print("")
            print("La mention majoritaire des candidats {} est {}, avec {}% de mention au dessus de la mention majoritaire."
                  .format(classement[n].Nom, classement[n].Mention, classement[n].Pourcentage))

        elif classement[n].Mention == "Insuffisant -" \
                or classement[n].Mention == "Passable -" \
                or classement[n].Mention == "Assez bien -" \
                or classement[n].Mention == "Bien -" \
                or classement[n].Mention == "Très bien -" \
                or classement[n].Mention == "Exellent":
            print("")
            print("La mention majoritaire des candidats {} est {}, avec {}% de mention au dessous de la mention majoritaire."
                  .format(classement[n].Nom, classement[n].Mention, 1 - classement[n].Pourcentage))
        n += 1

    print("")
    print("")
    print("")
    print("Il y a eu {} vote(s) blanc(s), cela représente {}% des électeurs."
          .format(vote_blanc, round(vote_blanc / nombre_de_votant * 100, 1)))

except ValueError or IndexError:
    print("")
    print("Une erreur c'est est survenue !")
    print("Aucune valeur n'a été entré ou alors elle n'a pas été rentré sous forme de nombre.")
    print("Veillez relancer le programme.")
