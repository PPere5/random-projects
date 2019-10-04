class cube(object):

    def __init__(self, color, size):
        self.color = color
        self.size=size


class stack(object):

    def __init__(self, label, cubes):
        self.cubes = cubes
        self.label = label
        self.list_cubes = [f"cube({cube_obj.color},{cube_obj.size})" for cube_obj in cubes]

    def number_of_cubes(self):
        return len(self.cubes)


    def add_cube(self, cube_obj):

        if self.cubes!=[]:
            largerq= (self.cubes[-1].size > cube_obj.size)
        else:
            largerq= False
        
        if ((self.cubes==[]) | largerq):
            self.cubes.append(cube_obj)
            self.list_cubes.append(f"cube({cube_obj.color},{cube_obj.size})")
        else:
            print('Cannot add larger cube on top of small one!')
    
    def remove_top_cube(self):
        if self.cubes!=[]:
            self.cubes.pop()
            self.list_cubes.pop()

    def top_cube(self):
        if self.cubes!=[]:
            return self.cubes[-1]
        else:
            return None

class game(object):

    def __init__(self, stacks):
        self.stacks = stacks
        self.list_stacks = [f"stack({stack_obj.label})" for stack_obj in stacks]

    def number_of_cubes_in_game(self):
        return sum([len(sta.cubes) for sta in self.stacks])

    def number_of_stacks_in_game(self):
        return len(self.stacks)

    def first_stack(self):
        return self.stacks[0]

    def last_stack(self):
        return self.stacks[-1]

    def add_stack(self, stack_obj):
        self.stacks.append(stack_obj)
        self.list_stacks.append(f"stack({stack_obj.label})")

    def stack_in_game(self, stack_obj):
        return stack_obj in self.stacks

    def allowed_move(self, stack_obj_1, stack_obj_2):
        if stack_obj_1 not in self.stacks:
            print('stack_obj_1 not in self.stacks')
            return False

        if stack_obj_2 not in self.stacks:
            print('stack_obj_2 not in self.stacks')
            return False

        if stack_obj_1.cubes==[]:
            print('stack_obj_1 is empty')
            return False
        elif stack_obj_2.cubes==[]:
            return True
        elif stack_obj_1.top_cube().size > stack_obj_2.top_cube().size:
            print('cannot move larger cube on top of small cube')
            return False
        else:
            return True

    def move_cube(self, stack_obj_1, stack_obj_2):
        if not isinstance(stack_obj_1, stack):
            print('not stack object')
            return None
        if not isinstance(stack_obj_2, stack):
            print('not stack object')
            return None

        if self.allowed_move(stack_obj_1, stack_obj_2):
            stack_obj_2.add_cube(stack_obj_1.top_cube())
            stack_obj_1.remove_top_cube()
        else:
            print('move not allowed')


    def do_allowed_move(self, stack_obj_1, stack_obj_2):
        if not isinstance(stack_obj_1, stack):
            print('not stack object')
            return None
        if not isinstance(stack_obj_2, stack):
            print('not stack object')
            return None

        if self.allowed_move(stack_obj_1, stack_obj_2):
            self.move_cube(stack_obj_1, stack_obj_2)
        elif self.allowed_move(stack_obj_2, stack_obj_1):
            self.move_cube(stack_obj_2, stack_obj_1)
        else:
            print('no allowed moves for stack objects')
            return None


    def move_stacks(self, start, end, source, target, spare):

        if start==end:
            self.move_cube(source, target)

            #show game current state
            print('\n')
            for sta in self.stacks:
                print(f'stack{self.stacks.index(sta)} cubes: {sta.list_cubes}')

        else:
            self.move_stacks(start+1, end  , source, spare , target)
            self.move_stacks(start  , start, source, target, spare )
            self.move_stacks(start+1, end  , spare , target, source)

        