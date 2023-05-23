#!/usr/bin/python3
#Implementation of linked list

class Node:

    def __init__(self,data):
        self.next = None
        self.data = data 

def printmenu():
    print('Linked-list Menu:')
    print('1. Insert node to linked list')
    print('2. Delete node to linked list')
    print('3. Print linked list')
    print('4. Quit menu')


def printlist(head):
    print('\n')
    if head == None:
        print('Linked-list is empty')
    else:
        while head:
            if not head.next:
                print(head.data)
            else: print(head.data, end=' -> ')
            head = head.next

def insertnode(head,data):
    if head == None:
        return Node(data)
    current = head
    while current.next:
        current = current.next
    current.next = Node(data)
    return head

def deletenode(head):
    current = head
    if head == None:
        print('Empty list, nothing to do here!')
        return None
    elif head.next == None:
        return None
    while current.next:
        previous = current
        current = current.next
    previous.next = None
    return head




def main():
    llist = None
    while True:
        print('\n')
        printmenu()
        i = int(input())

        if i==1:
            data = input('Insert node data: ')
            llist = insertnode(llist,data)
        if i==2:
            print('Deleting last node')
            llist = deletenode(llist)
        elif i ==3:
            printlist(llist)
        elif i == 4:
            break

if __name__ == "__main__":
    main()
