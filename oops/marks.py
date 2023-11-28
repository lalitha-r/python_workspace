# problem #5
# In your college Python is taught in 3 different departments by the same professor.
# For each dept, get the no of students studying Python and their marks in the final exam
# Get the input as comma seperated string

# Find the top 3 marks in each class
# Find the top 3 marks in all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.


class Department:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def top_marks(self):
        """Find the top 3 marks in the department."""
        return sorted(self.marks, reverse=True)[:3]

    def average_passing_marks(self, passing_mark=50):
        """Calculate the average mark of students who passed."""
        passing_marks = [mark for mark in self.marks if mark >= passing_mark]
        if passing_marks:
            return sum(passing_marks) / len(passing_marks)
        else:
            return 0

    def num_failed_students(self, passing_mark=50):
        """Calculate the number of students who failed."""
        return len([mark for mark in self.marks if mark < passing_mark])


class College:
    def __init__(self, departments):
        self.departments = departments

    def top_marks_across_all_departments(self):
        """Find the top 3 marks across all departments."""
        all_marks = sum([dept.marks for dept in self.departments], [])
        return sorted(all_marks, reverse=True)[:3]

    def overall_average_passing_marks(self):
        """Calculate the overall average mark of passing students across all departments."""
        total, count = 0, 0
        for dept in self.departments:
            avg = dept.average_passing_marks()
            if avg != 0:
                total += avg
                count += 1
        return total / count if count else 0

    def best_performance_department(self):
        """Find the department with the best average and least failures."""
        best_avg = max(self.departments,
                       key=lambda dept: dept.average_passing_marks())
        least_failures = min(
            self.departments, key=lambda dept: dept.num_failed_students())
        return best_avg.name, least_failures.name

# Get input for each department


def get_department_input(name):
    num_students = int(input(f"Enter the number of students in {name} dept: "))
    marks = [int(mark) for mark in input(
        f"Enter the marks for {num_students} {name} students as comma-separated values: ").split(',')]
    return Department(name, marks)


# Creating Department instances
it_dept = get_department_input("IT")
cs_dept = get_department_input("CS")
ece_dept = get_department_input("ECE")

# Creating College instance
college = College([it_dept, cs_dept, ece_dept])

# Displaying results
for dept in college.departments:
    print(f"Top 3 marks in {dept.name}: {dept.top_marks()}")
    print(
        f"Average mark of passing students in {dept.name}: {dept.average_passing_marks()}")
    print(
        f"Top 3 marks in all departments: {college.top_marks_across_all_departments()}")
    print(
        f"Overall average mark of passing students: {college.overall_average_passing_marks()}")
    print(
        f"Best average mark across departments: {dept.average_passing_marks()}")
