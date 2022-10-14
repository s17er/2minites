
class TwilightBus:
    def __init__(self, passengers=None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
            
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)
        
if __name__ == '__main__':
    team = ['A', 'B', 'C', 'D']
    bus = TwilightBus(team)
    bus.drop('C')
    print(team) # remove from team!
    
    l = [1, 2]
    l2 = list(l)
    print(l == l2)
    print(l is l2)