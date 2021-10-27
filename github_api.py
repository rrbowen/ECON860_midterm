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

df_userids = pandas.read_csv("userid_list_test.csv")
#print(df_userids)

access_point = "https://api.github.com"



user_url = access_point + "/users/" + userid_names
result = json.loads(github_session.get(user_url).text)
print(result)

#followers_url = result['followers_url']
#result = json.loads(github_session.get(followers_url).text)
#followers = [ item['login'] for item in result ]

df_userids = pandas.read_csv("userid_list_test.csv")
print(df_userids)

df = pandas.DataFrame()

for userid_names in df_userids:
	user_url = access_point + "/users/" + userid_names
	print(user_url)
	result = json.loads(github_session.get(user_url).text)
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
