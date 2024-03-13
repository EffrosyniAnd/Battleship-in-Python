from random import randint 
def show_board(board):
            for row in board:
                print(row)
n=int(input("press 1 for 1-player game or 2 for 2-player game:"))
if n!=1 and n!=2:
    print("invalid number.Try again")
   
if n==2:
        board = []
        for i in range(5):
            board.append([""] * 5)
        x=y=1
        lst1=[]
        lst2=[]
        lst = ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2 ', 'c3', 'c4', 'c5', 'd1',
               'd2', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5']

        while x < 6:
            z = input("enter the no %d: "%x)
            if z not in lst or z  in lst1:
                print('error')
            else:
                lst1.append(z)
                x += 1
        while y< 6:
            k = input("player2 enter the no %d: "%y)
            if k not in lst or k  in lst2:
                print('error')
            else:
                lst2.append(k)
                y+= 1
        w = randint(1, 2)
        if w == 1:
            while i!=0 or u!=0:
                i=0
                position1=[]
                r=input("Player 1 enter the position to throw your missile:")
                if r not in lst or r in position1:
                    print('error')
                else:
                    position1.append(r)
                    print("missile thrown at",r)
                if r in lst2:
                    #να πηγαινει στον πινακα του 2
                    print("target hit!")
                    i+=1
                    show_board(board)
                    show_board(board)
                    if i==5:
                        print("player1 won")
                else:
                    pass# να πηγαινει στον πινακα  και να βαζει
                    print("target miss")
                    show_board(board)
                    show_board(board)

                u=0
                position2=[]
                h= input("Player 2 enter the position to throw your missile:")
                if h not in lst or h in position2: 
                    print('error')
                    h= input("Player 2 enter the position to throw your missile:")
                else:
                    position2.append(h)
                    print("missile thrown at", h)
                if h in lst1:
                    u+=1
                    pass#να πηγανει στον πινακα 1 να βαζει χ
                    print("target hit!")
                    show_board(board)
                    show_board(board)
                    if u==5:
                        print("player2 won")
                else:
                    pass#να πηγαινει στον πινακα 1 και να βαλει 0
                    show_board(board)
                    show_board(board)
                    print("target miss")
        
        elif w==2:
            print("player2 starts first")
            u=0
            position2=[]
            h= input("Player 2 enter the position to throw your missile:")
            if h not in lst or h in position2: 
                print('error')
                h= input("Player 2 enter the position to throw your missile:")
            else:
                position2.append(h)
                print("missile thrown at", h)
                if h in lst1:
                    u+=1
                    pass#να πηγανει στον πινακα 1 να βαζει χ
                    print("target hit!")
                    show_board(board)
                    show_board(board)
                    if u==5:
                        print("player2 won")
                else:
                    pass#να πηγαινει στον πινακα 1 και να βαλει 0
                    show_board(board)
                    show_board(board)
                    print("target miss")

                i=0
                position1=[]
                r=input("Player 1 enter the position to throw your missile:")
                if r not in lst or r in position1:
                    print('error')
                else:
                    position1.append(r)
                    print("missile thrown at",r)
                if r in lst2:
                    #να πηγαινει στον πινακα του 2
                    print("target hit!")
                    i+=1
                    show_board(board)
                    show_board(board)
                    if i==5:
                        print("player1 won")
                else:
                    pass# να πηγαινει στον πινακα  και να βαζει
                    print("target miss")
                    show_board(board)
                    show_board(board)
