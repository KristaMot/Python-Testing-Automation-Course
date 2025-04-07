initial_data = '1h 45m,360s,25m,30m 120s,2h 60s'
time_string = initial_data.replace(' ', ',')
time_list = time_string.split(',')
sum_minutes = 0

for time in time_list:
    if 'h' in time:
        sum_minutes += int(time[:-1]) * 60
    elif 'm' in time:
        sum_minutes += int(time[:-1])
    elif 's' in time:
        sum_minutes += int(time[:-1]) // 60

print (sum_minutes)

