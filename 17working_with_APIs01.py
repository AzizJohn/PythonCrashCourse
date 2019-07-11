"""
The package <requests> is alreadly installed on Ubuntu 18.
"""
import requests
#Let's make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)#Store API response in a variable.
print(f"Status code: {r.status_code}")
#If r.status_code == 200, then the request goes well.
response_dict = r.json()#json() method returns a Python dictionary.
#Let's process results.
print(response_dict.keys())
#dict_keys(['total_count', 'incomplete_results', 'items'])
print(f"Total repositories: {response_dict['total_count']}")
repo_dicts = response_dict['items']
#repo_dicts is a list, each item is a dictionary containing
#information of a repository.
print(f"Repositories returned: {len(repo_dicts)}")
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

#Let's print all the keys.
first_item = True
for key in sorted(repo_dict.keys()):
	if first_item == True:
		first_item = False
	else:
		if previous == key[0]:
			print(', ', end='')
		else:
			print('\n\n', end='')
	print(key, end='')
	previous = key[0]
print('')
#Let's make an interactive bar chart: height of each bar is number of stars,
#and you can click the bar's label to go to that project's home on Github.
from plotly.graph_objs import Bar
from plotly import offline
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	stars.append(repo_dict['stargazers_count'])
	
	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner}<br />{description}"
#Plotly allows you to use HTML code within text elements,
#<br /> means line break.	
	labels.append(label)
	
data = [{
	'type': 'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': labels,
	'marker':{
		'color': 'rgb(60, 100, 150)',#set the bar color to blue
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}#set boundary to gray
	},
	'opacity': 0.6,#opacity=0 means transparent
}]
my_layout = {
	'title': 'Most-Starred Python Projects on GitHub',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Stars',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
