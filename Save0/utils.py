def walk(func, state):
  for x in range(get_world_size()):
    for y in range(get_world_size()):
      state = func(x, y, state)
      move(North)
    move(East)
  return state

def walk_checkerboard(func, state):
  toggle = False
  for x in range(get_world_size()):
    toggle = x % 2 == 0
    for y in range(get_world_size()):
      toggle = not toggle
      if not toggle:
        state = func(x, y, state)
      move(North)
    move(East)
  return state

def harvest_and_plant(type):
  harvest()
  if type in globs["tillable"] and get_ground_type() != Grounds.Soil:
    till()
  if get_entity_type() != type:
    plant(type)
  #do_a_flip()
  if get_water() < 0.5 and num_items(Items.Water_Tank) > 0:
    use_item(Items.Water_Tank)

def wait_for_harvest():
  while not can_harvest() and not get_entity_type() == None:
    do_a_flip()

def buy_up_to(qty, seed):
  if seed != None: # We might not execute this on all types.
    if num_items(seed) < qty:
      trade(seed, qty - num_items(seed))
      return True
    if num_items(seed) < qty:
      print("Could not buy ", qty, seed)
      return False