import getpass

class UserManager:
    """
    Simple role-based access control for agent management.
    """
    def __init__(self):
        self.admins = ['root', 'admin', getpass.getuser()]

    def is_admin(self, user=None):
        if user is None:
            user = getpass.getuser()
        return user in self.admins
