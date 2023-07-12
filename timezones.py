import datetime
import pytz

# Define the eastern time zone
eastern_tz = pytz.timezone('US/Eastern')

# Get the current time
current_time = datetime.datetime.now()

# Loop through each Eastern state
eastern_states = ['Massachusetts']

for state in eastern_states:
    # Set the time zone for the state
    state_tz = pytz.timezone('US/Eastern')

    # Convert the current time to the state's time zone
    state_time = current_time.astimezone(state_tz)

    #Convert the state's time to gmt
    gmt_time = state_time.astimezone(pytz.timezone('GMT'))

    # Format the time as a string
    time_str = gmt_time.strftime('%Y-%m-%d %H:%M:%S')

    # Print the state ad its corresponding gmt time
    print(f"{state}: {time_str} GMT")
