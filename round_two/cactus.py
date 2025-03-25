import planting
from watering import water
from globals import world_size
from globals import plots
from globals import opposites
from move import here
from move import move_to
from planting import smart_harvest
from planting import plant_entity

def swap_if(direction):
    changed = False
    height = measure()
    next = measure(direction)
    last = measure(opposites[direction])
    if next == None:
        return
    if height == None:
        plant_entity(Entities.Cactus)
    if height > next:
        swap(direction)
        changed = True
        if last > next:
            swap(opposites[direction])
    else:
         if last > height:
            swap(opposites[direction]) 
            changed = True
    return changed

def sort_in_direction(direction):
    done = False
    while not done:
        done = True
        for x in range(world_size - 2):
            done = not swap_if(direction) and done
            move(direction)
        move(direction)
        move(direction)

def sort_cacti():
    for y in range(world_size):
        move_to(1, y)
        side_direction = North
        if y >= world_size-1:
            side_direction = None
        sort_in_direction(East)
    for x in range(world_size):
        move_to(x, 1)
        side_direction = East
        if x >= world_size-1:
            side_direction = None
        sort_in_direction(North)

def loop(entity):
    planting.loop(entity)
    sort_cacti()
    move_to(world_size-1, world_size-1)
    smart_harvest()
