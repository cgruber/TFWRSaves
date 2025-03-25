clear()
while True:
  print(
    "Empty tanks: ",
    num_items(Items.Empty_Tank),
    "Tanks: ",
    num_items(Items.Water_Tank),
  )
  while num_items(Items.Water_Tank) + num_items(Items.Empty_Tank) < plots() * 4 :
    trade(Items.Empty_Tank)
    
  # Wait until we have a grass field, to
  # allow everything to start at the
  # origin point.
  wait_for_harvest()
  plant_crops(Entities.Grass, None, None)
  plant_trees()
  for i in range(3):
    plant_crops(Entities.Carrots, Items.Carrot_Seed, plots())
  pumpkin_field()
  solve_simple_maze()
  cactus_field()
  sunflower_field()
  print("Done!")