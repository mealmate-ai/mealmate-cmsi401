# Progress Log for 401
## My Overall Goal
For this project, I am hoping to migrate the current Coco Nutritionalist iOS app over to AWS, having the storage, database, and processing all held within AWS services. This is my chronological but not dated log of progress.

## Log #1

We were able to access the current lana_database and see all 15 tables and what their purpose is. To access the database, we used the psql command:

    psql postgresql://sls:<insert_password_here>@lana-database.czvpopdnxi2n.us-east-2.rds.amazonaws.com:5432/lana_database

This accessed the RDS database by including all the information within the host name (password, username, etc). After sifting through the data, we figured out that it would be best to make a copy of this database, then from that copy pull all the data we needed into a fresh and final database. 

## Log #2
We began on the process of refining the database by attempting to copy over the database to a new duplicate. This proved to be much harder than I anticipated as the snapshot instance I copied was not accessable no matter what I did. To work around this, I decided to use pg_dump instead to get a local dump of the database and copy from there. Here's the command:

    pg_dump -h lana-database.czvpopdnxi2n.us-east-2.rds.amazonaws.com -U sls -f lana-database-copy.sql lana_database

With that local copy of the database dump, I then booted up a fresh RDS instance running PostgreSQL called lana-database-copy and ran this command to import the dump and set up the database:

    psql --host=lana-database-copy.czvpopdnxi2n.us-east-2.rds.amazonaws.com --port=5432 --dbname=lana_database --username=sls --password < lana-database-copy.sql
    
After testing this and making sure my IP address was added to the security group, I finally have access to a standalone copy of the database!

## Log #3
I began by finding where the iOS Swift code connects to the back end using the RDS url. This is all held in the *LanaAPI.swift* file. Also *db_models* is essential in understanding the connection to the database. This was a quick session but helpful in getting an overview of the swift code in relation to the back end.

## Log #4
To get an overview of the current architecture vs the architecture I am going to be making, I decided to make two architecture diagrams from draw.io (a really good site for working with AWS icons).

Here is the before diagram:

![Before Diagram](https://github.com/mealmate-ai/mealmate-cmsi401/blob/master/backend/images/BeforeDiagram.png)

This diagram shows the current hybrid state of the architecture, and definetly shows theres a lot to move over to make things entirely on AWS.

Here is the diagram of what we're aiming for:

![After Diagram](https://github.com/mealmate-ai/mealmate-cmsi401/blob/master/backend/images/DailyBites.png)

This shows everything on AWS (keep in mind the Swift iOS code is being held elsewhere and uploaded to Apple for the app store).

## Log #5
We finally decided to make a final version of the database so we could load just the data we would be using for Daily Bites. This proved to be MUCH more difficult than I initially anticipated because it required me to make a new VPC, internet gateway, subnets, subnet groups, security groups, and route everything properly so the database was accessable. After finall doing this, we now have a the database (empty for now).

## Log #6
This was a quick session, but I added the schema that Bree sent me to load the 9 tables she had designed into the database. We went over these as a group to understand what the purpose was of each and to highlight that it is subject to change.

## Log #7
I began the setup process for the flask server that will be run on an EC2 instance. To begin, I created a EC2 instance with Amazon Linux 2 running. The instance was in a new public subnet that could be SSHed into from only my IP address, but group members could add theirs as well. Once it was up and running, I ran the command:

    sudo yum update
    
in order to update the AMI to the newest version (and to check network connectivity). Then I ran the command:

```
yum install -y python3-pip python3 python3-setuptools
```
to install python3 for the flask server. Then I would need pip for package installation, so I ran the commands on the steps for installing pip off this AWS forum (not installing EB CLI):

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html

Finally I could install flask with this command:

    sudo pip3 install flask

I also installed nginx which I am unsure if it is necessary or not.

    sudo amazon-linux-extras install nginx1
    
After that, I made an app.py that is just a "hello world!" test flask app. It has this python code:

    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    
    def hello():
    
    return "Hello World!"
    
    if __name__ == '__main__':
    
    app.run()


This was a great resource for debugging:
https://pyliaorachel.github.io/blog/tech/system/2017/07/07/flask-app-with-gunicorn-on-nginx-server-upon-aws-ec2-linux.html

## Log #8
Finally Bree and I were able to get the finalized Flask code running on the EC2 instance. This was also made accessable for Bree, proving a full connection between the EC2 instance, the database, and now an external user (Bree). This proves that the setup is ready for the use in the front end! The only issue is that this is being run in the foreground, so whenever the SSH connection is broken on my end, Bree is unable to access the flask server because it shuts down.

## Log #9
To fix the flask server from shutting down, I am going to put the flask server on a virtual environment on the EC2 server that can keep running in the background. In order to do this, I ran these commands:

I realize now that this wont be sufficent for even multiple users at the same time since flask doesn't support that scale of traffic, but seems to only support a single user at a time. In order to fix this issue, I am going to go with Gunicorn and Nginx, as that seems standard. This is the first task for next semester.
