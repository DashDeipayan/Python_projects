def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.

    """
    return time_2 - time_1


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.

    """
    return seconds_difference(time_1, time_2) / 3600


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.


    """
    x = hours + (minutes / 60) + (seconds / 3600)
    return x


def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    """

    return hours % 24


### Write your get_hours function definition here:
def get_hours(seconds):
    """ (int) -> int
    seconds is a number of seconds since midnight.
    Return the number of hours that have elapsed since midnight, as seen on a 24-hour clock.

    """
    return to_24_hour_clock(seconds // 3600)


### Write your get_minutes function definition here:
def get_minutes(seconds):
    """(int) -> int
    seconds is a number of seconds since midnight.
    Return the number of minutes that have elapsed since midnight as seen on a clock.

    """
    x = (seconds % 3600)
    return (x // 60) % 60


### Write your get_seconds function definition here:
def get_seconds(seconds):
    """(int) -> int
    seconds is a number of seconds since midnight.
    Return the number of seconds that have elapsed since midnight as seen on a clock.

    """
    x = seconds % 3600
    return (x % 60) % 60


def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    """
    x = time - utc_offset
    return to_24_hour_clock(x)


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.


    """
    return to_24_hour_clock(time + utc_offset - 24)
