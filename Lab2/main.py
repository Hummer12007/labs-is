from pyDatalog import pyDatalog

# Define rules and create relations
pyDatalog.create_atoms('employee, project, manager, works_on, has_skill, department, supervises, reports_to, salary, performance_score, bonus, high_performer, good_manager, project_department, department_head',\
                        'X, Y, Z, P, Q, R, S, T, U, V, W')

# Employees have skills
has_skill('John', 'Python')
has_skill('Mary', 'Java')
has_skill('Peter', 'C++')
has_skill('Alice', 'SQL')
has_skill('Bob', 'JavaScript')
has_skill('Dave', 'C#')

# Employees work on projects
works_on('John', 'Project A')
works_on('Mary', 'Project B')
works_on('Peter', 'Project A')
works_on('Peter', 'Project B')
works_on('Alice', 'Project C')
works_on('Bob', 'Project D')
works_on('Bob', 'Project E')
works_on('Dave', 'Project F')

# Projects have managers
manager('Project A', 'Alice')
manager('Project B', 'Bob')
manager('Project C', 'Alice')
manager('Project D', 'Bob')
manager('Project E', 'Bob')
manager('Project F', 'Dave')

# Each project belongs to a department
project_department('Project A', 'IT')
project_department('Project B', 'IT')
project_department('Project C', 'Sales')
project_department('Project D', 'Sales')
project_department('Project E', 'Sales')
project_department('Project F', 'IT')

# Employees are assigned to managers based on project
employee(X) <= works_on(X, Y) & manager(Y, Z)

# Employees are part of departments
department('IT')
department('Finance')
department('Sales')

# Employees supervise other employees within the same department
supervises('John', 'Mary') & department('IT')
supervises('John', 'Peter') & department('IT')
supervises('Alice', 'Bob') & department('Sales')
supervises('Bob', 'Dave') & department('IT')

# Employees report to other employees within the same department
reports_to(X, Y) <= supervises(Y, X) & department(Z) & department(Z)
reports_to(X, Y) <= supervises(Z, X) & reports_to(Z, Y)

# Employees have salaries and performance scores
salary('John', 80000)
salary('Mary', 90000)
salary('Peter', 95000)
salary('Alice', 110000)
salary('Bob', 120000)
salary('Dave', 100000)
performance_score('John', 8)
performance_score('Mary', 9)
performance_score('Peter', 7)
performance_score('Alice', 9)
performance_score('Bob', 8)
performance_score('Dave', 7)

# Employees are eligible for bonuses based on performance
bonus(X, Y) <= performance_score(X, P) & salary(X, Q) & (P >= 8) & (Q < 100000)
bonus(X, Y) <= performance_score(X, P) & salary(X, Q) & (P >= 9) & (Q < 120000) & (Y == 5000)

# High performers are employees with a performance score of 9 or higher
high_performer(X) <= performance_score(X, P) & (P >= 9)

# Good managers are employees who have at least one high performer in their team

good_manager(X) <= employee(Y) & employee(Z) & manager(Y, X) & high_performer(Z) & (Y != Z)

# The head of a department is the manager of a project within that department with the highest number of employees

department_head(X, Y) <= project_department(Z, X) & manager(Y, Z) & supervises(P, Q) & employee(P) & works_on(Q, Z) & (Q.counted() == count((P, D), if_(department_employee(D, X)), for_each=D)).distinct().limit(1)

# Print results

print("Employees who work on Project A:")
print(works_on('X', 'Project A'))
print()

print("Managers of Project B:")
print(manager('Project B', 'X'))
print()

print("Employees who report to Alice:")
print(reports_to('X', 'Alice'))
print()

print("Employees eligible for bonuses:")
print(bonus('X', 'Y'))
print()

print("High performers:")
print(high_performer('X'))
print()

print("Good managers:")
print(good_manager('X'))
print()

print("Heads of departments:")
print(department_head('IT', 'X'))
print(department_head('Sales', 'X'))