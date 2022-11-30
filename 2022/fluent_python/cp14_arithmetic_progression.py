
class ArithmeticPregression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end # None -> "inifinite" series
        
    def __iter__(self):
        # cast to larger class begin or step.
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


if __name__ == '__main__':
    ap = ArithmeticPregression(0, 1, 3)
    print(list(ap))
    ap = ArithmeticPregression(1, .5, 3)
    print(list(ap))
