from instagrapi import Client
import random,time


cl = Client()
comments = [

    "Great one!",
    "So cool!",
    "Amazing!",
    "Wow!",
    "Informative",
    "Love this post!",
    "Great shot!",
    "Awesome Thankyou", 
    "Yessss!",
    "Obsessed!",
    "Perfect!",
]

username,password= "",""
def login_user(USERNAME,PASSWORD):
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """
    try:
        cl.load_settings("session.json")
        cl.login (USERNAME, PASSWORD) 
        cl.get_timeline_feed()
    except:
        
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings("session.json")    
user_followed = []

def follow(pk):
    followers = cl.user_followers(pk,amount=5)
    keys  = followers.keys()
    for user_id in keys:
        cl.user_follow(user_id)
        time.sleep(5)
        user_followed.append(user_id)
    print(user_followed)
def unfollow():
    for user_id in user_followed:
        cl.user_unfollow(user_id)
        time.sleep(10)
def comment(id):
    comment = random.choice(comments)
    cl.media_comment(id, comment)

def like(id):
    cl.media_like(id)
    time.sleep(3)
    
def interactions():
    # getting instagram pages based on the hashtag
    hashtag = ["entrepreneur","success","onlinebusiness","sidehustle"]
    hashtag = random.choice(hashtag)
    medias = cl.hashtag_medias_recent(hashtag,amount=2)
    for media in medias:
        like(media.id)
        time.sleep(10)
        comment(media.id)
        time.sleep(2)
        follow(media.user.pk)
        

def main():
    run = True
    login_user(username,password)
    while run:
        time.sleep(10)
        interactions()
        time.sleep(3600)
        unfollow()

main()
    

    