def rest_wood(forest_volume, warehouse):
    preparation = forest_volume * 70 / 100
    warehouse -= preparation
    print('Залишок деревини на складі:', warehouse, 'м3')
    return warehouse


warehouse = 2000
volume = int(input("Кількість готових стільців (шт): "))
warehouse = rest_wood(volume, warehouse)
volume = int(input("Кількість готових стільців (шт): "))
warehouse = rest_wood(volume, warehouse)
