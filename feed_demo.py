from lab_classes import User, Tweet

def build_feed():
    me = User('gonch')
    other = User('kress')      # your second account name
    users = [me, other]
    posts = [
        Tweet('gonch', 'hello world #hi'),
        Tweet('kress', 'today is a bad day #sad'),
        Tweet('gonch', 'choose happiness, kress #optimism')
    ]
    
    me.follow()
    other.follow()
    me.unfollow()
    other.unfollow()

    posts[0].like()
    posts[1].like()
    posts[2].like()
    posts[0].unlike()
    posts[1].unlike()
    posts[2].unlike()

    return users, posts



def main():
    # Call build_feed and display the returned objects and hashtags.
    users, posts = build_feed()
    for user in users:
        print(user)
        print(user.followers)
    for post in posts:
        print(post)
        print(post.likes)
        print(post.hashtags())


if __name__ == '__main__':
    main()
