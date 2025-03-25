def test_sort_empty_set():
  set = { }
  list = sort_set(set, True)
  print(list)

def test_sort_text():
  set = { "c", "b", "d" }
  list = sort_set(set, True)
  print(list)

def test_sort_numbers():
  set = { 9, 3, 6, 2 }
  list = sort_set(set, True)
  print(list)

def test_sort_rever():
  set = { 9, 3, 6, 2 }
  list = sort_set(set, True)
  print(list)

def test_sort_dict_keys():
  dict = {Items.Wood:"foo", Items.Carrot:"blah"}
  list = sort_set(dict, True)
  print(list)

def test_sort_dict_keys_reverse():
  dict = {Items.Wood:"foo", Items.Carrot:"blah"}
  list = sort_set(dict, False)
  print(list)

def test_swap():
  list = [ 1, 2, 3, 4 ]
  swap_elements(list, 1, 3)
  print(list == [ 1, 4, 3, 2 ])	

def test_swap_items():
  dict = {Items.Wood:"foo", Items.Carrot:"blah"}
  list = to_list(dict)
  swap_elements(list, 0, 1)
  print(list == [ Items.Carrot, Items.Wood ])	
  
def test_new_list_from():
  list = [ 1, 2, 3, 4 ]
  list2 = new_list_from(list)  
  swap_elements(list, 0, 1) 
  print(list == [2, 1, 3, 4])
  print(list2 == [1, 2, 3, 4])	

def test_reverse_list():
  list = [ 1, 2, 3, 4 ]
  list2 = reverse_list(list)  
  print(list == list2)
  print(list2 == [4, 3, 2, 1])	
    
def test_operators():
  print(Items.Wood == Items.Carrot)
  print(Items.Wood > Items.Carrot)
  print(Items.Wood < Items.Carrot)

test_reverse_list()

  