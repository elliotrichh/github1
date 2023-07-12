import datetime
import pytz

# Define the eastern time zone
eastern_tz = pytz.timezone('US/Eastern')

# Define the western time zone
western_tz = pytz.timezone('US/Pacific')

# Get the current time
current_time = datetime.datetime.now()

# Loop through each Eastern state
eastern_states = ['Massachusetts']

western_states = ['California']

print("Dad's time")

for state in western_states:
    state_tz = pytz.timezone('US/Pacific')

    state_time = current_time.astimezone(state_tz)

    gmt_time = state_time.astimezone(pytz.timezone('GMT'))

    time_str = state_time.strftime('%Y-%m-%d %H:%M:%S')

    print(f"{state}: {time_str} GMT")

print("Sage's time")

# Resetting the time
current_time = datetime.datetime.now()

for state in eastern_states:
    # Set the time zone for the state
    state_tz = pytz.timezone('US/Eastern')

    # Convert the current time to the state's time zone
    state_time = current_time.astimezone(state_tz)

    # Convert the state's time to gmt
    gmt_time = state_time.astimezone(pytz.timezone('GMT'))

    # Format the time as a string
    time_str = state_time.strftime('%Y-%m-%d %H:%M:%S')

    # Print the state and its corresponding gmt time
    print(f"{state}: {time_str} GMT")
