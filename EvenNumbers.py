#function to find all the even numbers till the given range (including the number of the range)

def get_even_numbers(number):
	if number < 0 : return
	even = [x for x in range(number+1) if x % 2 == 0]
	return even

ans = get_even_numbers(11)
print (ans)
