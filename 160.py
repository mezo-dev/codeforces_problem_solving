


def max_profit_from_project():
    projects = [
    ("A", 1, 100),
    ("B", 2, 180),
    ("C", 3, 240),
    ("D", 4, 280),
    ("E", 5, 300),
    ]

    hours = 8

    projects.sort(key=lambda x: x[2] / x[1], reverse=True) # sort by profit per hour

    selected_projects = []
    total_profit = 0
    count_of_projects = 0

    for name, time, profit in projects:
        if time <= hours:
            selected_projects.append(name)
            hours -= time
            total_profit += profit
            count_of_projects += 1
    return selected_projects, total_profit, count_of_projects

print(max_profit_from_project())

