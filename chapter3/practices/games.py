<<<<<<< HEAD
class Game:
    def __init__(self, platform, *args, **kwargs):
        super().__init__()
        print("Game")
        self.platform = platform
        if 'awarded' in kwargs:
            self.awarded = kwargs['awarded']


class Strategic(Game):
    def __init__(self, platform, board, *args, **kwargs):
        super().__init__(platform, *args, **kwargs)
        self.board = board
        print("Strategic")


class Fps(Game):
    def __init__(self, platform, threed, *args, **kwargs):
        self.threeD = threed
        print("Fps")
=======
class Game:
    def __init__(self, platform, *args, **kwargs):
        super().__init__()
        print("Game")
        self.platform = platform
        if 'awarded' in kwargs:
            self.awarded = kwargs['awarded']


class Strategic(Game):
    def __init__(self, platform, board, *args, **kwargs):
        super().__init__(platform, *args, **kwargs)
        self.board = board
        print("Strategic")


class Fps(Game):
    def __init__(self, platform, threed, *args, **kwargs):
        self.threeD = threed
        print("Fps")
>>>>>>> b829bcb465b0e32104dbe492037b6da0f67e9948
