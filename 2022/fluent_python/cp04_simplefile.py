def save_and_load():
    open('cafe.txt', 'w', encoding='utf-8').write('café')
    print(open('cafe.txt').read()) # encode depend on OS
    
def print_expressions():
    import sys, locale
    expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
    
    my_file = open('dummy', 'w')
    
    for expression in expressions.split():
        value = eval(expression)
        print(expression.rjust(30), '->', value)
    
if __name__ == '__main__':
    save_and_load()
    print_expressions()