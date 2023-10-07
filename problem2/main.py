def draw_xyz(n):
	result = ""
	flag = 1
	i=1
	for i in range (1, (n*n)+1, 1):
		if i%n == 0 and i/n == flag :
			if i%3 == 0 :
				result = result + "X "
			elif i%2 == 0 :
				result = result + "Z "
			elif i%2 != 0 :
				result = result + "Y "
			flag=flag+1
			result = result + "\n"
		else:
			if i%3 == 0 :
				result = result + "X "
			elif i%2 == 0 :
				result = result + "Z "
			elif i%2 != 0 :
				result = result + "Y "
	return result

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """