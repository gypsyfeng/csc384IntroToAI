#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

'''
Construct and return Futoshiki CSP models.
'''

from cspbase import *
import itertools

def futoshiki_csp_model_1(initial_futoshiki_board):
    '''Return a CSP object representing a Futoshiki CSP problem along with an
    array of variables for the problem. That is return

    futoshiki_csp, variable_array

    where futoshiki_csp is a csp representing futoshiki using model_1 and
    variable_array is a list of lists

    [ [  ]
      [  ]
      .
      .
      .
      [  ] ]

    such that variable_array[i][j] is the Variable (object) that you built to
    represent the value to be placed in cell i,j of the futoshiki board
    (indexed from (0,0) to (n-1,n-1))


    The input board is specified as a list of n lists. Each of the n lists
    represents a row of the board. If a 0 is in the list it represents an empty
    cell. Otherwise if a number between 1--n is in the list then this
    represents a pre-set board position.

    Each list is of length 2n-1, with each space on the board being separated
    by the potential inequality constraints. '>' denotes that the previous
    space must be bigger than the next space; '<' denotes that the previous
    space must be smaller than the next; '.' denotes that there is no
    inequality constraint.

    E.g., the board

    -------------------
    | > |2| |9| | |6| |
    | |4| | | |1| | |8|
    | |7| <4|2| | | |3|
    |5| | | | | |3| | |
    | | |1| |6| |5| | |
    | | <3| | | | | |6|
    |1| | | |5|7| |4| |
    |6> | |9| < | |2| |
    | |2| | |8| <1| | |
    -------------------
    would be represented by the list of lists

    [[0,'>',0,'.',2,'.',0,'.',9,'.',0,'.',0,'.',6,'.',0],
     [0,'.',4,'.',0,'.',0,'.',0,'.',1,'.',0,'.',0,'.',8],
     [0,'.',7,'.',0,'<',4,'.',2,'.',0,'.',0,'.',0,'.',3],
     [5,'.',0,'.',0,'.',0,'.',0,'.',0,'.',3,'.',0,'.',0],
     [0,'.',0,'.',1,'.',0,'.',6,'.',0,'.',5,'.',0,'.',0],
     [0,'.',0,'<',3,'.',0,'.',0,'.',0,'.',0,'.',0,'.',6],
     [1,'.',0,'.',0,'.',0,'.',5,'.',7,'.',0,'.',4,'.',0],
     [6,'>',0,'.',0,'.',9,'.',0,'<',0,'.',0,'.',2,'.',0],
     [0,'.',2,'.',0,'.',0,'.',8,'.',0,'<',1,'.',0,'.',0]]


    This routine returns Model_1 which consists of a variable for each cell of
    the board, with domain equal to [1,...,n] if the board has a 0 at that
    position, and domain equal [i] if the board has a fixed number i at that
    cell.

    Model_1 also contains BINARY CONSTRAINTS OF NOT-EQUAL between all relevant
    variables (e.g., all pairs of variables in the same row, etc.).

    All of the constraints of Model_1 MUST BE binary constraints (i.e.,
    constraints whose scope includes two and only two variables).
    '''
  #IMPLEMENT 
    vs = []
    n = len(initial_futoshiki_board)
    csp = CSP('initial_futoshiki_1')
    for y in range(0, n):
        vs_row = []
        for x in range(0, len(initial_futoshiki_board[y])):
            obj = initial_futoshiki_board[y][x]
            #variables
            if (x % 2 == 0):
                domain = []
                if obj != 0:
                    domain.append(obj)
                else:
                    for i in range(1, n+1):
                        domain.append(i)
                new_var = Variable((int(x/2), y), domain)
                print new_var.name
                vs_row.append(new_var)
                csp.add_var(new_var)
        vs.append(vs_row)
                
    #add pairs of variables in the same row
    not_equal_var(csp, n)
    
    #potential constraints
    potential_cons(initial_futoshiki_board, csp)
    return csp, vs


def not_equal_var(csp, n): #type 0
    vs = csp.get_all_vars()
    for y in range(0, n):
        for x in range(y*n, (y+1)*n):
            for i in range(x+1, (y+1)*n):
                scope = tuple((vs[x], vs[i]))
                new_constraint = Constraint((scope, 0), scope) #name haven't decided yet
                tuples = []
                for a in scope[0].domain():
                    for b in scope[1].domain():
                        if a != b:
                            pair = tuple((a, b))
                            tuples.append(pair)
                new_constraint.add_satisfying_tuples(tuples)
                csp.add_constraint(new_constraint)
    return

