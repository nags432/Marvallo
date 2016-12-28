from fabric.api import *
from fabric.colors import green, red

path_to_dev = '/users/dreambig/coding_practice/marvallo_django'

def prepare_deployment(branch_name):
	local('python manage.py test marvallo_django')
	local('git add -p && git commit') #or local 

def staging() :
    #"""This pushes to the EC2 instance defined below"""
    # The Elastic IP to your server
    env.host_string = 'staging.marvallo.com'
    # your user on that system
    env.user = 'ubuntu' 
    # Assumes that your *.pem key is in the same directory as your fabfile.py
    env.key_filename = 'WindowsJSKey.pem'
    # path to the directory on the server where your vhost is set up
    global path
    path = "staging.marvallo.com/"
    #branch to pull from
    global branch
    branch = "staging"
    

def deploy():
	#name of application process
	process = "beyond"
	
	print (red("Beginning Deploy:"))
	print(branch)
	print(path)
	
	with cd("%s" % path):
		run("pwd")
		
	
		
		