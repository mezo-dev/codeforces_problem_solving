



def max_num_of_meetings():
    meetings = [
    (1, 3),
    (2, 4),
    (3, 5),
    (0, 7),
    (5, 8),
    (8, 9)
]
    
    meetings.sort(key=lambda x: x[1]) # sort by end time

    count = 0
    last_end_time = 0
    for start, end in meetings:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    return count

print(max_num_of_meetings())