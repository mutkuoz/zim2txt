zim2txt is a Python module that scrapes through a .zim file and creates .txt files from each article it contains. This tool is designed for Linux systems but it works with WSL (Windows Subsystem for Linux) as well. You must install zim-tools `(sudo apt-get install zimtools)` in advance for this module to work. Here is how to use the module: 
```
import zim2txt
zim2txt.ZimTools.Export("Path for .zim file", "Path for a temporary folder that will be deleted later (I used /usr/games/newfolder with WSL since it didn't work for any folder that is out of root directory. If it does for you, then you can use any other folder as well.)", "Path for .txt files to be saved (do not use same path with temporary files)", "encoding method, default set to utf8")

# Example

import zim2txt
zim2txt.ZimTools.Export("/data/articles.zim", "/usr/games/newfolder") # You don't have to pass encoding method any argument if you're cool with utf8
```