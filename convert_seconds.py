# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(seconds):
    minutes = int(seconds/60)
    seconds = seconds % 60
    hours = int(minutes/60)
    minutes = minutes % 60
    if hours == 1:
        hour_or_hours = "hour"
    else:
        hour_or_hours = "hours"
    if minutes == 1:
        minute_or_minutes = "minute"
    else:
        minute_or_minutes = "minutes"
    if seconds == 1:
        second_or_seconds = "second"
    else:
        second_or_seconds = "seconds"
    time = str(hours) + " " + hour_or_hours + ", " + str(minutes) + " " + minute_or_minutes + ", " + str(seconds) + " " + second_or_seconds
    return time

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds