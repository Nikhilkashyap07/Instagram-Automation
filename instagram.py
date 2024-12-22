from instabot import Bot

bot= Bot()

bot.login(username="",password="")
bot.follow("id/username")
bot.upload_photo("photo path",caption="i love python")
bot.unfollow("username")
bot.send_messages("msg",["username"]) 

followers = bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("username")
for Following in following:
    print(bot.get_user_info(Following))



