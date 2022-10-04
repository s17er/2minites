from functools import singledispatch
import html
import numbers

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br/>\n')
    return '<pre>{0}</pre>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

if __name__ == '__main__':
    print(htmlize( 'hello\nworld'))
    print(htmlize(500))