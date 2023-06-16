##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############

def create_network(list_of_friends):
    """ Cette fonction permet de créer un réseau d'amis à partir d'un tableau donné.
    Elle prend en argument un tableau qui comprend les noms des personnes et leurs relations.
    Elle retourne un dictionnaire qui contient le réseau des amis. """
    dico = {} # Initialisation de la variable "dico" qui va contenir le réseau des amis
    i = 0
    while i < len(list_of_friends)//2: # La boucle while qui permet de parcourir le tableau de l'algorithme (P1,P2)
        p1 = list_of_friends[2*i] # Personne 1
        p2 = list_of_friends[2*i+1] # Personne 2
        if p1 in list(dico): # Si "p1" se trouve dans la liste du dictionnaire, on lui ajoute la valeur "p2"
            dico[p1]+=[p2]
        else: # Sinon, on lui ajoute un nouvel élément
            dico[p1]=[p2]
        if p2 in list(dico): # Si "p2" se trouve dans la liste du dictionnaire, on lui ajoute la valeur "p1"
            dico[p2]+=[p1]
        else:
            dico[p2]=[p1]
        i+=1
    return dico # Finalement on retourne le "dico" contenant le réseau des amis 

def get_people(network):
    """ Cette fonction crée un tableau à partir d'un reseau (dico).
    Le tableau contient liste des personnes (leurs prénom) présentes dans le réseau. """
    tab=network.keys()
    Liste = list(tab)
    return Liste

def are_friends(network, person1, person2):
    """ Cette fonction prend en paramètre un réseau et deux personne.
    La fonction return true si les deux personnes sont ami(e)s et false sinon """
    if person1 in network[person2]: # Si la personne 1 est dans la liste d'amis de la personne 2
        return True 
    return False

def all_his_friends(network, person, group):
    """ Cette fonction prend en paramètre un réseau, une personne et un groupe.
    La fonction retournera True si la personne est amie avec toutes les personnes du groupe, et False sinon """
    cmp=0
    for amis in group: # On prend une personne (amis) du groupe
        if person in network[amis]: # si la personne est dans le tableau de l'amis
            cmp+=1
    if cmp == len(group): # Si le compteur = nombre des personnes dans le tableau groupe
        return True # Cela veut dire qu'il connait tout le monde (du groupe)
    return False

def is_a_community(network, group):
    """ Cette fonction prend un dico et un groupe de personne (tableau de personnes).
    Celui ci retournera True si ce groupe est une Communauté, et False sinon """
    i=0
    test=True # On commence avec la valeur True de le début pour le comparer
    while i<len(group) and test==True:
        prenom=group[i] # On prend le prenom de la personne "i"
        group.pop(i) # On efface la personne "i" du tableau
        test=all_his_friends(network,prenom,group) #Teste si tous les utilisateurs du groupe sont amis
        group.append(prenom) # On rajoute la personne de nouveau sur le tableau groupe
        i+=1
    return test

def find_community(network, group):
    """ Cette fonction trouve les membres d'une communauté à l'intérieur d'un groupe dans un réseau donné.
Elle prend en paramètre un réseau et un groupe et retourne une liste des membres de la communauté. """
    communaute=[group[0]] # Initialiser la liste communaute et y inclure le premier élément du groupe
    i=1
    while i<len(group): # Tant que le compteur i est inférieur à la taille du groupe il faut vérifier  si tous les amis de l'élément du groupe correspondant à i sont dans la communaute
        if all_his_friends(network,group[i],communaute)==True:
            communaute.append(group[i])
        i+=1
    return communaute

def order_by_decreasing_popularity(network, group):
    """Cette fonction prend en paramètre un réseau et un groupe et renvoie le groupe trié par ordre décroissant de popularité (nombre d'amis)"""
    dico={} # Dico dans lequel nous allons ranger les prenoms avec le nombre d'amis qu'ils ont
    tab=[] # tableau dans lequel on aura la liste trié
    for person in group:
        dico[person]=len(network[person]) # ex: {"alice":3 , "Bob":2}
        # key=lambda x: x[1], c'est pour prendre les valeur des clè du dico et les trier par rapport à eux
        # reverse = True, trié décroissante
    classement = sorted(dico,key=lambda x: x[1], reverse=True) # On va trier le dico en ordre décroissante
    for poste in classement: #On va rajouter les personne une par une en ordre décroissante dans le tableau
        tab.append(poste)
    return tab

def find_community_by_decreasing_popularity(network):
    """Cette fonction trouve une communauté dans un réseau en triant les personnes par ordre décroissant de popularité."""
    #La fonction find_community trouve une communauté dans le réseau à partir des personnes triées précédemment.
    tab=order_by_decreasing_popularity(network,get_people(network))
    communaute=find_community(network,tab)
    return communaute

def find_community_from_person(network, person):
    """ Cette fonction prend en paramètre un réseau social et une personne et 
    renvoie une liste des personnes qui font partie de la même communauté que cette personne. """
    tab=[person]
    #Trouver les personnes qui sont amis avec la personne donnée et les trier par popularité
    resultat = order_by_decreasing_popularity(network,(network[person]))
    for people in resultat:
        if all_his_friends(network, people, tab)==True: #Vérifier si toutes les personnes trouvées sont amis avec la personne donnée
            tab.append(people)
    return tab

def find_max_community(network):
    """ Cette fonction prend en paramètre un réseau.
    La fonction retourne la plus grande communauté trouvée"""
    tab = get_people(network) # Personne qui dans le réseau
    com_max=[] # tab qui servira pour garder la communité la plus grande
    for person in tab:
        resultat = find_community_from_person(network, person)
        if len(resultat)>len(com_max): # On compare les tableaux
            com_max=resultat #on garde le plus grand
    return com_max