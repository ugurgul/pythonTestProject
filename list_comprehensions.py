salaries = [1000, 2000, 3000, 4000, 5000]

new_salaries = []

[salary * 2 if salary < 3000 else salary * 3 if salary == 4000 else salary * 1.5 for salary in salaries]

