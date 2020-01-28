# SpongeBot Squarepants

Inspiration
-
For those who always want to be on top of good deals online, SpongeBot Squarepants was created to alert users whenever a hot new deal is posted on their favorite subreddit, or just for any posts in general!

How it works
-
SpongeBot fetches the given websites.rss url to access its full feed where it parses through specfic tags to return submitted posts. SpongeBot scrapes the data from its RSS feed every 3 minutes and updates users with new posts if any exist.

How to run SpongeBot
-

***IMPORTANT***
After cloning the repository, be sure to replace the string in **botToken.py** with the **token of YOUR bot**
```
git clone github.com/toado/discordbot
cd discordBot
python3 discordBot
```



A simple discord bot that doubles as an RSS reader.
SpongeBot alerts users whenever a new submission is posted onto their desired subreddit of choice, 
and also includes some other functions that may come in handy :-)
