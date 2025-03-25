from math import even
from math import odd
from watering import water
from globals import world_size

def smart_harvest():
    while get_entity_type() and not can_harvest():
        pass # wait
    if get_entity_type():
        harvest()
        
def plant_entity(entity):
    if entity["till_soil"] and get_ground_type() == Grounds.Grassland:
        till()
    #quick_print("(x, y)", even(get_pos_x()), even(get_pos_y()))   
    if not entity["plant_separately"] or even(get_pos_x()) != odd(get_pos_y()):
        plant(entity["key"])
    else:
        plant(Entities.Grass) # fill in the gaps

def loop(entity):
    for y in range(world_size):
        for x in range(world_size):
            smart_harvest()
            water()
            plant_entity(entity)
            move(North)
        move(East)
            