import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
#iam,ec2 and s3
iam_con_cli=aws_mag_con.client(service_name="iam",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
s3_con_cli=aws_mag_con.client(service_name="s3",region_name="us-east-1")

'''
#List all iam users using client objects
response_users=iam_con_cli.list_users()
for each_item in response_users['Users']:
        print(each_item)
'''

#List all ec2 instace IDs
response_instances=ec2_con_cli.describe_instances()
#print(response_instances['Reservations'])
for each_item in response_instances['Reservations']:
        for each_instance in each_item['Instances']:
                print(each_instance['InstanceId'])
        print('----------------')


response_cert = iam_con_cli.list_signing_certificates(
    UserName='Simon')

print(response_cert)
