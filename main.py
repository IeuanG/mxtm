import time
import praw
import wget
import re
sub = raw_input('Please enter the subreddit to download from:  ')
cdir = raw_input('Please enter the directory you wish to download to:  ')
r = praw.Reddit('Image downloader V1.0 /u/IeuanG'
                'Url: IeuanG.io/imgdl'
                'download.php')
already_done = []
checkWords = ['i.imgur.com',  'jpg', 'png', 'gif', 'gfycat.com', 'webm',]
gyfwords = ['gfycat.com']
while True:
    subreddit = r.get_subreddit(sub)
    for submission in subreddit.get_hot(limit=300):
        url_text = submission.url
        has_domain = any(string in url_text for string in checkWords)
        print '[LOG] Getting url:  ' + url_text
        is_gifcat = any(string in url_text for string in gyfwords)
        if submission.id not in already_done and has_domain:
           if is_gifcat:
              url = re.sub('http://.*gfycat.com/', '', url_text)
              url_text = 'http://giant.gfycat.com/' + url + '.gif' 
           wget.download(url_text, '/home/ieuang/Pictures/Extra/' + str(time.time())[-8:-3] + url_text[-4:])
           already_done.append(submission.id)
           print '[LOG] Done Getting ' + url_text
    exit()
