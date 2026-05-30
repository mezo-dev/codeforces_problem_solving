



def max_num_of_tasks():
    tasks = [2, 1, 3, 2, 4]
    time_available = 7

    tasks.sort()

    count = 0
    for task in tasks:
        if time_available >= task:
            time_available -= task
            count += 1
        else:
            break
    return count

print(max_num_of_tasks())