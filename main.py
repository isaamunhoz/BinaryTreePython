from BinarySearchTree import BinarySearchTree

def main():
    bst = BinarySearchTree()

    print("Inserting elements...")
    bst.insert(5, "five")
    bst.insert(3, "three")
    bst.insert(7, "seven")
    bst.insert(2, "two")
    bst.insert(4, "four")
    bst.insert(6, "six")
    bst.insert(8, "eight")

    print("Current tree:\n")
    print(bst)

    print("\nTraversals:")
    print("\nPre-order:", end=" ")
    bst.pre_order_traversal()
    print("\nIn-order:", end=" ")
    bst.in_order_traversal()
    print("\nPost-order:", end=" ")
    bst.post_order_traversal()

    print("\nSearching for key 4:", bst.search(4))
    print("Searching for key 9:", bst.search(9))

    print("\nTree properties:")
    print("Number of internal nodes:", bst.count_internal())
    print("Degree of node 5:", bst.degree(5))
    print("Height of node 5:", bst.height(5))
    print("Level of node 4:", bst.level(4))
    print("Ancestors of node 4:", bst.ancestor(4))

    print("\nDeleting node with key 3...")
    bst.delete(3)
    print("In-order after deletion:", end=" ")
    bst.in_order_traversal()
    print("\n\n")
    print(bst)

    print("\nClearing the tree...")
    bst.clear()
    print("Is tree empty?", bst.is_empty())
    print(bst)

if __name__ == "__main__":
    main()
