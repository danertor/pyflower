import hashlib as hl
import random as rd

class User:
    def __init__(self, username, password):
        '''Create a new user object, the password will be encrypted'''
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password, salt=''):
        '''Encrypt the passowed in the username and return the sha digest'''
        self.salt = ''.join([rd.choice('0123456789ABCDEF') for i in range(16)]) if salt == '' else salt
        print('salt: {}'.format(self.salt))
        hash_string = (self.username + password + self.salt)
        hash_string = hash_string.encode("utf8")
        return hl.sha256(hash_string).hexdigest()

    def check_password(self, password, salt=''):
        '''Return True if the passwrd in valid for this user, False otherwise'''
        salt = self.salt if salt == '' else salt
        encrypted = self._encrypt_pw(password, salt)
        return encrypted == self.password

#Exceptions
class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class PermissionError(AuthException):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


class Authenticator:
    def __init__(self):
        '''Construct and authenticator to manage users loggin in and out.'''
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 8:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError as e:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False


authenticator = Authenticator()


# Authorizor class that maps permisions to users
class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        '''create a new permission that users can be added to'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        '''Grant the given permission to the user'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError as e:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

authorizor = Authorizor(authenticator)




