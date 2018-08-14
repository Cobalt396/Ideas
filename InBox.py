def in_Box(x, box_width, grid_width):
    '''Returns True if in box.'''
    total = box_width + grid_width
    crit_ratio = box_width / total
    
    if ((x / total) - (x // total)) < crit_ratio:
        return True
    return False

def Bounds_1D(x, box_width, grid_width):
    '''Returns a tuple of the bound the square box in one dimension.'''
    total = box_width + grid_width
    lower_bound = (x // total) * total

    upper_bound = lower_bound + box_width

    return lower_bound, upper_bound

def Bounds_2D(x, y, box_width, grid_width):
    '''Returns the list of the 4 coordinates that bound the box.'''
    x_l, x_u = Bounds_1D(x, box_width, grid_width)
    y_l, y_u = Bounds_1D(y, box_width, grid_width)

    return [(x_l, y_l), (x_u, y_l), (x_l, y_u), (x_u, y_u)]

def main():
    test1 = in_Box(90, 20, 5)
    test2 = in_Box(97, 20, 5)
    test3 = Bounds_1D(90, 20, 5)
    test4 = Bounds_1D(40, 20, 5)
    test5 = Bounds_2D(90, 40, 20, 5)

    print(test1, test2)
    if test1 == True and test2 == False:
        print('test 1 and 2 passed.')
    else:
        print('test 1 and 2 failed.')
        
    print(test3)
    if test3 == (75, 95):
        print('test 3 passed.')
    else:
        print('test 3 failed.')
        
    print(test4)
    if test4 == (25, 45):
        print('test 3 passed.')
    else:
        print('test 3 failed.')
        
    print(test5)
    if test5 == [(75, 25), (95, 25), (75, 45), (95, 45)]:
        print('test 3 passed.')
    else:
        print('test 3 failed.')
        
main()
