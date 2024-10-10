**Microsoft** has been pushing for its users to use its Phone Link application. It's an app that allows users to control their phone through their computer. They can access their contacts, pictures, and open apps. 
One may think they store this information securely but this is not the case. It's stored in **AppData** in a database open for everyone to read.
By just scrolling through the file I was able to extract: 
- Phone numbers
* Contact names
+ Apps installed

This is a massive privacy concern and I would not advise people to install it.
I included a quick Python script that extracts this information. 
Here is a path that might work for most people:
**C:\Users\UserName\AppData\Local\Packages\Microsoft.YourPhone_8wekyb3d8bbwe\LocalCache\Indexed\4a932ba5-d3aa-43cc-bdd8-89db578e00ff\System\Database**
