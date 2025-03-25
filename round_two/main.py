import pumpkins
import planting
import power
import cactus
import globals
from move import move_to
from mgmt import entities



move_to(0, 0)
             

def main_loop():
    for type in entities:
        entity = entities[type]    
        #quick_print("Planting ", entity[0])
        move_to(0, 0) # return to origin
        logic = entity["logic"]
        logic(entity)

#start = get_time()
#main_loop()
#diff = get_time() - start
#quick_print("Executed in ", get_tick_count(), " steps and ", diff , " seconds.")

        
while True:
    start = get_time()
    main_loop()
    diff = get_time() - start
    quick_print("Executed in", diff , "seconds.", diff/globals.plots, " seconds/plot.")
    