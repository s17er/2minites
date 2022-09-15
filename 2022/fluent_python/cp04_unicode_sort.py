def unicode_sort(l):
    print(sorted(l))

def unicode_sort2(l):
    import locale
    #locale.setlocale(locale.LC_COLLATE, 'ja_JP.UTF-8')
    locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
    print(sorted(l, key=locale.strxfrm))

if __name__ == '__main__':
    l = ['りんご', 'アップル', 'みかん', 'グレープ']
    unicode_sort2(l)