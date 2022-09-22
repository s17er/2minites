
def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None: # No spaces were found.
        end = len(text)
    return text[0:end].rstrip()

def print_signature(func):
    print(func.__defaults__)
    print(func.__code__)
    print(func.__code__.co_varnames)
    print(func.__code__.co_argcount)

    from inspect import signature
    sig = signature(func)
    print(sig)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

if __name__ == '__main__':
    print_signature(clip)