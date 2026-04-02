class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.follower=0
        self.following=0
    def follow(self,user):
        user.follower+=1
        self.following+=1   
            
          
user1=User(1,"angela")
user2=User(2,"raj")
print(user1.username)
user1.follow(user2)
print(user1.follower)
print(user1.following)
