def pumpkin_field():
  count = 0
  if not buy_up_to(plots() * 2, Items.Pumpkin_Seed):
    return
  while count < plots():
    # Cycle planting/counting until we have all plots counted
    def plant_and_count_pumpkins(x, y, count):
      # If a grown pumpkin, count it, otherwise plant one.
      if get_entity_type() == Entities.Pumpkin and can_harvest():
        return count + 1
      else:
        harvest_and_plant(Entities.Pumpkin)
        return count
    count = walk(plant_and_count_pumpkins, 0)
  move_to(0,0)
  wait_for_harvest()                  
  harvest()