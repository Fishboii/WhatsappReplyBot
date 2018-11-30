# WhatsappReplyBot
A program that can reply Whatsapp messages through Whatsapp web. It is created using python 3.7 and selenium.You will need a valid phone number registered to Whatsapp, the Whatsapp app and an active internet connection for this to work. This version of the bot will use your Whatsapp account to reply and will check for keywords every 1 second \
Since the program uses Whatsapp web, you will be unable to use Whatsapp web to access other chats but the one the bot is checking. The bot will reply to your own messages. \
I do not take responsibility for any damages caused by this program. Use at your own risk. \
Do note that the reciepient's name must be the one stored in your contacts. You can check them in the Whatsapp mobile app. \
Before running the code, make sure you have selenium installed. \
If you have any questions, you can email me at juntaozhang0617@gmail.com. \
Important: You need to create a file with Chromedriver.exe on your computer. You can go to https://sites.google.com/a/chromium.org/chromedriver/downloads to get the latest version. You will then need to get the path of the file (Properties or More Info) and paste it into line 9 of the code.

# What the path should look like
The code should look like:
driver = webdriver.Chrome(executable_path=r' Your Chromedriver path ')

And you would need to change it to:
driver = webdriver.Chrome(executable_path=r'C:\Users\fishboii\Desktop\Selenium drivers\Chromedriver.exe')
(The above is an example)
# Instructions for entering your path
<ol>
  <li>Go to https://sites.google.com/a/chromium.org/chromedriver/downloads and download the latest version of Chromedriver
  <li>Unzip the file
  <li>Create a folder to store the .exe, I recommend the Desktop
  <li>Right click the folder and click Properties or More Info
  <li>You will then need to check the location of the file
  <li>Copy the location to your clipboard
  <li>Paste it over the location in the code, make sure the location ends with the Chromedriver.exe
  <li>If all is done correctly, the program should run.</li>
</ol>

# Instructions for the using the bot
<ol>
  <li>Enter a keyword that triggers the bot.
  <li>Enter the settings for the word, 'y' if you want the bot to only reply to messages that contain the keyword only, 'n' if the keyword can be in a sentence. (This includes words that contain the keyword)
  <li>Enter the message that the bot will reply to.
  <li>Enter the name of the person or group that you want the bot to check. (Unfortunately, this bot can only check one chat at a time. I might update it in the future.)
  <li>At this point, a Chrome window should open and prompt you to scan the QR code, scan it and return to the interpreter or terminal.
  <li>Hit enter to start the bot.</li>
</ol>


