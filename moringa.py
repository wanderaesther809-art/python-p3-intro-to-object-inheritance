from pprint import pp


class Employee:
    def __init__(self, first_name, last_name, salary, gender, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.gender = gender
        self.phone_number = phone_number

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def id(self):
        initials = f"{self.first_name[0]}{self.last_name[0]}"
        last_three_digits = self.phone_number[-3:]

        return f"MS-{initials}-{last_three_digits}"

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@moringaschool.com"


class Manager(Employee):
    def __init__(
        self,
        first_name,
        last_name,
        salary,
        gender,
        phone_number,
        department,
        employees=None,
    ):
        super().__init__(first_name, last_name, salary, gender, phone_number)
        self.department = department

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_employees(self):
        return [employee.fullname() for employee in self.employees]


class Instructor(Employee):
    def __init__(self, first_name, last_name, salary, gender, phone_number, course):
        super().__init__(first_name, last_name, salary, gender, phone_number)
        self.course = course


classroom_manager = Manager(
    "Bernard", "Musau", "500000", "Male", "0712345678", "Classroom"
)


instructor1 = Instructor(
    "Jerald", "Nyaga", "200000", "Male", "0712328639", "Software Engineering"
)
instructor2 = Instructor(
    "Nelson", "Muriithi", "200000", "Male", "0712328129", "Software Engineering"
)
instructor3 = Instructor(
    "Erick", "Mongare", "200000", "Male", "0712328900", "Software Engineering"
)

classroom_manager.add_employee(instructor1)
classroom_manager.add_employee(instructor2)
classroom_manager.add_employee(instructor3)

print(classroom_manager.list_employees())

# remove employee
classroom_manager.remove_employee(instructor2)


print(classroom_manager.list_employees())