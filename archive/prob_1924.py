def weekday(month, day):
    n_days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    weekdays = {
        0: 'SUN',
        1: 'MON',
        2: 'TUE',
        3: 'WED',
        4: 'THU',
        5: 'FRI',
        6: 'SAT'
    }
    day_of_year = 0
    for month in range(1, x):
        day_of_year += n_days_in_month[month]
    day_of_year += y
    return weekdays[day_of_year % 7]

x, y = map(int, input().split())
print(weekday(x, y))
