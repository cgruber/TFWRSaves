import planting
import pumpkins
import power
import cactus

base_entities = [
  # (Entity, Item, Separate, Till, Hat, Logic)
  #(Entities.Grass, Items.Hay, False, False, Hats.Straw_Hat, planting.loop),
  #(Entities.Tree, Items.Wood, True, False, Hats.Straw_Hat, planting.loop),
  #(Entities.Carrot, Items.Carrot, False, True, Hats.Straw_Hat, planting.loop),
  #(Entities.Pumpkin, Items.Pumpkin, False, True, Hats.Straw_Hat, pumpkins.loop),
  #(Entities.Sunflower, Items.Power, False, True, Hats.Straw_Hat, power.loop),
  (Entities.Cactus, Items.Cactus, False, True, Hats.Straw_Hat, cactus.loop),
]

def map_items(entities):
    items = {}
    for entity in entities:
        items[entity[1]] = entity[0]
    return items
items = map_items(base_entities)

deps_cache = {}

def deps(entity):
    if entity in deps_cache:
        return deps_cache[entity]
    else:
        cached = get_cost(entity)
        deps_cache[entity] = cached
        return cached
    
entities = {}

def enrich(base_entity):
    key = base_entity[0]
    enriched = {
        "key": base_entity[0],
        "item": base_entity[1],
        "plant_separately": base_entity[2],
        "till_soil": base_entity[3],
        "hat": base_entity[4],
        "logic": base_entity[5],
        "deps": deps(base_entity[0]),
    }
    entities[key] = enriched

for entity in base_entities:
    enrich(entity)
    
def get_entity():
    return (Entities.Grass, Entities.Grass, False, False, planting.loop)