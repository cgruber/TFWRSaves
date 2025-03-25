import pumpkins
import planting
import power
import cactus
import globals
from move import move_to
from mgmt import entities



move_to(0, 0)
             

def loop_entities(round):
    for type in entities:
        entity = entities[type]    
        #quick_print("Planting ", entity[0])
        move_to(0, 0) # return to origin
        logic = entity["logic"]
        start_ticks = get_tick_count()
        start_time = get_time()
        logic(entity)
        work = get_tick_count() - start_ticks
        duration = get_time() - start_time
        entity["metrics"].append((work, duration))
        quick_print("     Run: ", round, type, work, "steps", duration, "seconds")
        
#start = get_time()
#main_loop()
#diff = get_time() - start
#quick_print("Executed in ", get_tick_count(), " steps and ", diff , " seconds.")

def avg(metrics, field):
    sum = 0
    for m in metrics:
        sum += m[field]
    return sum / len(metrics)
    
def avg_time(metrics):
    pass

def main():
    count = 5
    start = get_time()
    for x in range(count):
        quick_print("Round", x)
        loop_entities(x)
    diff = get_time() - start
    for key in entities:
        entity = entities[key]
        quick_print(entity["key"], "avg work:",avg(entity["metrics"], 0), "avg duration:", avg(entity["metrics"], 1), "seconds.")
    quick_print("Total executed in", diff , "seconds.", diff/globals.plots/count, " seconds/plot/round.")

main()