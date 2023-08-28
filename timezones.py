print("elliot's time (gmt)")

#read the input and turn it into an integer

Elltime = int(input())

# telling if the input is AM or PM

Stime = (Elltime - 5 + 12) % 24
# turn the time into USA eastern by subtracting 5 hours from the inputted times

if Stime > 12:
    print("AM")
else:
    print("PM")

#checks if the calculated time is either AM or PM

Stime %= 12
if Stime == 0:
    Stime = 12

#finally, print the converted time, along with either the designated AM or PM

print(Stime , "USA eastern")

