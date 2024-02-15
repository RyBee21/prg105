# List of the times and hear rate 

time_slots = ["morning", "midday", "afternoon", "evening"]
heart_rate = []

# Asks user for heart rate appends it the empty list
for time in time_slots:
    heart_rate_inq = int(input(f"What is your hear rate (in BPM) for {time} "))
    heart_rate.append([time, heart_rate_inq])

# Total 
total = 0
for rate in heart_rate:
    total += rate[1]
# Average
average = round(total / len(heart_rate))

# Prints the array and average
print(heart_rate)
print("your average heart rate is ", average)
