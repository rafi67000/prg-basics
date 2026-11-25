class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"{self.username} timeline:")

        for index, post in enumerate(self.posts, start = 1):
            print(f"{index}. {post}")

profile = SocialMediaProfile("johndoe")

posts = ["Hello, world!", "Had a great day at the park!", "What's up, Natalie? How are you?"]

for post in posts:
    profile.add_post(post)

profile.display_timeline()