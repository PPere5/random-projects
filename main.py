from hannoi_structures import cube, stack, game
from solutions import solve_game, solve_game_recursively
from parameters import parameters

#instanciate game
the_game = game([])

#setup stacks
for k in range(parameters.num_of_stacks):
    stack_ins = stack(str(k),[])
    the_game.add_stack(stack_ins)

#setup cubes and add cubes to first stack
for k in range(parameters.num_of_cubes-1,-1,-1):
    cube_ins = cube(str(k), k)
    the_game.first_stack().add_cube(cube_ins)


#solve_game(the_game)

solve_game_recursively(the_game)