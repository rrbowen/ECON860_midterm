import json
import requests
import pandas
import time

f = open("token", "r")
token = f.read()
f.close()

f = open("username", "r")
username = f.read()
f.close()

github_session = requests.Session()
github_session.auth = (username, token)

#this works - therefore I can communicate with github api
#access_point = "https://api.github.com"
#rate_limit_url = access_point + "/rate_limit"
#result = json.loads(github_session.get(rate_limit_url).text)
#print(result)

df_userids = pandas.read_csv("userid_list_simple.csv")
print(df_userids)

df_results = pandas.DataFrame()
access_point = "https://api.github.com"
for userid_test in df_userids['userid_test']:
	user_url = access_point +"/users/" + userid_test
	result = json.loads(github_session.get(user_url).text)
	print(result)
	time.sleep(5)

	
for login in df_userids['userid_test']:
		user_url = access_point +"/users/" + login
		result = json.loads(github_session.get(user_url).text)
		df_results = df_results.append({
			'id' : result['id'],
			'avatar_url' : result['avatar_url'],
			'url' : result['url'],
			'followers_count' : result['followers'],
			'following_count' : result['following'],
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
			},ignore_index = True)
		time.sleep(2)


print(df_results)

df_results.to_csv("github_download2.csv")






	

