import thirdpartymod_a
import thirdpartymod_ro

def new_init(self):
    self.a = 77

if __name__ == '__main__':
    thirdpartymod_a.SomeClass.__init__ = new_init
    thirdpartymod_ro.dosomething()

