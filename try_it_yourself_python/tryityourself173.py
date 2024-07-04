# Ice Cream Stand

# Admin

class IceCreamStand:

    def __init__(self, title):
        """Initialize all variables"""
        self.title = title

    def title_icecreamstand(self):
        """This will lable the ice cream stand"""
        title_icecream = f"{self.title} is now open!"
        return title_icecream

name = IceCreamStand('Jones Ice Cream')
print(name.title_icecreamstand())


class Admin:

    def __init__(self, admin, privileges, users):
        """Initialize variables"""
        self.admin = admin
        self.privileges = privileges
        self.users = users

    def greet_admin(self):
        """Greet the admin"""
        greeting_message = f"{self.admin} You can delete posts,"
        return greeting_message
    
    def admin_privileges(self):
        """What are the admin's privileges?"""
        list_privileges = f"{self.privileges} in this database."
        return list_privileges
    
    def greet_users(self):
        """Greet users"""
        greet_normal_people = f"{self.users} Welcome to the database."
        return greet_normal_people

message = Admin('Hello Admin.', 'ban, and add users', 'Hello Users!')
print(message.greet_admin())
print(message.admin_privileges())
print(message.greet_users())

# This is just __init__ practice.

class Jobs:
    """What jobs do they work?"""

    def __init__(self, Gabe, Mom, Mark):
        """Initialize the variables"""
        self.Gabe = Gabe
        self.Mark = Mark
        self.Mom = Mom

    def gabe_job(self):
        """What is Gabe's job?"""
        css_job = f"Gabe works in the {self.Gabe}!"
        return css_job

    def mom_job(self):
        """What is mom's job?"""
        projmanager = f"Moms job is {self.Mom}."
        return projmanager

    def mark_job(self):
        """What is Mark's job?"""
        personnel = f"Mark works in {self.Mark} on drill weekends."
        return personnel

job_modules = Jobs('CSS', 'Project Manager', 'Personnel')
print(job_modules.gabe_job())
print(job_modules.mom_job())
print(job_modules.mark_job())




    


