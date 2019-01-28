import boto.sns, time, json, logging
from datetime import datetime
import os
import tailer
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
region = os.environ['REGION']
sns_topic_arn = os.environ["SNS_TOPIC_ARN"]
tag = os.environ["TAG"]
file_path = "/logs"
logging.basicConfig(filename="sns-publish.log", level=logging.DEBUG)
c = boto.sns.connect_to_region(region, aws_access_key_id = aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
while 1:
    for body in tailer.follow(open(file_path)):
        subject = str(time.time()) + " " + tag
        print str(time.time())
        publication = c.publish(sns_topic_arn, body, subject)