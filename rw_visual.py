import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
	rw = RandomWalk(60000)
	rw.fill_walk()

	plt.figure(dpi=128, figsize=(10, 6))

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

	# emphasize start and finish points
	plt.scatter(0, 0, c='red', edgecolors='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=100)

	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	response = input("Would you like to have another random walk? (y/n) ")
	if response.lower() == 'n':
		break 