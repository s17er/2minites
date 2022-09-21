
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s=%s' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ""
        
    if content:
        return '\n'.join("<%s%s>%s</%s>" % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

if __name__ == '__main__':
    print(tag('br'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='testing', name='img', width='100px'))
    print(tag('img', 'content', width='100px'))
    print(tag('p', 'content', 'content2', cls='class', width='100px'))