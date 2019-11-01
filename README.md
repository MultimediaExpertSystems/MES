# MES
### To start you virtual environment follow this directions:
#### On windows:
1. Upgrade pip
 ` py -m pip install --upgrade pip `
2. Install virtualenv
 ` py -m pip install --user virtualenv `
3. Start virtual env
 ` py -m venv env `
4. Activate your virtual environment
` .\env\Scripts\activate `
5. Install all modules:
` pip install -r requirements.txt `

#### To run the ImgDownload Python script:
1. Change the queries based on the images needed then:
` py imgDownload.py `
## Inference Engine Rules:

If the user sets a limit to the number of images displayed, then the search results will display a limited number of pages
If the search query is empty, then the most popular images will be displayed on UI
If the user chooses a specific “sort by” option, such as relevance or popularity, then the program will organize the images shown by that option.
If the user inputs a specific team, then media with subsections of that team will also be displayed, not just the images tagged with that specific team.
If the user inputs a specific field position, then the program will display media with all players of that position across all different teams.
If the user inputs a query relating to a specific gender, such as women’s specific teams, then the search result will display images related to teams with that gender
If the user inputs a query relating to countries, such as Colombian teams, then the search results will display results relating to that specific country.
If user’s input is not found on database, then a “not found” message will be displayed on UI
If the user hovers over a search result, then a download icon will show where the image can be downloaded
If the user inputs a query relating to a specific player, such as Cristiano Ronaldo, then the results will display images relating to the specific player

## Analysis:
For the input of our program, we will take in text. This text will then be used to search through our database for pictures and gifs that match the given description. Any media that does match will then be displayed on the screen. We will search through several different tags. For example, if someone requests a certain team, we will not only pull up media that’s tagged with the whole team, but also media that’s tagged with one or more of the team’s members.
 
## Design:

Design: How many program modules are required? Which programming language should be used for each program module? Should you use OOP?  If YES, how many classes/methods are required? What are the potential shared classes/methods, i.e., core of the system?


We will need a total of 3 program modules. The first module will be a database containing the media and their respective tags. This module is what will be used to provide us with all our media and we will filter through this database to only get the media with appropriate tags. The next module will be a database that contains text information detailing different levels of specification. So, for example, we will have each team and within that team we will have all known members of that team. This is what will allow us to provide media not directly specified by the user, but media that is related to it. Finally, we will have our GUI which will provide all the visuals and will help us implement the rules. As far as programming language, we will be using python to code a lot of our program. We will also test LISP and PROLOG and see which one works best for this program, then continue coding in whichever one turns out to be more efficient.
  
## Execution Plan: 
We will all work on each module at a time. So, we will first develop the database of images, then the database of team information, then the GUI and rule implementation. We have chosen this layout so that every team member can be active at each step of development and get the most out of this project.

For the actual implementation of the code, we are to use python which is an OPP. 

![Domain Expert Information](http://www.netlancers.com/us/wp-content/uploads/2014/04/domain-expert.jpg)


