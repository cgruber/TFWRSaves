import planting
from watering import water
from globals import world_size
from globals import power_threshold
from move import here
from move import move_to
from planting import smart_harvest

def scan_flowers():
    flowers = dict()
    for petals in range(7, 16):
        flowers[petals] = []
    for y in range(world_size):
        for x in range(world_size):
            move(North)
            flowers[measure()].append(here())
        move(East)
    return flowers    
    
def loop(entity):
    if num_items(Items.Power) > power_threshold:
        quick_print("Power at ", num_items(Items.Power), "/", power_threshold, "... skipping.")  
        return
    planting.loop(entity)
    petals_index = scan_flowers()
    #quick_print(petals_index)
    for petals in range(15, 8, -1):
        # TODO: Optimize on nearest?
        for x, y in petals_index[petals]:
            move_to(x, y)
            smart_harvest()
