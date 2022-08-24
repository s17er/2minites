import random
import string

def gen(length=16):
    total = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.sample(total, length))

if __name__ == '__main__':
    print(gen(8))