#import student's function
from rushhour import *
import pdb      # for debugging

def test():
    s0 = make_init_state((7, 8), [['gv', (3, 1), 2, True, True],
              ['1', (6, 1), 3, False, False],
              ['2', (5, 5), 6, False, False],
              ['3', (5, 4), 4, True, False],
              ['4', (1, 0), 3, False, False]], (7, 1), 'E')
    num_states = 6
    car_pos = [['gv', (2, 1), 2, True, True],
              ['1', (6, 0), 3, False, False],
              ['3', (6, 4), 4, True, False],
              ['3', (4, 4), 4, True, False],
              ['4', (1, 1), 3, False, False],
              ['4', (1, 6), 3, False, False]]
    heur_moves = 3
    desired_pos = (6, 1)
    tester( 1, s0, num_states, car_pos, heur_moves, desired_pos )
    
    s1 = make_init_state((7, 8), [['gv', (3, 2), 2, False, True],
              ['1', (2, 1), 3, True, False],
              ['2', (3, 4), 3, True, False],
              ['3', (2, 2), 3, False, False],
              ['4', (5, 1), 3, False, False]], (3, 6), 'N')
    num_states1 = 4
    car_pos1 = [['1', (1,1), 3, True, False],
              ['2', (4, 4), 3, True, False],
              ['3', (2, 3), 3, False, False],
              ['4', (5, 0), 3, False, False]]
    heur_moves1 = 3
    desired_pos1 = (3, 6)
    tester( 2, s1, num_states1, car_pos1, heur_moves1, desired_pos1 )
    
    s2 = make_init_state((8, 5), [['gv', (1, 3), 3, False, True],
                 ['a', (0, 0), 4, True, False],
                 ['b', (0, 1), 3, False, False],
                 ['c', (1, 2), 4, True, False],
                 ['d', (2, 3), 2, True, False],
                 ['e', (3, 4), 3, False, False],
                 ['f', (0, 6), 3, True, False],
                 ['g', (0, 7), 5, True, False]], (1, 1), 'N')
    num_states2 = 5
    car_pos2 = [['a', (1,0), 4, True, False],
              ['a', (4, 0), 4, True, False],
              ['b', (0, 2), 3, False, False],
              ['d', (3, 3), 2, True, False],
              ['f', (4, 6), 3, True, False]]
    heur_moves2 = 2
    desired_pos2 = (1, 1)
    tester( 3, s2, num_states2, car_pos2, heur_moves2, desired_pos2 )
    
    s3 = make_init_state((8, 5), [['gv', (1, 3), 3, False, True],
                 ['a', (0, 0), 4, True, False],
                 ['b', (0, 1), 3, False, False],
                 ['c', (1, 2), 3, True, False],
                 ['d', (2, 3), 2, True, False],
                 ['e', (3, 4), 3, False, False],
                 ['f', (0, 6), 3, True, False],
                 ['g', (0, 7), 4, True, False],
                 ['h', (4, 0), 8, False, False]], (1, 1), 'N')
    num_states3 = 1
    car_pos3 = [['b', (0, 2), 3, False, False]]
    heur_moves3 = 2
    desired_pos3 = (1, 1)
    tester( 4, s3, num_states3, car_pos3, heur_moves3, desired_pos3 )
    
    s4 = make_init_state((7, 8), [['gv', (3, 1), 2, True, True],
              ['gv2', (2, 1), 1, True, True],
              ['1', (6, 2), 2, False, False],
              ['2', (5, 5), 6, False, False],
              ['3', (5, 4), 4, True, False],
              ['4', (0, 0), 3, False, False]], (1, 1), 'E')
    num_states4 = 5
    car_pos4 = [['1', (6, 1), 2, False, False],
              ['gv2', (1,1), 1, True, True],
              ['3', (6, 4), 4, True, False],
              ['3', (4, 4), 4, True, False],
              ['4', (0, 1), 3, False, False],
              ['4', (0, 6), 3, False, False]]
    heur_moves4 = 1
    desired_pos4 = (0, 1)
    tester( 5, s4, num_states4, car_pos4, heur_moves4, desired_pos4 )

    print( "All Tests have passed !!!!!" )

def tester( test_num, state, num_states, car_pos, heur_moves, desired_pos ):
    next_states = state.successors()
    assert len(next_states) == len(car_pos)
    car_count = 0
    for nstate in next_states:
        curr_state_count, new_state_count = 0, 0
        car_pos_copy = [ pos for pos in car_pos ]
        for vehicle in nstate.vehicle_list:
            if vehicle in state.vehicle_list:
                curr_state_count += 1
            elif vehicle in car_pos_copy:
                new_state_count += 1
                car_pos_copy.remove(vehicle)
       
    assert (heur_moves == heur_min_moves(state))
    state.vehicle_list[0][1] = desired_pos
    assert ( rushhour_goal_fn(state) == True )
    
    if( test_num == 5 ):
        state.vehicle_list[0][1] = (3,1)
        state.vehicle_list[1][1] = (1,1)
        assert ( rushhour_goal_fn(state) == True )
        state.vehicle_list[1][1] = (2,1)
        se = SearchEngine('astar', 'full')
        final = se.search(state, rushhour_goal_fn, heur_zero)
    print( "Test " + str(test_num)+ " Passed !!\n")

if __name__ == "__main__":
    test()


