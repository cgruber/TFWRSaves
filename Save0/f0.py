globs = create_globs()
clear()
farm_size = 7
iterations = 5
algorithms =  [
  swap_line_same_direction,
  swap_line_back_and_forth, 
  swap_line_back_and_forth_dim,
]
get_seeds(Items.Cactus_Seed, square(farm_size) * len(algorithms) * iterations)
set_farm_size(farm_size)
quick_print("Benchmark with farm size", farm_size, "and iterations", iterations)
for algo in algorithms:
  quick_print("**********")  quick_print("Testing algorithm", algo)
  cost = 0
  time = 0
  for i in range(iterations):
    get_seeds(Items.Cactus_Seed, plots())
    head = get_op_count()
    head_time = get_time()
    cactus_field_with(algo)
    cost = cost + get_op_count() - head
    time = time + get_time() - head_time
  avg = cost / iterations
  avg_time = time / iterations
  quick_print("  Average cost in ops: ", avg)
  quick_print("  Average run-time: ", avg_time)

#unlock_levels([Unlocks.Speed], True)
#clear()
#create_bones(3000)
