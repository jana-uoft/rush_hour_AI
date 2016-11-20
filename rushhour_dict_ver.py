#Look for #IMPLEMENT tags in this file. These tags indicate what has to be
#implemented to complete the warehouse domain.

'''
rushhour STATESPACE
'''
#   You may add only standard python imports---i.e., ones that are automatically
#   available on CDF.
#   You may not remove any imports.
#   You may not import or otherwise source any of your own files

from search import *
from random import randint
from copy import deepcopy

##################################################
# The search space class 'rushhour'             #
# This class is a sub-class of 'StateSpace'      #
##################################################


class rushhour(StateSpace):
    def __init__(self, action, gval, vehicle_dict, board_properties, parent=None):
        """Initialize a rushhour search state object."""
        StateSpace.__init__(self, action, gval, parent)
        self.vehicle_dict = vehicle_dict
        self.board_properties = board_properties


    def successors(self):
        '''Return list of rushhour objects that are the successors of the current object'''

        """We have 2 actions for each vehicle in the board: For each horizontal vehicle
        in the board, move one block to E or one block to W if its unblocked. For each
        vertical vehicle in the board, move one block to N or one block to S if its
        unblocked. All actions have cost of 1"""
        
        States = list()
        current_index = 0
        (m,n) = self.board_properties[0]

        for (key, val) in self.vehicle_dict:
               
            move_direction = can_move_list(self, vehicle)
                                    
            """vehicle is vertical"""
           
            if (move_direction[0]):
                """if not blocked in the North direction, move one block towards North"""
                new_vehicle_list =  deepcopy(self.vehicle_list)
                new_vehicle_list[current_index][1] = (vehicle[1][0], (vehicle[1][1]-1)%m)
                action = '(move_vehicle(<' + vehicle[0] + '>, <North>)'       
                States.append(rushhour(action, self.gval+1, new_vehicle_list, self.board_properties, self))
                                        
            if (move_direction[2]):
                """if not blocked in the South direction, move one block towards South"""
                new_vehicle_list =  deepcopy(self.vehicle_list)
                new_vehicle_list[current_index][1] = (vehicle[1][0], (vehicle[1][1]+1)%m)
                action = '(move_vehicle(<' + vehicle[0] + '>, <South>)'           
                States.append(rushhour(action, self.gval+1, new_vehicle_list, self.board_properties, self))
                                      
            """vehicle is horizontal"""
             
            if (move_direction[1]):
                """if not blocked in the East direction, move one block towards East"""
                new_vehicle_list = deepcopy(self.vehicle_list)
                new_vehicle_list[current_index][1] = ((vehicle[1][0]+1)%n, vehicle[1][1])
                action = '(move_vehicle(<' + vehicle[0] + '>, <East>)'
                States.append(rushhour(action, self.gval+1, new_vehicle_list, self.board_properties, self))
                
            if (move_direction[3]):
                """if not blocked in the West direction, move one block towards West"""
                new_vehicle_list =  deepcopy(self.vehicle_list)
                new_vehicle_list[current_index][1] = ((vehicle[1][0]-1)%n, vehicle[1][1])
                action = '(move_vehicle(<' + vehicle[0] + '>, <West>)'        
                States.append(rushhour(action, self.gval+1, new_vehicle_list, self.board_properties, self))
                
                
            current_index += 1  # try to move next vehicle in the list
        
        return States
        
        
    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''
        
        # vehicle positions are unique for each state.
        # vehicle length, orientation, is_goal, board_properties all remain same
        
        positions = []
        for v in self.vehicle_list:
            positions.append(v[1])
            
        positions = sorted(positions)
        # need to make it hashble. so convert to tuple.
        
        # first convert the inner lists to tuples.
        positions = [tuple(i) for i in positions]
        
        # now convert the outer list to a tuple.
        positions = tuple(positions)        
   
        return positions


    def print_state(self):
        #DO NOT CHANGE THIS FUNCTION---it will be used in auto marking
        #and in generating sample trace output.
        #Note that if you implement the "get" routines
        #(rushhour.get_vehicle_statuses() and rushhour.get_board_size())
        #properly, this function should work irrespective of how you represent
        #your state.

        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))

        print("Vehicle Statuses")
        for vs in sorted(self.get_vehicle_statuses()):
            print("    {} is at ({}, {})".format(vs[0], vs[1][0], vs[1][1]), end="")
        board = get_board(self.get_vehicle_statuses(), self.get_board_properties())
        print('\n')
        print('\n'.join([''.join(board[i]) for i in range(len(board))]))


