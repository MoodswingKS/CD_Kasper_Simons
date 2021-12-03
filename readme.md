# CD Project

I’ve managed to create a continuous development pipeline through the use of a VPS (droplet @ digitalocean), nginx, python, flask and gunicorn. 

A commit made in this repository will execute a series of commands through the SSH connection I’ve configured in github. I have another SSH link, specifically made for without the use of Github - for me to check if all steps in the workflow have been done correctly.

While building the pipeline I’ve encountered numeral issues, so I narrowed down the top three issues I faced:

### Gunicorn
Gunicorn was my biggest hurdle in the whole process. Even after successfully running the flask application on the VPS, gunicorn refused to identify the application. 
The solution was to learn to ‘read better’. 

### SSH connection
Creating a valid SSH connection between github and the VPS served a lot more complications than initially necessary. As I’m working on Windows, the ‘easy’ method of creating an SSH-key was not working for me. So I used Putty as a tool to create one. But Putty gives me a ‘fingerprint’ in the key, which Github refused to identify which led to errors. With the help of one of the teachers, I created a new key with Git Bash and the issue was immediately fixed.

### Nginx / app.service
In the linux terminal the format of an error is less descriptive than I would have hoped for. 
A simple error code gave me hours of headaches, as I couldn’t figure out yet that error-200 simply meant that I had misspelled a directory somewhere. Through the use of ‘jounalctl -xe’. ‘systemctl status app.service’ and google, I got the answers to those errors.

Kasper Simons