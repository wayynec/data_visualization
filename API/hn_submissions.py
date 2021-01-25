import requests
from operator import itemgetter

# call API and save the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code: ", r.status_code)

# Then we get a bunch of ids, then we need to get each of them
ids = r.json()
dicts = []

for index, t_id in enumerate(ids):
	# call API for every id
	url = 'https://hacker-news.firebaseio.com/v0/item/' + str(t_id) + '.json'
	t_r = requests.get(url)
	# print(t_r.status_code)
	temp_dict = t_r.json()
	# print(str(index)+"ok")

	t_dict = {
		'title': temp_dict['title'],
		'link': 'https://news.ycombinator.com/item?id=' + str(temp_dict['id']),
		'comments': temp_dict.get('descendants', 0) # try to get the value for descendants, if not existant, put 0
	}
	dicts.append(t_dict)

dicts = sorted(dicts, key=itemgetter('comments'), reverse=True)

for entry in dicts:
	print('\nTitle: ' + entry['title'])
	print('Link: ' + entry['link'])
	print('Comments: ' + str(entry['comments']))