#Data accessor routines.

    def get_vehicle_statuses(self):
        '''Return list containing the status of each vehicle
           This list has to be in the format: [vs_1, vs_2, ..., vs_k]
           with one status list for each vehicle in the state.
           Each vehicle status item vs_i is itself a list in the format:
                 [<name>, <loc>, <length>, <is_horizontal>, <is_goal>]
           Where <name> is the name of the robot (a string)
                 <loc> is a location (a pair (x,y)) indicating the front of the vehicle,
                       i.e., its length is counted in the positive x- or y-direction
                       from this point
                 <length> is the length of that vehicle
                 <is_horizontal> is true iff the vehicle is oriented horizontally
                 <is_goal> is true iff the vehicle is a goal vehicle
        '''
        
        return self.vehicle_list


    def get_board_properties(self):
        '''Return (board_size, goal_entrance, goal_direction)
           where board_size = (m, n) is the dimensions of the board (m rows, n columns)
                 goal_entrance = (x, y) is the location of the goal
                 goal_direction is one of 'N', 'E', 'S' or 'W' indicating
                                the orientation of the goal
        '''
        
        return self.board_properties


#############################################
# heuristics                                #
#############################################


def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0


def heur_min_moves(state):
    '''rushhour heuristic'''
    #We want an admissible heuristic. Getting to the goal requires
    #one move for each tile of distance.
    #Since the board wraps around, there are two different
    #directions that lead to the goal.
    #NOTE that we want an estimate of the number of ADDITIONAL
    #     moves required from our current state
    #1. Proceeding in the first direction, let MOVES1 =
    #   number of moves required to get to the goal if it were unobstructed
    #2. Proceeding in the second direction, let MOVES2 =
    #   number of moves required to get to the goal if it were unobstructed
    #
    #Our heuristic value is the minimum of MOVES1 and MOVES2 over all goal vehicles.
    #You should implement this heuristic function exactly, even if it is
    #tempting to improve it.
    
    vehicle_list = state.get_vehicle_statuses()
    board_properties = state.get_board_properties()
    goal_entrance = board_properties[1]
    (m, n) = board_properties[0]
    goal_direction = board_properties[2]
    
    min_moves = [float("inf")]  # incase no goal vechicles or none can reach goal
       
    for vehicle in vehicle_list:
        if vehicle[4]:  # check if it is a goal vehicle
            if vehicle[3]: # vehicle is horizontal
                if vehicle[1][1] == goal_entrance[1]: # check if its in the same row as the goal
                    if goal_direction == 'E':   # only the tail can reach the goal
                        MOVES1 = (goal_entrance[0] - (vehicle[1][0] + vehicle[2] - 1)) % n
                        MOVES2 = ((vehicle[1][0] + vehicle[2] - 1) - goal_entrance[0]) % n
                    else:  # Goal is West. Only the head can reach the goal
                        MOVES1 = (goal_entrance[0] - (vehicle[1][0])) % n
                        MOVES2 = (vehicle[1][0] - goal_entrance[0]) % n
                        
                    min_moves.append(min(MOVES1, MOVES2))
                                       
            else: # vehicle is vertical
                if vehicle[1][0] == goal_entrance[0]: #check if its in the same column as the goal                
                    if goal_direction == 'S': # only the tail can reach the goal
                        MOVES1 = (goal_entrance[1] - (vehicle[1][1] + vehicle[2] - 1)) % m
                        MOVES2 = ((vehicle[1][1] + vehicle[2] - 1) - goal_entrance[1]) % m
                    else:   # goal is North. # only the head can reach the goal
                        MOVES1 = (goal_entrance[1] - vehicle[1][1]) % m
                        MOVES2 = (vehicle[1][1] - goal_entrance[1]) % m
                      
                    min_moves.append(min(MOVES1, MOVES2))
          
    return min(min_moves) # the minimum of MOVES1 and MOVES2 over all goal vehicles


