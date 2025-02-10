def read_hour():
    h = int(input('Enter hour: '))
    return h
def read_minute():
    m = int(input('Enter minute: '))
    return m
def read_second():
    s = int(input('Enter second: '))
    return s
def to_seconds(h, m, s):
    sum = (h * 3600)+(m *60)+s
    return sum
def time_elapsed(start_time, finish_time):
    e_sec = finish_time - start_time
    hour = e_sec//3600
    min = (e_sec%3600)//60
    sec = e_sec - (hour * 3600+ min *60)
    e = f'{hour} hours {min} minutes {sec} seconds.'
    return e
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))