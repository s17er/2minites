def main():
    t = (1, 2, [30, 40])
    t[2] += [50, 60]
    print(t)  # -> error? or t[2] is [30, 40, 50, 60] ?
    
def main2():
    t = (1, 2, [30, 40])
    t[2].extend([50, 60])
    print(t)
    

if __name__ == '__main__':
    main()
