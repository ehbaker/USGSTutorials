Help! What is GitHub?
==
### Q: Why are we using GitHub to share code?
### A: It allows for easy collaboration - it's like a combination of social media and wikipedia, for coding! Nerd :)

To use GitHub, you must first have a program called **Git** installed on your computer. It tracks changes in your code (version control).

To Install Git, follow these directions from [Software Carpentry](https://uwescience.github.io/2017-01-09-uw/#setup):

1. Download the Git for Windows [installer.](https://git-for-windows.github.io/) 
2. Run the installer and follow the steps bellow:
  *Click on "Next".
  * Click on "Next".
  * Keep "Use Git from the Windows Command Prompt" selected and click on "Next". 
  * Click on "Next".
  * Keep "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".
  * Keep "Use Windows' default console window" selected and click on "Next".
  * Click on "Install".
  * Click on "Finish".
  
To Sign up for GitHub with an official USGS account, follow [these directions](http://butst.usgs.gov/open-source/):
* You must use your USGS email and name

From here, I reccommend using SoftwareCarpentry's [Version Control with GitHub](http://swcarpentry.github.io/git-novice/):
* You can fly through it pretty darn quickly! They say  it takes 2.5 hrs. If you don't have that kind of time today, see below.

The quick-and-dirty version:
------
note: [this linked tutorial](https://try.github.io/levels/1/challenges/1) lets you practice these commands online, and prompt you if you mess up - pretty neat
1. From the **Start** menu, open 'GitBash'
  * This will open a scary-looking GitBash terminal window (no GUI? The horror!). Don't freak out! Remember you look super cool with a command prompt on your screen.
2. Navigate to the directory (folder) that you want to track. To do that in the command line, you type `cd` to change directory.
  * Typing `pwd` and hitting enter will show where in the folder tree you are currently.
  * Typing `ls` and hitting enter will list all the files in that directory. To see hidden files, use `ls -a`
  * If you're in "Users/yourname", and want to access a folder called "Dragon Taming" in your Documents folder, you can type `cd Documents/Dragon Taming`
  * Alternatively, you can use tab completion; type `cd Docu` and then hit tab; the rest of `Documents` should fill in. Ditto for the rest of the path. This is a handy little shortcut, and prevents silly typos!!
3. Once you're in the directory you want to track, type `git init`. This initiates a tracking system for files in the directory (and sub-directories). However, you must tell it which files in there you want to track.
4. To do that, you type `git add filename`. Use tab completion to add filename, to prevent typos. This adds to staging area.
5. To store file in your local (your computer) version control, type `git commit filename -m "message about what you did to the file"`
  * This part is a little tricky - it will not accept the commit without a note about what you've done to the file. Useful for going back through different versions. Can be confusing if an error message pops up while commiting. Repeat for all files you wish to track, and eventually push to github.
  
**Now your file(s) are being tracked by Git! Hooray**

6. Push files to GitHub. Go to your GitHub page, and start a new repository  (your github -> Repositories -> New). 
  * Do not initialize with a read-me or liscence; just make an empty repo.
7. Now you will see a bunch of text under "Quick Setup".
  * Copy the code under **" ...or push an exising repository from the command line"** (git remote add origin blah blah blah)
  * Paste the code into your GitBash terminal window. Hit enter if needed. Read the happy little Writing Objects 100% success message.
  * Now, refresh your browser window on the github page. **WOW, your files are there!! Amazing!**
8. In the future, to push changes made on your local machine up to GitHub, use `git push origin master`. To get changes made by yourself in the online editor, use 'git pull origin master'. Get in the habit of doing these regularly, so that both are in sync. Git knows which file was updated most recently, and will let you know if there is a merge conflict it can't resove. Hooray!




  




