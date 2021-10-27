import json
import requests
import pandas

f = open("token", "r")
token = f.read()
f.close()

f = open("username", "r")
username = f.read()
f.close()

github_session = requests.Session()
github_session.auth = (username, token)

df_userids = pandas.read_csv("userid_list.csv")

#result = json.loads(github_session.get(df_userids[:1]))



df = pandas.DataFrame()

for i in range(0,700):
	result = df_userids[:i]
	#result = user_url
	df = df.append({
	'id' : result['id'],
	'avatar_url' : result['avatar_url'],
	'url' : result['url'],
	'followers_count' : result['followers'],
	'following_count' : result['following'],
	#'starred' : result['starred'],
	'repos_count' : result['public_repos'],
	'name' : result['name'],
	'company' : result['company'],
	'blog' : result['blog'],
	'location' : result['location'],
	'email' : result['email'],
	'hireable' : result['hireable'],
	'created_at' : result['created_at'],
	'updated at' : result['updated_at'],
	'login' : result['login'],
	'twitter_username' : result['twitter_username']
}, ignore_index = True)

df.to_csv("userid_dataset.csv")