def rushhour_goal_fn(state):
    '''Have we reached a goal state'''
    
    vehicle_list = state.get_vehicle_statuses()
    board_properties = state.get_board_properties()
    goal_entrance = board_properties[1]
    goal_direction = board_properties[2]
    (m, n) = board_properties[0]
    
    for vehicle in vehicle_list:      
        if vehicle[4]: #check if its a goal vehicle
            
            if vehicle[3]: # vehicle is horizontal                  
                if vehicle[1][1] == goal_entrance[1]: #check if its in the same row as the goal                   
                    
                    tail = (vehicle[1][0] + vehicle[2] - 1) % n
                    head = vehicle[1][0]

                    '''Special case when the vehicle length is the same as the board'''
                    if (vehicle[2] == n):
                        # vechicle can move in both West and East and reach the goal
                        # only if its head or tail is on the goal entrance
                        if goal_entrance[0] in [head, tail]:
                            return True 
                    
                    # check if the tail position is on the goal in East
                    if (tail == goal_entrance[0]) and (goal_direction == 'E'):
                        return True
                        
                    # check if the head position is on the goal in West
                    if (head == goal_entrance[0]) and (goal_direction == 'W'):
                        return True                        
                       
            else:
                # vehicle is vertical                  
                if vehicle[1][0] == goal_entrance[0]: #check if its in the same column as the goal
                    
                    tail = (vehicle[1][1] + vehicle[2] - 1) % m
                    head = vehicle[1][1]
                    
                    '''Special case when the vehicle length is the same as the board'''
                    if (vehicle[2] == m):
                        # vechicle can move in both West and East and reach the goal
                        # only if its head or tail is on the goal entrance
                        if goal_entrance[1] in [head, tail]:
                            return True   
                    
                    # check if the tail position is on the goal in South
                    if (tail == goal_entrance[1]) and (goal_direction == 'S'):
                        return True 
                    
                    # check if the head position is on the goal in North
                    if (head == goal_entrance[1]) and (goal_direction == 'N'):
                        return True
                    
    return False    # current state is not a goal


def make_init_state(board_size, vehicle_list, goal_entrance, goal_direction):
    '''Input the following items which specify a state and return a rushhour object
       representing this initial state.
         The state's its g-value is zero
         The state's parent is None
         The state's action is the dummy action "START"
       board_size = (m, n)
          m is the number of rows in the board
          n is the number of columns in the board
       vehicle_list = [v1, v2, ..., vk]
          a list of vehicles. Each vehicle vi is itself a list
          vi = [vehicle_name, (x, y), length, is_horizontal, is_goal] where
              vehicle_name is the name of the vehicle (string)
              (x,y) is the location of that vehicle (int, int)
              length is the length of that vehicle (int)
              is_horizontal is whether the vehicle is horizontal (Boolean)
              is_goal is whether the vehicle is a goal vehicle (Boolean)
      goal_entrance is the coordinates of the entrance tile to the goal and
      goal_direction is the orientation of the goal ('N', 'E', 'S', 'W')

   NOTE: for simplicity you may assume that
         (a) no vehicle name is repeated
         (b) all locations are integer pairs (x,y) where 0<=x<=n-1 and 0<=y<=m-1
         (c) vehicle lengths are positive integers
    '''
    
    vehicle_dict = {}
    for i in vehicle_list:
        vehicle_dict[i[0]] = [i[1],i[2],i[3],i[4]]
    board_properties = (board_size, goal_entrance, goal_direction)
    return rushhour("START", 0, vehicle_dict, board_properties)



