# Logos

1) Change install.sh to match whatever OS you're using.  Mine uses the "brew" commands because I'm using MacOS, so if you're using Linux to something like:

apt-get update
apt-get upgrade
apt-get install python3-pip postgresql sqlite3
pip3 install -r requirements.txt

2) Run install.sh 

2.1) Once you've done this, you should be able to run the app locally by doing:

python3 main.py

3) Create your virtual environment and activate it:

python3 -m venv env
source env/bin/activate

4) Install the Google Cloud SDK if you don't have it already, instructions here:

https://cloud.google.com/sdk/docs/

5) After you've signed in to your account, set your current project to Logos:

gcloud config set project logos-257201

6) If you want to deploy your current version of the app to the cloud, do:

gcloud app deploy

Be careful.  We've yet to set up a development v. production server, so we shouldn't break things.  Don't commit to the reposity unless you've deployed your code and it works on the cloud.

