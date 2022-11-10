
class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]
    
if __name__ == '__main__':
    # use like sequence
    f = Foo()
    print(f[1])
    print(35 in f)
    for i in f:
        print(i)
    #print(len(f)) # TypeError: object of type 'Foo' has no len()