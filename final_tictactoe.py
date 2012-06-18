from random import randint, choice
import pdb

class Game():
   
    def __init__(self):
        self.matrix = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def user_move(self):
#        self.help()
        yourmove = raw_input("Enter your move as 0,0 to 2,2\n")
#        #try:
        i = int(yourmove[0])
#        #except ValueError:
#        #    self.help()
        j = int(yourmove[2])
        if self.matrix[i][j] <> ' ':
            print "That square is occupied.  Try again."
            self.user_move()
        else: 
            self.matrix[i][j] = 'x'

    def help(self):
        print '(0,0) (0,1) (0,2)'
        print '(1,0) (1,1) (1,2)'
        print '(2,0) (2,1) (2,2)'

    def legal_moves(self):
        moves = []
        for i in range(0,3):
            for j in range(0,3):
                if self.matrix[i][j] == ' ':
                    moves.append([i,j])
        return moves

    def move(self, player):
        if player == 'o':
            self.minimax(player)
        else:
            self.user_move()

    def next_turn(self, player):
        if player == 'x':
            player = 'o'
        else:
            player = 'x'
        return player

    def is_won(self):
        won = 'no'
        whowon = 'nobody'
        for i in range(0,3):
            if self.matrix[i][0] == self.matrix[i][1] and self.matrix[i][1] == self.matrix[i][2] and self.matrix[i][0] <> ' ':
                won = 'yes'
                whowon = self.matrix[i][0]
        for j in range(0,3):
            if self.matrix[0][j] == self.matrix[1][j] and self.matrix[1][j] == self.matrix[2][j] and self.matrix[0][j] <> ' ':
                won = 'yes'
                whowon = self.matrix[0][j]
        if self.matrix[0][0] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][2] and self.matrix[1][1] <> ' ':
            won = 'yes'
            whowon = self.matrix[0][0]
        if self.matrix[0][2] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][0] and self.matrix[1][1] <> ' ':
           won = 'yes'
           whowon = self.matrix[1][1]
        return won, whowon

    def print_board(self):
        for i in range(0,2):
            for j in range(0,2): 
                print self.matrix[i][j], '|',
            print self.matrix[i][2]
            print " -  -  - "
        for j in range(0,2): 
            print self.matrix[2][j], '|',
        print self.matrix[2][2]

    def utility(self): #utility is from player o's perspective (1 if o wins, -1 if o loses)
        won, whowon = self.is_won()
        if whowon == 'o':
             util = 1
        elif whowon == 'x':
            util = -1
        else:
            util = 0
        return util

    def game_over(self):
        squares = 0
        for i in range(0,3):    #looping through rows (but not cols - count does that for us)
            squares = squares + self.matrix[i].count('x') + self.matrix[i].count('o')
        if self.is_won()[0] == 'yes':
            return 'over'
        elif squares == 9:
            return 'over'
        else:
            return 'not over'

    def max_value(self): # maximizing player is computer ('o')
        if self.game_over() == 'over':
            return self.utility()
        else:
            maxval = -10           # initialize
            children = []
            availmoves = self.legal_moves()
            for i in range(0,len(availmoves)):
                self.matrix[availmoves[i][0]][availmoves[i][1]] = 'o'     #do move
                children.append(self.min_value())                         #evaluate move
                self.matrix[availmoves[i][0]][availmoves[i][1]] = ' '     #undo move
        return max(max(children), maxval)
            
    def min_value(self): #minimizing player is user ('x')
        if self.game_over() == 'over':
            return self.utility()
        else:
            minval = 10
            children = []
            availmoves = self.legal_moves()
            for i in range(0,len(availmoves)):
                self.matrix[availmoves[i][0]][availmoves[i][1]] = 'x'    #play move (player is 'x' or 'o')
                children.append(self.max_value())
                self.matrix[availmoves[i][0]][availmoves[i][1]] = ' '    #undo move
        return min(min(children), minval)

    def minimax(self, player):
        availmoves = self.legal_moves()
        options = []
        for i in range(0,len(availmoves)):
            self.matrix[availmoves[i][0]][availmoves[i][1]] = 'o'
            options.append(self.min_value())
            self.matrix[availmoves[i][0]][availmoves[i][1]] = ' '    #undo move
        print "options are:", options
        max_val = max(options)
        print "max is ", max_val
        location = options.index(max_val)
        print availmoves[location]
        move = availmoves[location]
        self.matrix[move[0]][move[1]] = 'o'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

b = Game()

b.print_board()

player = choice(['x','o'])
if player == 'o':
     print 'Computer\'s turn first'
else: 
    print 'Your turn first'

while b.game_over() == 'not over':
    b.move(player)
    print "player is", player, "is_won is", b.is_won(), "utility is ", b.utility()
    player = b.next_turn(player)
    b.print_Pboard()

winner = b.is_won()[1]
if winner == 'x':
    print "You win!"
elif winner == 'o':
    print "Computer wins!"
else: 
    print "It's a tie."

