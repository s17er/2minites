def color_priority():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)
    
    t = ('%s %s' % (c, s) for c in colors for s in sizes)
    
    print( ( i for i in range(1, 10) ) ) # -> generator
    print( i for i in range(1, 10) ) # -> generator
    print( [ i for i in range(1, 10) ] ) # -> list

    print( (color, size) for color in colors for size in sizes )
    print(t)
    
def size_priority():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(size, color) for color in colors for size in sizes]
    print(tshirts)
    
if __name__ == '__main__':
    color_priority()
    #size_priority()
