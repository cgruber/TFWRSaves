def plant_crops(type, seed, seed_qty):
  if not buy_up_to(seed_qty, seed):
    return
  def do_simple_plant(x, y, state):
    harvest_and_plant(type)
    return None
  walk(do_simple_plant, None)