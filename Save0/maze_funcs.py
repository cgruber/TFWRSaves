def is_treasure():
  return get_entity_type() == Entities.Treasure

def find_treasure():
  dirs = [North, West, South, East]
  if get_entity_type() == Entities.Treasure:
    return
  descend([], dirs)

def scan_plot(facing, path):
  prev = flat_here()
  move(facing)
  #quick_print("Moving ", facing, path, flat_here())
  if is_treasure():
    return
  elif flat_here() == prev: # wall
    return    
  elif flat_here() in path:
    move(opposite(facing)) # bounce
    return
  else:
    dirs = [left(facing), facing, right(facing)]
    descend(path, dirs)
    if not is_treasure():
      move(opposite(facing)) # done, so back up
      
def descend(path, dirs):
  path.append(flat_here())
  for dir in dirs:
    scan_plot(dir, path)
    if is_treasure():
      return
  #path.pop()    

def solve_maze(reuse):
  move_to(0,0)
  harvest_and_plant(Entities.Bush)
  wait_for_harvest()
  for i in range(reuse):
    while not get_entity_type() == Entities.Hedge:
      if not num_items(Items.Fertilizer) > 1:
        return False # quit early if no fertilizer
      use_item(Items.Fertilizer)
    find_treasure()
  harvest()
  move_to(0, 0)
 
