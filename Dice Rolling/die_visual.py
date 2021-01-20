import pygal
from die import Die

die_1 = Die()
die_2 = Die()
# results store the rolls
results = []

for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# analysis on results
frequencies = []

for value in range(2, die_1.num_sides+die_2.num_sides+1):
	frequency = results.count(value) # count how many of this value in our rolls
	frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()
hist.title = "Rolling 2 dice for 1000 times"
hist.x_labels = [str(x) for x in range(2, die_1.num_sides+die_2.num_sides+1)]
hist.x_title = "Rolled Value"
hist.y_title = "Frequency of Each Value"

hist.add('2 dice', frequencies)
hist.render_to_file('die_visual.svg')