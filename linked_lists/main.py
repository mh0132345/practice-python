from linked_list import LinkedList
# from node import Node


def main():
    ll = LinkedList()

    print("Initial size: ", len(ll))
    ll.push(4)
    print("New size: ", len(ll))
    ll.push(6)
    # Push to the end
    ll.append(8)
    print(ll)
    ll.pop()
    print(ll)
    ll.push(9)
    ll.push(8)
    print(ll)
    if ll.contains(8):
        print("Yes")
    else:
        print("No")

    print("Delete all 8: ")
    ll.delete(8)
    print(ll)

if __name__ == "__main__":
    main()