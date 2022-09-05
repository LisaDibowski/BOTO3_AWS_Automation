import boto3
#import the boto3 library

aws_mag_con_root=boto3.session.Session(profile_name="root")
aws_mag_con_root=boto3.session.Session(profile_name="ec2_developer")
#With session.Session(profile_name="null") you can create a session for a specified user

iam_con_re=aws_mag_con_root.resource(service_name='iam',region_name="us-east-2")
iam_con_cli=aws_mag_con_root.resource(service_name='iam',region_name="us-east-2")
#specify region

for each_user in iam_con_re.users.all():
	print(each_user.name)
#for loop to print all users 