def potential_cons(initial_futoshiki_board, csp):
    vs = csp.get_all_vars()
    n = len(initial_futoshiki_board)
    for y in range(0, n):
        for x in range(0, len(initial_futoshiki_board[y])):
            obj = initial_futoshiki_board[y][x]    
            if x % 2 != 0:
                if obj == '<':                     #type 1
                    k = int((y+1) * (x+1)/2 - 1)
                    scope = tuple((vs[k], vs[k+1]))
                    new_constraint = Constraint((scope, 1), scope) 
                    tuples = []
                    for a in scope[0].domain():
                        for b in scope[1].domain():
                            if a < b:
                                pair = tuple((a, b))
                                tuples.append(pair)
                    new_constraint.add_satisfying_tuples(tuples)
                    csp.add_constraint(new_constraint)
                    
                elif obj == '>':                   #type 2
                    k = int((y+1) * (x+1)/2 - 1)
                    scope = tuple((vs[k], vs[k+1]))
                    new_constraint = Constraint((scope, 2), scope) 
                    tuples = []
                    for a in scope[0].domain():
                        for b in scope[1].domain():
                            if a > b:
                                pair = tuple((a, b))
                                tuples.append(pair)
                    new_constraint.add_satisfying_tuples(tuples)
                    csp.add_constraint(new_constraint)
    return

##############################


def futoshiki_csp_model_2(initial_futoshiki_board):
    '''Return a CSP object representing a futoshiki CSP problem along with an
    array of variables for the problem. That is return

    futoshiki_csp, variable_array

    where futoshiki_csp is a csp representing futoshiki using model_2 and
    variable_array is a list of lists

    [ [  ]
      [  ]
      .
      .
      .
      [  ] ]

    such that variable_array[i][j] is the Variable (object) that you built to
    represent the value to be placed in cell i,j of the futoshiki board
    (indexed from (0,0) to (n-1,n-1))

    The input board takes the same input format (a list of n lists of size 2n-1
    specifying the board) as futoshiki_csp_model_1.

    The variables of Model_2 are the same as for Model_1: a variable for each
    cell of the board, with domain equal to [1,...,n] if the board has a 0 at
    that position, and domain equal [n] if the board has a fixed number i at
    that cell.

    However, Model_2 has different constraints. In particular, instead of
    binary non-equals constaints Model_2 has 2*n all-different constraints:
    all-different constraints for the variables in each of the n rows, and n
    columns. Each of these constraints is over n-variables (some of these
    variables will have a single value in their domain). Model_2 should create
    these all-different constraints between the relevant variables, and then
    separately generate the appropriate binary inequality constraints as
    required by the board. There should be j of these constraints, where j is
    the number of inequality symbols found on the board.  
    '''

#IMPLEMENT
    vs = []
    n = len(initial_futoshiki_board)
    csp = CSP('initial_futoshiki_2')
    for y in range(0, n):
        vs_row = []
        for x in range(0, len(initial_futoshiki_board[y])):
            obj = initial_futoshiki_board[y][x]
            #variables
            if (x % 2 == 0):
                domain = []
                if obj != 0:
                    domain.append(obj)
                else:
                    for i in range(1, n+1):
                        domain.append(i)
                new_var = Variable((int(x/2), y), domain)
                vs_row.append(new_var)
                csp.add_var(new_var)
        vs.append(vs_row)
                
    #variables in the same row
    same_row(csp, n)
    
    #potential constraints
    potential_cons(initial_futoshiki_board, csp)
    return csp, vs


def same_row(csp, n):
    vs = csp.get_all_vars()
    y = 0
    while y < n:
        x = 0
        scope = []
        all_c = itertools.permutations(range(1, n+1))
        all_comb = []
        for a in all_c:
            all_comb.append(a)
        while x < n:
            v = vs[y*n+x]
            scope.append(v)
            if len(v.cur_domain()) == 1:
                for c in all_comb:
                    if c[x] != v.domain()[0]:
                        all_comb.remove(c)
            x = x + 1
        tuple(scope)
        new_constraint = Constraint((scope, y, 0), scope)
        new_constraint.add_satisfying_tuples(all_comb)
        y = y + 1
        csp.add_constraint(new_constraint)
    return
