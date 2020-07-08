def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_list = [apple + a for apple in apples]
    orange_list = [orange + b for orange in oranges]
    apples_in_house = [apple_num for apple_num in apple_list if apple_num >= s and apple_num <= t]
    oranges_in_house = [orange_num for orange_num in orange_list if orange_num >= s and orange_num <= t]
    print( len(apples_in_house), len(oranges_in_house), sep="\n" )



countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])
