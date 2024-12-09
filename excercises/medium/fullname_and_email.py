class employee:
    def __init__(self,first_name,last_name):
        self.full_name = f"{first_name} {last_name}"
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
employee = employee("Gayathri","Anand")
print("fullname",employee.full_name)
print("email",employee.email)      

