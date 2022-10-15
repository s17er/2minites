import weakref

class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

def check_weakref_cheese():
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    print(catalog)
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(stock)
    print(sorted(stock.keys()))
    del catalog
    print(sorted(stock.keys()))
    del cheese
    print(sorted(stock.keys()))

def check_weakref():
    a_set = {0, 1}
    wref = weakref.ref(a_set)
    print(wref)
    print(wref())
    a_set = {2, 3, 4}
    print(wref())

if __name__ == '__main__':
    check_weakref()
    check_weakref_cheese()
