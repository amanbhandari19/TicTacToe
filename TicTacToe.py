def main():
    import random
    from IPython.display import clear_output

    def choose_first():
        x=random.randint(1,2)
        if x==1:
            print('Player 1 will go first.')
        else:
            print('Player 2 will go first.')      
        return x

    def replay():
        restart=input('Do you want play another game!! select yes or no: ')

        while (restart.lower()!= 'yes' and restart.lower()!= 'no'):
            restart=input('Play again??? Please enter yes or no:  ' )
            print('val '+restart.lower())
        return restart.lower()

    def place_marker(board, marker, position):
        board[position]=marker
        display_board(board)

    def space_check(board, position):
        return (board[position]!='X' and board[position]!='O')

    def player_choice(board,plyVal):
        pos=int(input(f'Player{plyVal} choose your position: (1-9) \n'))
        return pos

    def full_board_check(board):
       # print(board)
        count=0
        for item in board:
            if item=='X' or item=='O' :
                count +=1
                if(count==9):
                    return True
                    break
            elif item!='X' and item!='O' and count!=0:
                return False

    def win_check(board, mark):
        comb={1:board[1]+board[2]+board[3],
             2:board[4]+board[5]+board[6],
             3:board[7]+board[8]+board[9],
             4:board[1]+board[4]+board[7],
             5:board[2]+board[5]+board[8],
             6:board[3]+board[6]+board[9],
             7:board[3]+board[5]+board[7],
             8:board[1]+board[5]+board[9]}

        return (mark*3 in comb.values())

    def display_board(board): 
        clear_output()
        brd={11:'      |      |',
        1:('  '+ board[1]+ '   |   '+ board[2]+ '  |   '+ board[3] ),
        4:('  '+ board[4]+ '   |   '+ board[5]+ '  |   '+ board[6] ),
        7:('  '+ board[7]+ '   |   '+ board[8]+ '  |   '+ board[9] ),
        13:'_ _ _ _ _ _ _ _ _ _ _'}
        pattern={'bord':[11,7,11,13,11,4,11,13,11,1,11]}


        for game in pattern['bord']:
            print(brd[game])

    print ('Welcome to Tic Tac Toe!')

    p1v=input('Player 1: Do you want to be X or O? ')
    p2v=''
    while(p1v !='X' and p1v !='O'):
        p1v=input('Player 1: Please select X or O? ')

    if(p1v=='X'):
        p2v='O'
    elif(p1v=='O'):
        p2v='X'

    print(f'player values: Player1 is {p1v} and Player2 is {p2v}')

    whchPlyr=choose_first()
    gameOn='N'


    strt=input('Are you ready to play? Enter yes or no. ' )
    while (strt.lower()!= 'yes' and strt.lower()!= 'no'):
            strt=input('Are you ready to play? Please enter yes or no. ' )
            print('val '+strt.lower())

    rboard=['#','1','2','3','4','5','6','7','8','9']

    if(strt.lower()== 'yes'):
        gameOn='Y'     
        display_board(rboard)
    elif (strt.lower()== 'no'):
        clear_output()
        print('Restarting the game!!')
        main()

    while(gameOn=='Y'):
        if(not full_board_check(rboard)):
            pos=player_choice(rboard,whchPlyr)
            if whchPlyr==1:
                print(f'Game is ON and Player {whchPlyr} with Value of {p1v} is playing')
                avail=space_check(rboard, pos)
                if(avail):
                    place_marker(rboard,p1v,pos)
                    if(win_check(rboard,p1v)):
                        print(f'Player {whchPlyr} WON the game!! Congratulations!!!')
                        rstrt=replay()
                        if rstrt=='yes':
                            gameOn='N'
                            rboard=['#','1','2','3','4','5','6','7','8','9']
                            main()
                        else:
                            gameOn='N'
                            exit()  
                else:
                    print(f'Game is ON and Player {whchPlyr} select available space from board between (1-9)')
                    continue
                whchPlyr=2
            elif whchPlyr==2:
                print(f'Game is ON and Player {whchPlyr} with Value of {p2v} is playing')
                avail=space_check(rboard, pos)
                if(avail):
                    place_marker(rboard,p2v,pos)
                    if(win_check(rboard,p2v)):
                        print(f'Player {whchPlyr} WON the game!! Congratulations!!!')
                        rstrt=replay()
                        if rstrt=='yes':
                            gameOn='N'
                            rboard=['#','1','2','3','4','5','6','7','8','9']
                            main()
                        else:
                            gameOn='N'
                            exit()
                else:
                    print(f'Game is ON and Player {whchPlyr} select available space from board between (1-9)')
                    continue
                whchPlyr=1
        elif full_board_check(rboard):
            print('Game ended in Tie!!!')
            rstrt=replay()
            if rstrt=='yes':
                gameOn='N'
                rboard=['#','1','2','3','4','5','6','7','8','9']
                main()
            else:
                gameOn='N'
                exit()
main()
