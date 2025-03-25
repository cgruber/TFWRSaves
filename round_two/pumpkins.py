from watering import water
from planting import smart_harvest
from planting import plant_entity
from globals import world_size
from globals import plots

# TODO: Optimize on dead pumpkin plots.
def loop(entity):
    pumpkins = 0
    while pumpkins < plots:
        pumpkins = 0
        for y in range(world_size):
           for x in range(world_size):
               if get_entity_type() != Entities.Pumpkin:
                   smart_harvest()
                   water()
                   plant_entity(entity)
               else:
                   pumpkins +=1
               move(North)
           move(East) 
    #do_a_flip() # Delay for the last pumpkin.
    harvest()