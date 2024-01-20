import time
import discord
from discord.ext import commands




DISCORD_API_TOKEN = '<TOKEN GOES HERE>'


def run():
    intents=discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot=commands.Bot(command_prefix="!", intents=intents)
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name="MATHS", url="https://www.mathongo.com"))
        print(bot.user)
        print(bot.user.id)
        print("----------------------")

    @bot.command()
    async def ping(ctx):
        """---> Replies pong"""
        await ctx.send("pong")

    @bot.event
    async def on_message(message):
       username = str(message.author).split('#')[0]
       user_message = str(message.content)
       channel = str(message.channel.name)
       print(f'{username} : {user_message} ({channel})')
       if message.channel.name == 'bot-test':
              if user_message.lower() == 'hello':
                  await message.channel.send(f"Hello {username}!! how was your day in discord today?")
                  return
              #-------------------------------------------------------------------------------------------------------------------
              elif user_message == 'Remind':
                  count=0
                  print("hereeeee")
                  #for guild in bot.guilds[0]:  # all servers of the bot

                  #msg="ðŸŽŠHello and welcome to the Mathongo career headstart program! \n \n ðŸŽ‰Congratulations on successfully securing your seat, you are already one step ahead of your peers! \n \nWe're excited to have you join us on this journey of learning and growth. We have a lot of fun and informative activities planned for you, and we can't wait to get started. \n \n Lets Headstart!ðŸ”¥ðŸ”¥"
                  msg ="Hello there dear Trainee! \nHope you are doing well.\n\nActivity 4 : Google Forms Essential is now live! 🤩 🤩  \n\nThis is an individual activity where upon completion you will recieve a Certificate Of Participation too🫶!!\nSo make sure to submit it before the deadline. \n\nHere's a direct link to the Activity Post :\n > https://discord.com/channels/1118904264484466700/1141774375591346196 \n \nBest Of luck! \nTeam Mathongo. \n\nPlease ignore if already submitted :)  "
                  role = discord.utils.find(lambda r: r.name == 'Active Trainee', bot.guilds[0].roles)
                  for member in bot.guilds[0].members:
                      if role in member.roles:
                             if count<6:
                               count+=1
                             else:
                                 try:
                                   await member.send(msg)
                                   await message.channel.send(str(count)+"Sucessfully sent DM to "+str(member))
                                   count+=1
                                 except:
                                    await message.channel.send("Couldn't send to a user, Skipping it!")
                  await message.channel.send("DM has been sent to {} members having role 'Active Trainee' ".format(count))
                  return
              #---------------------------------------------------------------------------------------------------------------------
              elif user_message.lower()=='dmme':
                  #await message.author.send("Hi!")
                  stri="Shourya"
                  #await "".fetch_user.send("Hi! this is a customisable message")
                  user = discord.utils.get(bot.guilds[0].members, nick=stri)
                  msg="Hi! this is a customisable message"
                  if user:
                      await user.send(msg)
                      await message.channel.send("DM is sucessfully sent to "+stri)
                  else:
                      await message.channel.send("Some Error occured")

                  return
              elif user_message=="SendReminder":
                  count=0
                  skip=0
                  s=0
                  for member in bot.guilds[0].members:
                      try:
                         file=open("reminder.txt","r")
                         file2=open('SentReminder.txt','w')
                         for line in file:
                            s+=1
                            if(str(member)==line):
                                 await member.send("Hello there dear Trainee! \nHope you are doing well.\n\nActivity 4 : Google Forms Essential is now live! 🤩 🤩  \n\nThis is an individual activity where upon completion you will recieve a Certificate Of Participation too🫶!!\nSo make sure to submit it before the deadline. \n\nHere's a direct link to the Activity Post :\n > https://discord.com/channels/1118904264484466700/1141774375591346196 \n \nBest Of luck! \nTeam Mathongo. \n\nPlease ignore if already submitted :)  ")
                                 count+=1
                                 print ("message is sent to {}".format(str(member)))
                                 file2.write(str(member))
                         file.close()
                         file2.close()
                      except:
                         print("Couldn't send DM to {} , skipping it!".format(str(member)))
                         skip+=1
                  await message.channel.send("DM successfully sent to {} members , skipped {} members".format(str(count),str(skip)))
                  print(s)
                  return
              elif user_message== 'sendDMcontinuous':
                  #file=open("username.txt","r")
                  names = {'Shourya','Manas','Anmol','TilluOP','BhaloMeye'}
                  for line in names:
                      time.sleep(2)
                      print (line)
                      user = discord.utils.get(bot.guilds[0].members, nick=line)
                      msg="Hi! this is a customisable message"
                      if user:
                          await user.send(msg)
                          await message.channel.send("DM is successfully sent to "+line)

                      else:
                          await message.channel.send("Some Error occurred, message can not be delivered to "+line)
                  #file.close()
                  return
              elif user_message=="StoreUserData":
                  c=1
                  file=open("username.txt","w")
                  print("Storing Data")
                  for member in bot.guilds[0].members:
                      try:
                         file.write(str(c)+"$"+str(member)+"\n")
                         await message.channel.send("{} Username {} saved".format(c,member))
                         c+=1
                      except:
                          await message.channel.send("Couldn't save a username, skipping it!")
                  file.close()
                  print("All Usernames are Saved!")
                  return

              elif user_message=="testt":
                  c=1
                  file=open("test.txt","w")
                  print("Storing Data")
                  for member in bot.guilds[0].members:
                      try:
                         file.write(str(c)+"$"+str(member)+"\n")
                         print("{} Username {} saved".format(c,member))
                         c+=1
                      except:
                          print("Couldn't save a username, skipping it!")
                  file.close()
                  print("All Usernames are Saved!")
                  return

              elif user_message.lower() == "xd":
                 await message.channel.send("Ara")
                 return

       if user_message == "SendEmbed":
              await message.channel.send(message.guild.default_role)
              embed=discord.Embed(title="MATHONGO CAREER HEADSTART", url="https://www.mathongo.com",
                                  description="ðŸŽ‰ Join the Mathongo Career Headstart Program! ðŸŽ‰ \n Hello fellow engineering enthusiasts and problem solvers! \n \n We're thrilled to introduce the Mathongo Career Headstart Program, an exciting opportunity for you to dive into the world of task management, collaborate with like-minded individuals, and enhance your skills. \n \n ðŸ” What is the Mathongo Career Headstart Program? \n \n The Mathongo Career Headstart Program is a unique initiative aimed at nurturing talent within our student community. If you're passionate about learning, solving real-world needs, this program is perfect for you. Through a series of engaging workshops, collaborative projects, and mentorship opportunities, you'll get the chance to learn, create, and grow. \n \n ðŸŒŸ Why Should You Join? \n \n Knowledge Enhancement \n Skill Development \n Networking \n Hands-on Experience \n Mentorship \n \n ðŸ“… Program Details: \n \n Format: Online workshops, collaborative projects, discussions, and more. \n \n Eligibility: All members who are intertested may join \n \n ðŸ“¢ How to Join: \n \n Fill the google form attached and we will add you! \n(members who already got -Trainee- role can skip) \n [https://forms.gle/opoPWUBVtthbzUqSA] \n \n See you inside the world of Mathongo Career Headstart Program! \n \n Best regards, \n Mathongo Discord Team ", color=0x426ff5)
              await message.channel.send(embed=embed)
              return
       elif user_message.lower() == "image":
              await message.channel.send(file=discord.File('mathongo.png'))
       elif user_message == "FollowUp":
              embed=discord.Embed(description = "Due to limited seat, only first 500 members to fill the form will be able to enroll \n as the users from other platforms are also participating. \n Google forms will be open till Tuesday 11:59 PM \n \n Best of luck securing your seat!", color=0x426ff5)
              await message.channel.send(embed=embed)
              return
    bot.run(DISCORD_API_TOKEN)

if __name__=="__main__":
    run()
