from operator import attrgetter

try:
    classement = []
    liste_des_choix = []

    nombre_de_choix = int(input("Combien y a t'il de candidats ? : "))

    print("")

    for i in range(nombre_de_choix):
        liste_des_choix.append(input("Nom du candidat {} : ".format(i+1)))

    print("")
    print("Candidats enregistré :")

    for i in range(nombre_de_choix):
        print("{}".format(liste_des_choix[i]))

    print("")
    nombre_de_votant = int(input("Combien de personnes vont voter ? : "))

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

    for i in range(nombre_de_choix):

        Nom = liste_des_choix[i]

        print("")

        voix = Jugement(int(input("Combien de voix 'A rejeter' pour le candidat {} ? : ".format(liste_des_choix[i]))),
                        int(input("Combien de voix 'Insuffisant' pour le candidat {} ? : ".format(liste_des_choix[i]))),
                        int(input("Combien de voix 'Passable' pour le candidat {} ? : ".format(liste_des_choix[i]))),
                        int(input("Combien de voix 'Assez bien' pour le candidat {} ? : ".format(liste_des_choix[i]))),
                        int(input("Combien de voix 'Bien' pour le candidat {} ? : ".format(liste_des_choix[i]))),
                        int(input("Combien de voix 'Très bien' pour le candidat {} ? : ".format(liste_des_choix[i]))),
                        int(input("Combien de voix 'Excellent' pour le candidat {} ? : ".format(liste_des_choix[i]))))

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

        classement.append(Candidat(Nom, Mention, Pourcentage))  # enregistrement des choix à classer


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

    titre_mention = ["A rejeter", "Insuffisant -", "Insuffisant +", "Passable -", "Passable +",
                     "Assez bien -", "Assez bien +", "Bien -", "Bien +", "Très bien -", "Très bien +", "Exellent"]

    for i in range(len(classement)):
        for j in range(len(titre_mention)):
            if classement[i].Mention == j:
                classement[i].Mention = titre_mention[j]
                break

    print("")
    print("")

    n = 0
    for i in range(11):
        if classement[0].Mention == titre_mention[n]:
            print("")
            print("Les candidats élus sont {} avec la mention majoritaire {}, avec {}% de mention au dessus de la mention majoritaire."
                  .format(classement[0].Nom, classement[0].Mention, classement[0].Pourcentage))
            break

        elif classement[0].Mention == titre_mention[n+1]:
            print("")
            print("Les candidats élus sont {} avec la mention majoritaire {}, avec {}% de mention en dessous de la mention majoritaire."
                  .format(classement[0].Nom, classement[0].Mention, 1 - classement[0].Pourcentage))
            break
        n += 2

    print("")

    for i in range(len(classement)):
        n = 0
        for j in range(11):
            if classement[i].Mention == titre_mention[n]:
                print("")
                print("La mention majoritaire des candidats {} est {}, avec {}% de mention au dessus de la mention majoritaire."
                      .format(classement[i].Nom, classement[i].Mention, classement[i].Pourcentage))
                break

            elif classement[i].Mention == titre_mention[n + 1]:
                print("")
                print("La mention majoritaire des candidats {} est {}, avec {}% de mention au dessous de la mention majoritaire."
                      .format(classement[i].Nom, classement[i].Mention, 1 - classement[i].Pourcentage))
                break
            n += 2

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
