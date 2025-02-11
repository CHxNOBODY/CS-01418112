def read_hour():
    
    while True:
        hour = input("Enter hour: ")
        if hour.isdigit() and 0 <= int(hour) <= 23:
            return int(hour)

def read_minute():
    
    while True:
        minute = input("Enter minute: ")
        if minute.isdigit() and 0 <= int(minute) <= 59:
            return int(minute)

def read_second():
    
    while True:
        second = input("Enter second: ")
        if second.isdigit() and 0 <= int(second) <= 59:
            return int(second)

def to_seconds(h, m, s):
    """แปลงเวลา h ชั่วโมง m นาที s วินาที เป็นจำนวนวินาที"""
    return h * 3600 + m * 60 + s

def time_elapsed(start, finish):
    
    elapsed = finish - start
    hour = elapsed // 3600
    minute = (elapsed % 3600) // 60
    second = elapsed % 60
    return f"{hour} hours {minute} minutes {second} seconds"

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