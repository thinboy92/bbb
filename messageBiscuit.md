# Message

#### Initial Message (TheEnginner -> biscuit)

Please write your messages using Markdown on SublimeText2. You should use the same file to write messages. If you need references on Markdown, please refer to [this](http://daringfireball.net/projects/markdown/) but I believe that by following my template, it would be enough.

##### On Git/working in a Team
To my _padawan_, biscuit, please do all the exercises that I have assigned to you. If you want to leave me a message, please do so in 
this message so that we can communicate better.

To start this project, you need to fork my repo first then, clone your fork into your local machine. Everything else will be the same. 
Run this on your terminal, `git remote add upstream git@github.com:afeezaziz/bbb.git`. So there will be two remote repo for you. One is 
you fork, where you would on your own,_origin_ and one repo where all of us will share, _upstream_. If you need help with forking, 
please refer to [this](https://help.github.com/articles/fork-a-repo).

Write your code, then commit and push to your fork. It is good that to always pull from original repo, _upstream_ before you commit to 
your fork to see changes made to the repo by other developers while you are writing your code. You should pull from _upstream_. Pull is 
fetch and merge done together.

Then, it is time to integrate your code with the original repo. This is git push/pull/fork exercise is to teach you to work in a team. 
There is no single rock star developer that can survive on his own. We need to collaborate with others to build great things. Ok enough 
of my rant. After you push your code to your forked repo, go to the page for original repo, that is my [repo](https://github.
com/afeezaziz/bbb) and click the pull request button. If you need help with this, please refer to [this](https://help.github.
com/articles/using-pull-requests).

##### On Flask

Please refer to README to check the milestones. 

*Always remember to activate virtual environment and pip install necessary requirements*

##### Initial workflow(For working on existing project on Github)

*Must fork the project on Github first*

* `cd /path/to/folder`
* `git clone git@github.com:<yourgithubusername>/bbb.git`
* `cd bbb`
* `virtualenv venv --distribute`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `git remote add upstream git@github.com:afeezaziz/bbb.git`

##### To make changes workflow(For working on existing project on Github)

* `cd /path/to/folder`
* `git pull upstream`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* __write your code__
* `git add .`
* `git commit -m "message"`
* `git push origin`
* Go to original repo on afeezaziz/BBB
* __pull request__ on github

#### Message 1 (biscuit -> TheEngineer)

*Your message here, if any*.