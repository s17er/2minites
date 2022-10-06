def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')
'''
target = deco(target)
'''

if __name__ == '__main__':
    target() # print 'inner'
    print(target) # print inner function.deleted_product