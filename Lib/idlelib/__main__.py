def seconds_difference(time1, time2):
    return time2 - time1

def hours_difference(time1, time2):
    return (time2 - time1) / 3600

def to_float_hours(hours, minutes, seconds):
    return hours + minutes / 60 + seconds / 3600

def get_hours(seconds):
    return seconds // 3600

def get_minutes(seconds):
    return (seconds % 3600) // 60

def get_seconds(seconds):
    return seconds % 60

def time_to_utc(offset, time):
    return time - offset

def time_from_utc(offset, time):
    return time + offset

