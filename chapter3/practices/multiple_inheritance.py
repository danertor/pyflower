class BaseClass:
    num_base_calls = 0
    def call_me(self, num_base_calls, *args):
        print("Calling method on {3}: first: {0}, args: {1} : {2}".format(num_base_calls, args,  '',self.__class__.__name__))
        self.num_base_calls = num_base_calls


class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self, num_left_calls, *args ):
        super().call_me(args )
        print("Calling method on {3}: first: {0}, args: {1} : {2}".format(num_left_calls, args,  '',self.__class__.__name__))
        self.num_left_calls = num_left_calls


class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self, num_right_calls, *args ):
        super().call_me(args )
        print("Calling method on {3}: first: {0}, args: {1} : {2}".format(num_right_calls, args,  '',self.__class__.__name__))
        self.num_right_calls = num_right_calls


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self, num_sub_calls, *args ):
        super().call_me(args )
        print("Calling method on {3}: first: {0}, args: {1} : {2}".format(num_sub_calls, args,  '',self.__class__.__name__))
        self.num_sub_calls = num_sub_calls

s = Subclass()
s.call_me(3, 2, 1, 0)
print(s.num_base_calls, s.num_right_calls, s.num_left_calls, s.num_sub_calls)