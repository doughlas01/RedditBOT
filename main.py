import praw
import random
import time
reddit = praw.Reddit(
    client_id="client id",
    client_secret="client secret",
    password="enter your password",

    user_agent="user agent ",
    username="username of bot",
)
quotes_list = [ "When you have a dream, you’ve got to grab it and never let go.”",
"“People tell you the world looks a certain way. Parents tell you how to think. Schools tell you how to think. TV. Religion. And then at a certain point, if you’re lucky, you realize you can make up your own mind. Nobody sets the rules but you. You can design your own life.”",

" “For me, becoming isn’t about arriving somewhere or achieving a certain aim. I see it instead as forward motion, a means of evolving, a way to reach continuously toward a better self. The journey doesn’t end.”",


"Spread love everywhere you go.”",

" “Do not allow people to dim your shine because they are blinded. Tell them to put some sunglasses on.”"


" “If you make your internal life a priority, then everything else you need on the outside will be given to you and it will be extremely clear what the next step is.”",

 "You don’t always need a plan. Sometimes you just need to breathe, trust, let go and see what happens.”",

" “You can be everything. You can be the infinite amount of things that people are.” Kesha",


 "Nothing is impossible. The word itself says ‘I’m possible!"]


subreddit = reddit.subreddit("sad")
for submission in subreddit.hot(limit =10):
    #print(submission.title)
    # print("********")
    for comment in submission.comments:
        if hasattr(comment, "body"):
           
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("<<<<<<")
                print(comment.body)
                random_index = random.randint(0,len(quotes_list)-1)
                comment.reply(quotes_list[random_index])
                time.sleep(660)
