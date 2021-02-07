import praw
import time


reddit = praw.Reddit(client_id="your-client-id-here",
                     client_secret="your-client-secret-here",
                     password="your-reddit-password-here",
                     user_agent="vidbt by /u/your-reddit-username-here",
                     username="your-reddit-username-here")


#Validate correct authorization 
#should print reddit username 
#print(reddit.user.me())
#should print False 
#print(reddit.read_only)

#list of subreddits I want to post to

subreddits = ['programming','SelfPromotionYouTube', 'Youtubeviews', 'videos', 'SubscribeToMe',
'YouTubePromoter', 'SmallYoutuberArmy',' YoutubeSelfPromotion', 'shamelessplug', 
'YouTubeSubscribeBoost', 'YouTube_startups', 'Youtubestartups', 
'AdvertiseYourVideos', 'SmallYoutubers','madeinpython', 'girlsgonewired', 'codeprojects',
'coding']



#title of my reddit post
title = "title-of-reddit-post-here"
#link to my video
link = "link-to-your-video-here"

count = 0

for subreddit in subreddits:
	count+=1
	try:
		reddit.subreddit(subreddit).submit(title,url=link,send_replies=False)
		print("Sucessfully posted to",subreddit,"Posted to",count,"of",len(subreddits),"subreddits")

	except praw.exceptions.RedditAPIException as exception:

		for subexception in exception.items:
			
			#if we are RATELIMITED
			if subexception.error_type == "RATELIMIT":
				

				#figure out how long to wait before posting again
				wait = str(subexception).replace("RATELIMIT: 'you are doing that too much. try again in ","")
				
				if 'minute' in wait:
					wait = wait[:2]
					wait = int(wait) + 1
					
				#if wait time is a second value, wait = 1	
				else:
					wait = 1

				#wait for a certain amount of seconds before posting again 
				print("waiting for:",wait,"minutes")
				time.sleep(wait*60)
				reddit.subreddit(subreddit).submit(title,url=link)
				print("Sucessfully posted to",subreddit,"Posted to",count,"of",len(subreddits),"subreddits")
		
