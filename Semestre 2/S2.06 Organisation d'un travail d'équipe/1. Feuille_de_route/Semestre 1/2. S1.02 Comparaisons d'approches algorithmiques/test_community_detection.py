amis = {
  "Alice" : ["Bob", "Dominique"],
  "Bob" : ["Alice", "Charlie", "Dominique"],
  "Charlie" : ["Bob"],
  "Dominique" : ["Alice", "Bob"]
}



def test_create_network():
    assert create_network(["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"])=={'Alice': ['Bob', 'Charlie'], 'Bob': ['Alice', 'Denis'], 'Charlie': ['Alice'], 'Denis': ['Bob']}
    assert create_network([]) == {}
    assert create_network(["Alice", "Bob"]) == {"Alice": ["Bob"], "Bob": ["Alice"]}
    print("Test de la fonction create_network : ok")


def test_get_people():
    assert get_people(amis)==['Alice', 'Bob', 'Charlie', 'Dominique']
    assert get_people({})==[]
    print("Test de la fonction get_people : ok")

def test_are_friends():
    assert(are_friends(amis,'Alice','Bob'))==True
    assert(are_friends(amis,'Alice','Charlie'))==False
    print("Test de la fonction are_friends : ok")

def test_all_his_friends():
    assert all_his_friends(amis,'Alice',['Bob','Dominique'])==True
    assert all_his_friends(amis,'Alice',['Bob','Charlie'])==False
    print("Test de la fonction all_his_friends : ok")
    
def test_is_a_community():
    assert is_a_community(amis,["Alice", "Bob", "Dominique"])==True
    assert is_a_community(amis,["Alice", "Bob", "Charlie"])==False
    print("Test de la fonction is_a_community : ok")

def test_find_community():
    assert find_community(amis,["Alice", "Bob", "Charlie", "Dominique"])==['Alice', 'Bob', 'Dominique']
    assert find_community(amis,["Charlie", "Alice", "Bob", "Dominique"])==['Charlie', 'Bob']
    print("Test de la fonction find_community : ok!")

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(amis,["Alice", "Bob", "Charlie"])==['Bob', 'Alice', 'Charlie']
    assert order_by_decreasing_popularity(amis,["Alice", "Dominique", "Charlie"])==['Alice', 'Dominique', 'Charlie']
    print("Test de la fonction order_by_decreasing_popularity : ok")

def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(amis)==['Bob', 'Alice', 'Dominique']
    print("Test de la fonction find_community_by_decreasing_popularity : ok")

def test_find_community_from_person():
    assert find_community_from_person(amis,'Alice')==['Alice', 'Bob', 'Dominique']
    assert find_community_from_person(amis,'Charlie')==['Charlie', 'Bob']
    print("Test de la fonction find_community_from_person : ok")

def test_find_max_community():
    assert find_max_community(amis)==['Dominique', 'Bob', 'Alice']
    print("Test de la fonction find_max_community : ok")

