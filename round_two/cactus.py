import planting
from watering import water
from globals import world_size
from globals import plots
from move import here
from move import move_to
from planting import smart_harvest
from planting import plant_entity

def swap_if(direction, side_direction):
    changed = False
    height = measure()
    next = measure(direction)
    side = measure(side_direction)
    if next == None:
        return
    if height == None:
        plant_entity(Entities.Cactus)
    if height > next:
        swap(direction)
        changed = True
        if side_direction and next > side:
            swap(side_direction)
    else:
        if side_direction and height > side:
            swap(side_direction)
            changed = True
    return changed

def sort_in_direction(direction, side_direction):
    done = False
    while not done:
        done = True
        for x in range(world_size - 1):
            done = not swap_if(direction, side_direction) and done
            move(direction)
        move(direction)

def sort_cacti():
    for y in range(world_size):
        done = False
        move_to(0, y)
        side_direction = North
        if y >= world_size-1:
            side_direction = None
        sort_in_direction(East, side_direction)
    for x in range(world_size):
        done = False
        move_to(x, 0)
        side_direction = East
        if x >= world_size-1:
            side_direction = None
        sort_in_direction(North, side_direction)

                       
    
def loop(entity):
    planting.loop(entity)
    sort_cacti()
    move_to(world_size-1, world_size-1)
    smart_harvest()
    do_a_flip()