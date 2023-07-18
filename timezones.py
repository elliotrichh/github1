print("elliot's time (gmt)")
Elltime = int(input())
# telling if the input is AM or PM
Stime = (Elltime - 5 + 12) % 24
if Stime > 12:
    print("PM")
else:
    print("AM")

# converts calculated time to military time
Stime %= 12
if Stime == 0:
    Stime = 12
# printing answer
print(Stime , "USA eastern")