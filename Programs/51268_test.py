i = 0
numbers = input("input list here ")
is_ascending = False
while i <= len(numbers) and len(numbers) != 0:
	if numbers[i] <= numbers[i + 1]:
		is_ascending = True
		i += 1
	else: is_ascending = False
