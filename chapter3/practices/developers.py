class Blizzard:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Blizzard")
        print('*args {}'.format([e for e in args]))
        print('**kwargs {}'.format(kwargs))
        self.platform = "Battle.net"
