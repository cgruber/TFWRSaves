def water():
    if get_water() < 0.8 and num_items(Items.Water) > 5:
        use_item(Items.Water)
        