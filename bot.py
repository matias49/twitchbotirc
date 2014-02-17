# Twitch IRC BOT for emulators
# This Python script connects to the twitch channel provided with the credencials provided to gets the chat input in order to convert them into keypresses
# Big thanks to TwitchPlaysPokemon (http://www.twitch.tv/twitchplayspokemon) for create this idea.
# Author : Matias49 | https://github.com/matias49
# Licence : GPL v3
# For the key's hex code, check this link : http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx
# irclib & ircbot download : http://sourceforge.net/projects/python-irclib/files/python-irclib/
import irclib
import ircbot
import time
# win32api download : http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
import win32api
import win32con

class Bot(ircbot.SingleServerIRCBot):
	# Initialize the bot
    def __init__(self):
	# format of this function : (self, [(IRC server, port, password)], name, comment)
        ircbot.SingleServerIRCBot.__init__(self, [("irc.twitch.tv", 6667, "oauth:yourkey")], # key : www.twitchapps.com/tmi 
                                           "TwitchAccountName", "IRC Bot")
    def on_welcome(self, serv, ev):
        # join the Twitch channel you want
        serv.join("#ChannelName")
    def on_pubmsg(self, serv, ev):
        # Gets the message
        message = ev.arguments()[0].lower()
	# Gets the author (ex : dentuk!~dentuk@EpiK-BE9687C2.fbx.proxad.net)
        author = ev.source()
	# gets the ! position to remove the rest
        namePosition = author.index('!')
	# save only the author
        author = author[0:namePosition]
        #print author," : ",message # print test
        if message == "a":
            print author," : ",message
            win32api.keybd_event(0x41, 0) #types a
            time.sleep(.05)
            win32api.keybd_event(0x41,0 , win32con.KEYEVENTF_KEYUP) #releases a
        if message == "b":
            print author," : ",message
            win32api.keybd_event(0x42, 0) #types b
            time.sleep(.05)
            win32api.keybd_event(0x42,0 ,win32con.KEYEVENTF_KEYUP) #releases b
        if message == "left" or message == "gauche": #you can add more languages
            print author," : left"
            win32api.keybd_event(0x43, 0) #types c (Yes, because left key hex code didn't work well)
            time.sleep(.05)
            win32api.keybd_event(0x43,0 ,win32con.KEYEVENTF_KEYUP) #releases c
        if message == "right" or message == "droite": #you can add more languages
            print author," : right"
            win32api.keybd_event(0x44, 0) #types d (same)
            time.sleep(.05)
            win32api.keybd_event(0x44,0 ,win32con.KEYEVENTF_KEYUP) #releases d
        if message == "up" or message == "haut": #you can add more languages
            print author," : up"
            win32api.keybd_event(0x45, 0) #types e  (same)
            time.sleep(.05)
            win32api.keybd_event(0x45,0 ,win32con.KEYEVENTF_KEYUP) #releases e
        if message == "down" or message == "bas": #you can add more languages
            print author," : down"
            win32api.keybd_event(0x46, 0) #types f (same)
            time.sleep(.05)
            win32api.keybd_event(0x46,0 ,win32con.KEYEVENTF_KEYUP) #releases f
        if message == "start":
            print author," : ",message
            win32api.keybd_event(0x47, 0) #types g
            time.sleep(.05)
            win32api.keybd_event(0x47,0 ,win32con.KEYEVENTF_KEYUP) #releases g
        #if message == "select": | Disabled
         #   win32api.keybd_event(0x47, 0) #types h
          #  time.sleep(.05)
           # win32api.keybd_event(0x47,0 ,win32con.KEYEVENTF_KEYUP) #releases h
if __name__ == "__main__":
    Bot().start()
    
