import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)
# now we know that the response is good

# store the response in a dictionary
response_dict = r.json()
print(response_dict.keys())
# now we know what keys are in json file

print("Total repositories: ", response_dict['total_count'])
print("Results returned: ", len(response_dict['items']))

repositories = response_dict['items']
# now we look into the dic repository key-value pair
# dic = repositories[0]
# print("\nKeys: ", len(dic))
# for key in sorted(dic.keys(), key=lambda x:x[0]): # seems it only sorts the dic letter
# 	print(key)
# for index, dic in enumerate(repositories):
# 	print("\nWe want to know the following info on repository " + str(index+1) + ":")
# 	print("Name: ", dic['name'])
# 	print('Owner: ', dic['owner']['login']) # dict in dict
# 	print('Stars: ', dic['stargazers_count'])
# 	print('Repostory: ', dic['html_url'])
# 	print('Created: : ', dic['created_at'])
# 	print('Updated: ', dic['updated_at'])
# 	print('Description: ', dic['description'])

# following parts create a chart listing high # stars repos
# names, stars = [], []
# for repo in repositories:
# 	names.append(repo['name'])
# 	stars.append(repo['stargazers_count'])

# with bar descrpitions
names, plot_dicts = [], []
for repo in repositories:
	names.append(repo['name'])
	plot_dict = {
		'value': repo['stargazers_count'],
		'label': repo['description'] or "",   # could be no description
		'xlink': repo['html_url']
	}
	plot_dicts.append(plot_dict)

# x-repo name y-stars
my_style=LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
# chart.title = "Python repos with most stars on GitHub"
# chart.x_labels = names

# chart.add('', stars)
# chart.render_to_file("python_repos.svg")

# use config to config the chart
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Python repos with most stars on GitHub"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')