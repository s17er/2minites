class HauntedBus:
    def __init__(self, passengers=[]) -> None:
        # bad
        self.passengers = passengers
            
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)

if __name__ == '__main__':
    bus1 = HauntedBus(['Apple', 'Bell', 'Car', 'Dart'])
    bus1.pick('End')
    bus1.drop('Apple')
    print(bus1.passengers)
    
    bus2 = HauntedBus()
    print('bus2 before init ', HauntedBus.__init__.__defaults__)
    bus2.pick('Who')
    print(bus2.passengers)
    print('bus2 after init ',HauntedBus.__init__.__defaults__)
    
    bus3 = HauntedBus()
    print(bus3.passengers)
    
    bus3.pick('Zzz')
    print(bus1.passengers)
    print(bus2.passengers)
    print(bus3.passengers)
    print(bus2.passengers is bus3.passengers) # True
    