<<<<<<< HEAD
from games import Game, Strategic
from developers import Blizzard
from multiple_inheritance import Subclass

class Starcraft(Blizzard, Strategic):
    def __init__(self, platform, board, *args, **kwargs):
        super().__init__(platform, board, *args, **kwargs)
        print("Starcraft")

if __name__ == '__main__':
    print(Starcraft.__mro__)
    g = Starcraft(platform='Windows', board=[128,128], awarded=True)
    print(g.__dict__)
=======
from games import Game, Strategic
from developers import Blizzard
from multiple_inheritance import Subclass

class Starcraft(Blizzard, Strategic):
    def __init__(self, platform, board, *args, **kwargs):
        super().__init__(platform, board, *args, **kwargs)
        print("Starcraft")

if __name__ == '__main__':
    print(Starcraft.__mro__)
    g = Starcraft(platform='Windows', board=[128,128], awarded=True)
    print(g.__dict__)
>>>>>>> b829bcb465b0e32104dbe492037b6da0f67e9948
