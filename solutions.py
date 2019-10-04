#solution
def solve_game(game_obj):


    num_moves = 0

    while game_obj.last_stack().number_of_cubes()< game_obj.number_of_cubes_in_game():

        #show game current state
        print('\n')
        for sta in game_obj.stacks:
            print(f'stack{game_obj.stacks.index(sta)} cubes: {sta.list_cubes}')

        game_obj.do_allowed_move(game_obj.stacks[0],game_obj.stacks[1])
        game_obj.do_allowed_move(game_obj.stacks[0],game_obj.last_stack())
        game_obj.do_allowed_move(game_obj.stacks[1],game_obj.last_stack())

        num_moves+=3

    print('\n')    
    print(f'Finished game in {num_moves} moves')

    for sta in game_obj.stacks:
            print(f'stack{game_obj.stacks.index(sta)} cubes: {sta.list_cubes}')


def solve_game_recursively(game_obj):
    game_obj.move_stacks(
        start = 0,
        end = game_obj.number_of_stacks_in_game(),
        source = game_obj.first_stack(),
        target = game_obj.last_stack(),
        spare = game_obj.stacks[1]
        )

    print('\n')    
    print(f'Finished game:')

    for sta in game_obj.stacks:
            print(f'stack{game_obj.stacks.index(sta)} cubes: {sta.list_cubes}')