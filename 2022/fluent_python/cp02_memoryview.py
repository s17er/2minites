import array

def main():
    # This array item is 2byte.
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0]) # -2
    
    # This array item is 1byte.
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    # -> [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
    #     -> FFFE, FFFF, 0000, 0001, 0002

    # 0x0400 -> 1024
    memv_oct[5] = 4
    print(numbers)

if __name__ == '__main__':
    main()