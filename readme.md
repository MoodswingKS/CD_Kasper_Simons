# You need to master the following to complete this assignment:

Creating and provisioning a server at Digital Ocean;
Connecting to a Linux server over SSH;
Running basic terminal commands on a Linux server;
Deploying a Flask application on a Linux server.


## The continuous deployment pipeline should look like this:

You manually write, commit and push some code. This only requires you to be familiar with git.

GitHub Actions runs tests on your code. You can use Pytest for this.

If and only if the tests pass, GitHub Actions logs into the VPS you have running with Digital Ocean 
and runs commands such that the code is updated to the latest version.


### Finally, write a short, 200/300-word report in which you discuss at least the following:

Name three components of your solution, explain what they are and how they relate to each other. 
A 'component' can be anything from GitHub Actions or Bash to Digital Ocean and SSH.
Discuss three problems that you encountered along the way and how you solved them.
(optional) Anything of note that you want to share about the process of solving this assignment.

### Tips

Tip 1: GitHub: Deploy Keys
Tip 2: sh files.
Tip 3: Secrets.

### Extra to do

It's usually not a good idea to give continuous deployment pipelines root access to your server, 
but we will accept it for this assignment. 
If you are interested, you can look into how to create and use new users on Ubuntu (and Linux in general).