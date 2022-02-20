class User:
    '''
    A class that generate new instances of users
    '''
    user_list = []

    def __init__(self,app_name, user_name,password):
        self.user_name = user_name
        self.app_name = app_name
        self.password = password

    def save_user(self):

        '''
        A method that save an instance of a user in the user list
        '''
        User.user_list.append(self)

    def delete_user(self,account):

        '''
        A method that save an instance of a user in the user list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_appName(cls,app_name):
        '''
        Method that takes in a application name and return a string that matches that name
        Args:
            appName: appName to search for
        Returns :
            matching account username
        '''
        for login in cls.credentials_list:
            if login.app_name == app_name:
                return login