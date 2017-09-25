import random 

with open('data.txt', 'w') as f:
	for x in range(100):
		x = random.uniform(0,100)
		y = random.uniform(0,100)
		x_noise = random.uniform(-2.5,2.5); 
		y_noise = random.uniform(-2.5,2.5);

		z = (0.5*x+x_noise + 0.75*y+y_noise)
		line = str(x)+','+str(y)+','+str(z)+'\n'
		f.write(line)