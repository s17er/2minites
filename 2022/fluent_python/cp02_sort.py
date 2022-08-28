
def main():
    fruits = ['grape', 'rasberry', 'apple', 'banana']
    print(sorted(fruits))
    print(fruits)
    print(sorted(fruits, reverse=True))
    print(sorted(fruits, key=len))
    fruits.sort()
    print(fruits)
    
if __name__ == '__main__':
    main()