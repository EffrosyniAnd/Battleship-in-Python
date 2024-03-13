from random import randint 
def show_board(board):
    board = []
    for i in range(5):
        board.append([""] * 5)
    set=['a','b','c','d','e']
    for j,i in zip(set,board):
        return (j,i)
def player1_first():
        position1=[]
        r=input("Player 1 enter the position to throw your missile:")
        while r not in lst or r in position1:
            r=input("Player 1 enter the position to throw your missile:try again")
        else:
            position1.append(r)
            print("missile thrown at",r)
        if r in lst2:
            #να πηγαινει στον πινακα του 2
            print("target hit!")
            
            return 1
        else:
            pass# να πηγαινει στον πινακα  και να βαζει
            print("target miss")
            
def player2_first():
        position2=[]
        h= input("Player 2 enter the position to throw your missile:")
        while h not in lst or h in position2: 
            h= input("Player 2 enter the position to throw your missile:")
        else:
            position2.append(h)
            print("missile thrown at", h)
        if h in lst1:
            pass#να πηγανει στον πινακα 1 να βαζει χ
            print("target hit!")
            show_board(board)
            return 1
        else:
            pass#να πηγαινει στον πινακα 1 και να βαλει 0
            
            print("target miss")
n=str(input("press 1 for 1-player game or 2 for 2-player game:"))
while n!='1' and n!='2':
    n=str(input("invalid number.Try again"))
if n=='2':
        
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
        w = randint(1,2)
        if w == 1:
            print("player1 starts first")
            a=0
            b=0
            c=player1_first()
            d=player2_first()
            while c!=1 or d!=1:
                            
            c=player1_first()
            d=player2_first()
                    
                    player1_first()
                    player2_first()
            if c==1 :
                while a<5:
                    a+=1
                    print("P1", end="   ")
                    print("P2")
                    
                    player1_first()
                    player2_first()
                
                    
            elif d==1:
                while  b<5:
                    b+=1
                    
                    
                    player1_first()
                    player2_first()
                if b==5:
                    print("player 2 won")
            else:
                print("player2 starts first")
                print("P1", end="   ")
                print("P2")
                a=0
                b=0
                while c!=1 or d!=1:
                    print("P1", end="   ")
                    print("P2")
                    
                    player2_first()
                    player1_first()
                if d==1:
                    while b<5:
                        b+=1
                        print("P1", end="   ")
                        print("P2")
                        
                        player2_first()
                        player1_first()
                    if b==5:
                        print("player1 won")
                        
                elif c==1:
                    while a<5:
                        a+=1
                        print("P1", end="   ")
                        print("P2")
                        player2_first()
                        player1_first()
                    if a==5:
                        print("player1 won")
