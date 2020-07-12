standard = ""
race_time = float(99999999999999999)
while standard != "no more races,":
	standard = input("Time? ")
	if standard != "no more races," and race_time > float(standard):
		race_time = standard
		print(race_time)
print(race_time)
