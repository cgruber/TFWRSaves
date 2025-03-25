def plant_trees():	
  def plant_tree(x, y, state):
    harvest_and_plant(Entities.Tree)
    return None
  walk_checkerboard(plant_tree, None)
  wait_for_harvest()
            