########################################################
#   Functions provided so that you can more easily     #
#   Test your implementation                           #
########################################################


def get_board(vehicle_statuses, board_properties):
    #DO NOT CHANGE THIS FUNCTION---it will be used in auto marking
    #and in generating sample trace output.
    #Note that if you implement the "get" routines
    #(rushhour.get_vehicle_statuses() and rushhour.get_board_size())
    #properly, this function should work irrespective of how you represent
    #your state.
    (m, n) = board_properties[0]
    board = [list(['.'] * n) for i in range(m)]
    for vs in vehicle_statuses:
        for i in range(vs[2]):  # vehicle length
            if vs[3]:
                # vehicle is horizontal
                board[vs[1][1]][(vs[1][0] + i) % n] = vs[0][0]
                # represent vehicle as first character of its name
            else:
                # vehicle is vertical
                board[(vs[1][1] + i) % m][vs[1][0]] = vs[0][0]
                # represent vehicle as first character of its name
    # print goal
    board[board_properties[1][1]][board_properties[1][0]] = board_properties[2]
    return board


def make_rand_init_state(nvehicles, board_size):
    '''Generate a random initial state containing
       nvehicles = number of vehicles
       board_size = (m,n) size of board
       Warning: may take a long time if the vehicles nearly
       fill the entire board. May run forever if finding
       a configuration is infeasible. Also will not work any
       vehicle name starts with a period.

       You may want to expand this function to create test cases.
    '''

    (m, n) = board_size
    vehicle_list = []
    board_properties = [board_size, None, None]
    for i in range(nvehicles):
        if i == 0:
            # make the goal vehicle and goal
            x = randint(0, n - 1)
            y = randint(0, m - 1)
            is_horizontal = True if randint(0, 1) else False
            vehicle_list.append(['gv', (x, y), 2, is_horizontal, True])
            if is_horizontal:
                board_properties[1] = ((x + n // 2 + 1) % n, y)
                board_properties[2] = 'W' if randint(0, 1) else 'E'
            else:
                board_properties[1] = (x, (y + m // 2 + 1) % m)
                board_properties[2] = 'N' if randint(0, 1) else 'S'
        else:
            board = get_board(vehicle_list, board_properties)
            conflict = True
            while conflict:
                x = randint(0, n - 1)
                y = randint(0, m - 1)
                is_horizontal = True if randint(0, 1) else False
                length = randint(2, 3)
                conflict = False
                for j in range(length):  # vehicle length
                    if is_horizontal:
                        if board[y][(x + j) % n] != '.':
                            conflict = True
                            break
                    else:
                        if board[(y + j) % m][x] != '.':
                            conflict = True
                            break
            vehicle_list.append([str(i), (x, y), length, is_horizontal, False])

    return make_init_state(board_size, vehicle_list, board_properties[1], board_properties[2])



'''Check if the current_vehicle in the current state can move one block
   in any given direction. Return a list of bools indicating N, E, S, W.
   <state>: rushhour state object
   <current_vehicle>: the vehicle in vehicle_list to be moved.
   return [True/False, True/False, True/False, True/False].
'''
def can_move_list(state, current_vehicle):
    vehicle_list = state.get_vehicle_statuses()
    board_properties = state.get_board_properties()
    
    # get the 2D list of the current state
    # NOTE: I am using the modified get_board_2 function incase a vehicle is 
    # already on top of a goal, the returned 2D list wont have a goal marked.
    board_game = get_board_2(vehicle_list, board_properties)
    (m, n) = board_properties[0]
    
    # current_vehicle can move in all directions
    North, East, South, West = True, True, True, True
    
    # store the current position of the vehicle
    (curr_x, curr_y) = current_vehicle[1]
    
    if current_vehicle[3]: # current_vehicle is horizontal
        # So current_vehicle cannot move North and South
        North, South = False, False
            
        """Try moving East"""         
        length = current_vehicle[2]
        tail_x = curr_x + length - 1
        
        new_x = (tail_x + 1)%n
        new_y = curr_y
        
        """Check if board_game has any other vehicles in this new position."""
        if board_game[new_y][new_x] not in ['.', 'N', 'E', 'S', 'W']:
            # there is another vehicle in this position
            East = False    
        
            
        """Try moving West"""
        new_x = (curr_x - 1)%n
        new_y = curr_y
        
        """Check if board_game has any other vehicles in this new position"""
        if board_game[new_y][new_x] not in ['.', 'N', 'E', 'S', 'W']:
            # there is another vehicle in this position
            West = False

            
        '''Special case: when vehicle length is the same as the board'''
        # I can avoid this without affecting the game and actually improving it
        # by expanding less nodes and states. Because by moving this vehicle,
        # we are basically in the same overall state, except that the initial
        # position of the vehicle has changed. But I am doing this anyway since
        # the assignment is automarked, and I have no idea if the game will be 
        # tested with the correct number of intermediate states or successors.
        # For that reason, I' am leaving this here. Same thing applies for N, S.
        # UPDATE: Piazza forum, this vechicle can move! 
        if (current_vehicle[2] == n):
            East, West = True, True
            
    else:    # vhecile is vertical
        # So current_vehicle cannot move East and West
        East, West = False, False

        """Try moving North"""          
        new_x = curr_x
        new_y = (curr_y - 1)%m
        
        """Check if board_game has any other vehicles in this new position"""
        if board_game[new_y][new_x] not in ['.', 'N', 'E', 'S', 'W']:
            # there is another vehicle in this position
            North = False


        """Try moving South"""
        length = current_vehicle[2]
        tail_y = curr_y + length - 1
        
        new_x = curr_x
        new_y = (tail_y + 1)%m
        
        """Check if board_game has any other vehicles in this new position"""
        if board_game[new_y][new_x] not in ['.', 'N', 'E', 'S', 'W']:
            # there is another vehicle in this position
            South = False

            
        '''Special case: when vehicle length is the same as the board'''
        if (current_vehicle[2] == m):
            North, South = True, True        
            
    # all directions that the current_vehicle can move are True, others False
    return [North, East, South, West]


'''This is the same function as get_board except for the special case
   where a vehicle is placed on top of the goal in a state.
   So instead of overwriting the vehicle name with the goal,
   I just don't add the goal in the result board 2D list.
'''
def get_board_2(vehicle_statuses, board_properties):
    #DO NOT CHANGE THIS FUNCTION---it will be used in auto marking
    #and in generating sample trace output.
    #Note that if you implement the "get" routines
    #(rushhour.get_vehicle_statuses() and rushhour.get_board_size())
    #properly, this function should work irrespective of how you represent
    #your state.
    (m, n) = board_properties[0]
    board = [list(['.'] * n) for i in range(m)]
    for vs in vehicle_statuses:
        for i in range(vs[2]):  # vehicle length
            if vs[3]:
                # vehicle is horizontal
                board[vs[1][1]][(vs[1][0] + i) % n] = vs[0][0]
                # represent vehicle as first character of its name
            else:
                # vehicle is vertical
                board[(vs[1][1] + i) % m][vs[1][0]] = vs[0][0]
                # represent vehicle as first character of its name
    # print goal
    goal = board[board_properties[1][1]][board_properties[1][0]] 
    if (goal == '.'):   #check if no other vehicle is in this position
        board[board_properties[1][1]][board_properties[1][0]] = board_properties[2]
    return board    
    

def test(nvehicles, board_size):
    s0 = make_rand_init_state(nvehicles, board_size)
    s0.print_state()
    print ('\n')
    se_1 = SearchEngine('astar', 'full')
    se_2 = SearchEngine('best_first', 'full')
    #se.trace_on(2)
    final = se_1.search(s0, rushhour_goal_fn, heur_min_moves)
    print ('\n')
    final = se_2.search(s0, rushhour_goal_fn, heur_min_moves)