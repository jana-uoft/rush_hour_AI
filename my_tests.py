from rushhour import *


def print_state(s):
    board = get_board_2(s.get_vehicle_statuses(), s.get_board_properties())
    print (s.action)
    for row in board:
        print (row)
    print ('')    


def test_successors(s):
    print_state(s)
    
    for i in s.successors():
        test_heuristics(i)
        print_state(i)
        
        
        
        
def test_heuristics(s):
    print (heur_min_moves(s))
    
    
def test_goals(s):
    return rushhour_goal_fn(s)


if __name__ == '__main__':

    #se.trace_on(1)
    
    vehicle_list_1 = [['g',(0,1),2,True,True],
                      ['1',(2,0),2,False,False],
                      ['2',(0,3),2,True,False],
                      ['3',(2,4),2,False,False]]
    
    goal_list_1 = [['g',(2,1),2,True,True],
                      ['1',(2,2),2,False,False],
                      ['2',(0,3),2,True,False],
                      ['3',(2,4),2,False,False]]
    
    goal_list_2 = [['g',(2,1),2,True,True],
                      ['1',(2,6),2,False,False],
                      ['2',(2,3),2,True,False],
                      ['3',(2,4),2,False,False]]
    
    goal_list_3 = [['g',(2,1),2,True,True],
                      ['1',(2,2),2,False,False],
                      ['2',(1,3),2,True,False],
                      ['3',(2,4),2,False,False]]
    
    goal_list_4 = [['g',(2,1),2,True,True],
                      ['1',(2,2),2,False,False],
                      ['2',(0,3),2,True,False],
                      ['3',(2,5),2,False,False]]
    
    board_size_1 = (7, 4)
    goal_entrance_1 = (3, 1)
    goal_orientation_1 = 'E'    
    s1 = make_init_state(board_size_1, vehicle_list_1, goal_entrance_1, goal_orientation_1)
    
    g1 = make_init_state(board_size_1, goal_list_1, goal_entrance_1, goal_orientation_1)
    g2 = make_init_state(board_size_1, goal_list_2, goal_entrance_1, goal_orientation_1)
    g3 = make_init_state(board_size_1, goal_list_3, goal_entrance_1, goal_orientation_1)
    g4 = make_init_state(board_size_1, goal_list_4, goal_entrance_1, goal_orientation_1)
    
  

    vehicle_list_2 = [['g',(1,2),2,False,True],
                      ['1',(0,5),2,True,False],
                      ['2',(3,4),2,False,False],
                      ['3',(1,1),2,True,False]]
    board_size_2 = (7, 4)
    goal_entrance_2 = (1, 6)
    goal_orientation_2 = 'S'    
    s2 = make_init_state(board_size_2, vehicle_list_2, goal_entrance_2, goal_orientation_2)

    
    

    vehicle_list_3 = [['g',(0,3),2,True,True],
                      ['1',(4,2),2,False,False],
                      ['2',(2,5),2,False,False],
                      ['3',(1,1),2,True,False]]
    board_size_3 = (7, 5)
    goal_entrance_3 = (3, 3)
    goal_orientation_3 = 'W'    
    s3 = make_init_state(board_size_3, vehicle_list_3, goal_entrance_3, goal_orientation_3)

    
    

    vehicle_list_4 = [['g',(2,3),2,False,True],
                      ['1',(0,4),2,True,False],
                      ['2',(1,1),2,True,False],
                      ['3',(4,1),2,False,False]]
    board_size_4 = (5, 5)
    goal_entrance_4 = (2, 0)
    goal_orientation_4 = 'N'    
    s4 = make_init_state(board_size_4, vehicle_list_4, goal_entrance_4, goal_orientation_4)

    
    
    
    vehicle_list_5 = [['g',(0,3),2,True,True],
                      ['1',(3,2),2,False,False],
                      ['2',(0,0),2,True,False],
                      ['3',(2,4),2,False,False]]
    board_size_5 = (6, 4)
    goal_entrance_5 = (2, 3)
    goal_orientation_5 = 'W'    
    s5 = make_init_state(board_size_5, vehicle_list_5, goal_entrance_5, goal_orientation_5)

    
    
    
    vehicle_list_6 = [['g',(3,3),2,True,True],
                      ['1',(2,1),2,False,False]]
    board_size_6 = (6, 5)
    goal_entrance_6 = (2, 5)
    goal_orientation_6 = 'S'    
    s6 = make_init_state(board_size_6, vehicle_list_6, goal_entrance_6, goal_orientation_6)

    
    vehicle_list_7 = [['g',(0,3),2,True,True]]
    board_size_7 = (6, 5)
    goal_entrance_7 = (4, 3)
    goal_orientation_7 = 'E'    
    s7 = make_init_state(board_size_7, vehicle_list_7, goal_entrance_7, goal_orientation_7)
    

    vehicle_list_8 = [['g',(4,3),2,False,True],
                      ['1',(0,2),2,True,False],
                      ['2',(1,5),3,False,False],
                      ['3',(2,1),2,True,False],
                      ['4',(5,4),2,True,False],
                      ['5',(3,5),2,False,False],
                      ['6',(5,1),2,True,False],
                      ['7',(4,0),3,True,False],  
                      ['8',(3,2),2,True,False],
                      ['9',(0,3),3,True,False]]
    board_size_8 = (6, 6)
    goal_entrance_8 = (4, 1)
    goal_orientation_8 = 'S'    
    s8 = make_init_state(board_size_8, vehicle_list_8, goal_entrance_8, goal_orientation_8)
    

    vehicle_list_9 = [['g',(2,2),2,True,True],
                      ['1',(0,1),2,False,False],
                      ['2',(1,4),2,False,False],
                      ['3',(2,3),2,False,False],
                      ['4',(3,0),2,False,False],
                      ['5',(4,0),3,False,False],
                      ['6',(5,0),3,False,False],
                      ['13',(0,0),3,True,False],  
                      ['14',(1,1),2,True,False],
                      ['16',(0,3),2,True,False],
                      ['17',(4,4),2,True,False],
                      ['18',(2,5),2,True,False],
                      ['24',(4,5),2,True,False]]
    board_size_9 = (6, 6)
    goal_entrance_9 = (5, 2)
    goal_orientation_9 = 'E'    
    s9 = make_init_state(board_size_9, vehicle_list_9, goal_entrance_9, goal_orientation_9)
    

    vehicle_list_10 = [['g',(1,3),5,True,True]]
    board_size_10 = (6, 5)
    goal_entrance_10 = (3, 3)
    goal_orientation_10 = 'W'    
    s10 = make_init_state(board_size_10, vehicle_list_10, goal_entrance_10, goal_orientation_10)
    
    
    vehicle_list_11 = [['g',(2,2),2,True,True],
                      ['1',(0,1),2,False,False],
                      ['2',(1,4),2,False,False],
                      ['3',(2,3),2,False,False],
                      ['4',(3,0),2,False,False],
                      ['5',(4,1),3,False,False],
                      ['6',(5,0),3,False,False],
                      ['13',(0,0),3,True,False],  
                      ['14',(1,1),2,True,False],
                      ['16',(0,3),2,True,False],
                      ['17',(4,4),2,True,False],
                      ['18',(2,5),2,True,False],
                      ['24',(4,5),2,True,False],
                      ['a',(0,0),6,True,False],
                      ['b',(0,1),6,False,False],
                      ['c',(1,6),6,True,False],
                      ['d',(6,0),6,False,False]]
    board_size_11 = (8, 7)
    goal_entrance_11 = (5, 2)
    goal_orientation_11 = 'E'    
    s11 = make_init_state(board_size_11, vehicle_list_11, goal_entrance_11, goal_orientation_11)
    
    
    vehicle_list_12 = [['g',(1,3),3,True,True],
                       ['w',(5,4),1,True,False]]
    board_size_12 = (6, 6)
    goal_entrance_12 = (2, 3)
    goal_orientation_12 = 'E'    
    s12 = make_init_state(board_size_12, vehicle_list_12, goal_entrance_12, goal_orientation_12)


    vehicle_list_13 = [['g',(6,2),2,False,True],
                       ['1',(3,1),2,True,False],
                       ['2',(4,5),2,False,False],
                       ['3',(3,5),2,False,False],
                       ['4',(6,0),2,False,False],
                       ['5',(0,0),2,True,False],
                       ['6',(0,4),3,True,False],
                       ['7',(2,2),2,True,False],
                       ['8',(1,6),2,True,False]]
    board_size_13 = (7, 7)
    goal_entrance_13 = (6, 6)
    goal_orientation_13 = 'N'    
    s13 = make_init_state(board_size_13, vehicle_list_13, goal_entrance_13, goal_orientation_13)


    vehicle_list_14 = [['g',(2,3),2,False,True],
                       ['1',(3,0),3,False,False],
                       ['2',(4,0),2,True,False],
                       ['3',(5,1),3,False,False],
                       ['4',(0,2),3,True,False],
                       ['5',(0,3),2,False,False],
                       ['6',(3,3),2,True,False],
                       ['7',(0,5),3,True,False]]
    board_size_14 = (6, 6)
    goal_entrance_14 = (2, 0)
    goal_orientation_14 = 'N'    
    s14 = make_init_state(board_size_14, vehicle_list_14, goal_entrance_14, goal_orientation_14)
    

    vehicle_list_15 = [['g',(1,3),6,True,True]]
    board_size_15 = (6, 6)
    goal_entrance_15 = (2, 3)
    goal_orientation_15 = 'W'    
    s15 = make_init_state(board_size_15, vehicle_list_15, goal_entrance_15, goal_orientation_15)
    
    s16 = make_init_state((7, 7), [['gv', (1, 1), 2, True, True], ['1', (3, 1), 2, False, False], ['3', (4, 4), 2, False, False]], (4, 1), 'E')
    
    s17 = make_init_state((7,7), [['gv', (6, 3), 2, True, True], ['1', (6, 0), 2, False, False], ['2', (4, 6), 2, False, False], ['3', (0, 6), 3, True, False]], (3,3), 'E')
    #print_state(s8)
    #test_successors(s7)
    #test_heuristics(s8)
    
    
    se = SearchEngine('astar', 'full')
    #se.trace_on(2)
    final = se.search(s17, rushhour_goal_fn, heur_min_moves)
    
    
    
    #print("=========Test 1. Astar with h_min heuristic========")
    #se.search(s8, rushhour_goal_fn, heur_min_moves)
    #print("===================================================")
    #print("")
    
    
    #se.set_strategy('breadth_first')
    #print("=========Test 3a. Breadth first (full cycle checking)==")
    #se.search(s8, rushhour_goal_fn)
    #print("===================================================")
    #print("")
    
    #se.set_strategy('breadth_first', 'path')
    #print("=========Test 3a. Breadth first with only path checking=====")
    #se.search(s8, rushhour_goal_fn)
    #print("===================================================")
    #print("")
    
    #se.set_strategy('breadth_first', 'none')
    #print("=========Test 3a. Breadth first with no cycle checking=====")
    #se.search(s8, rushhour_goal_fn)
    #print("===================================================")
    #print("")
    

    #se.set_strategy('breadth_first', 'path')
    #print("=========Test 4. Breadth first on unreachable goal with only path checking==")
    #se.search(s7, rushhour_goal_fn)
    #print("========================================================")
    #print("")
    
    #se.set_strategy('breadth_first', 'full')
    #print("=========Test 5. Breadth first on unreachable goal with full checking==")
    #se.search(s7, rushhour_goal_fn)
    #print("========================================================")
    #print("")
    
    #se.set_strategy('depth_first')

    #print("=========Test 6. Depth first on unreachable goal with path checking==")
    #se.search(s7, rushhour_goal_fn)
    #print("========================================================")
    #print("")
    
    
    
    
    
    