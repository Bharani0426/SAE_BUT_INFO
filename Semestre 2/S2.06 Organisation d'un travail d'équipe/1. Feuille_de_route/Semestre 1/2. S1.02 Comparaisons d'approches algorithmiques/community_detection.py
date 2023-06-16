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
    """
    Crée un réseau d'amis à partir d'une liste de couples d'amis

    Paramètres:
    pairs_of_friends (list): Une liste de tuples représentant les couples d'amis. Chaque tuple contient deux chaînes de caractères représentant les noms des amis.
    """
    
    network1={}
    i=0
    
    while i<len(list_of_friends)/2:
        
        if list_of_friends[2*i]in list(network1):
            network1[list_of_friends[2*i]]+=[list_of_friends[2*i+1]]
            
        else:
            network1[list_of_friends[2*i]]=[list_of_friends[2*i+1]]
        
        if list_of_friends[2*i+1] in list(network1):
            network1[list_of_friends[2*i+1]]+=[list_of_friends[2*i]]
            
        else:
            network1[list_of_friends[2*i+1]]=[list_of_friends[2*i]]
            
        i+=1
    return network1
    

create_network(p_amis)

def get_people(network):
	"""
    Cette fonction prend en paramètre un rÃ©seau (dictionnaire) et retourne la liste des personnes dans un tableau.
    
    :param network: un dictionnaire représentant un réseau social
    :return: une liste des personnes prÃ©sentes dans le rÃ©seau
    """

	tab=[]
	personne=list(network)
	
	i=0
	while i<len(personne):
		if personne not in tab:
			tab.append(personne)
		i+=1
	return tab
	

    
def are_friends(network,person1,person2):
	"""
    Vérifie si les deux personnes données sont amies dans le réseau donné.

    :param network: Le réseau de personnes sous forme de dictionnaire, où chaque clé est un nom de personne et la valeur associée est une liste de noms d'amis.
    """

	if person1 in network[person2]:
        return True
    else:
        return False




def all_his_friends(network,person,group):
    """
    Vérifie si une personne est amie avec toutes les personnes d'un groupe donnée.
    """
      for in range (len(groupe)):
          if groupe[i] not in network[pers]:
              return False
      return True


def is_a_community(network, group):
    """
    Cette fonction prend en paramètre un dictionnaire modélisant le réseau et un groupe de personnes (tableau de personnes)
    et retourne True si ce groupe est une communauté, et False sinon.
    Une communautÃ© est définie comme un groupe de personnes où tous les amis de chaque personne appartiennent également au groupe.
    """

    for person1 in group:
        for person2 in group:
            if person1 != person2 and person2 not in network[person1]:
                return False
    return True



def find_community(network, group):
    """
    Cette fonction prend en paramètre un réseau (un dictionnaire où les clés sont les noms des personnes
    et les valeurs sont les noms de leurs amis) et un groupe (une liste de noms de personnes).
    Elle utilise l'heuristique décrite pour trouver une communautÃ© maximale dans le réseau en utilisant
    l'ordre des personnes dans le groupe.
    Elle retourne la communautée trouvée (une liste de noms de personnes).
    """
    communaute=[group[0]]
    i=1
    while i<len(group):
        if all_his_friends(network,group[i],communaute)==True:
            communaute.append(group[i])
        i+=1
    return communaute


   
def order_by_decreasing_popularity(network, group):
    """
    Tri le groupe de personnes selon la popularité (nombre d'amis) décroissante dans un réseau donné.
    
    Parameters:
        network (dict): un dictionnaire représentant le réseau social, où les clés sont les noms des personnes
                        et les valeurs sont les noms de leurs amis sous forme de liste.
        group (list): un groupe de personnes Ã  trier selon leur popularitée.
    
    Returns:
        list: le groupe de personnes trié selon la popularité décroissante.
    """
    dico={}
    tab=[]
    for person in group:
        dico[person]=len(network[person])
    tri = sorted(dico,key=lambda x: x[1], reverse=True)
    for elt in tri:
        tab.insert(0,elt)
    tab.reverse()
    return tab



def find_community_by_decreasing_popularity(network):
    """
    Cette fonction prend en paramètre un réseau de personnes et retourne la communauté maximale en utilisant l'heuristique de construction de communauté maximale.
    La communauté est construite en triant les personnes du réseau selon l'ordre décroissant de popularité et en ajoutant les personnes connectées à au moins une personne déjà dans la communauté.
    """
    group = order_by_decreasing_popularity(network, get_people(network))
    return find_community(network, group)


def find_community_from_person(network, person):
    """
    Trouve la communauté maximale contenant une personne donnée dans un réseau donné en utilisant les heuristiques suivantes:
    - Sélectionne une personne dans le réseau
    - Crée une communauté contenant uniquement cette personne
    - Considère les amis de cette personne par ordre de popularité décroissant.
    Pour chacun de ces amis, s'ils sont amis avec tous les membres de la communauté déjà créée, ils sont ajoutés à la communauté.
    """
    community = [person]
    group = find_community_by_decreasing_popularity(network)
    i = 0
    while i < len(group):
        if all_his_friends(network, group[i], community):
            community.append(group[i])
        i += 1
    return community

def find_max_community(network):
    """
    Trouve la communauté maximale dans un réseau en utilisant l'heuristique de recherche de communauté donnée par la fonction find_community_from_person.
    """
    group = get_people(network)
    i = 0
    while i < len(group):
        max_community = find_community_from_person(network, group[i])
        j = 1
        while j < len(group):
            if find_community_from_person(network, group[j]) > max_community:
                max_community = find_community_from_person(network, group[j])
            j += 1
        i += 1
    return max_community
