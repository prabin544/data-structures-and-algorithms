from hashtable.hashtable import Hashtable

def hash_intersection(tree1, tree2):
    placeholder = []
    tree1 = tree1.pre_order()
    tree2 = tree2.pre_order()
    hashtable = Hashtable()

    for value in tree1:
        hashtable.add(key=str(value), value = value)

    for value in tree2:
        if hashtable.contains(str(value)):
            placeholder.append(value)

    return placeholder
        