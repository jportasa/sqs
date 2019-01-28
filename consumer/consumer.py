import boto.sqs, time, json
import os
from datetime import datetime
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
region = os.environ['REGION']
sqs_queue_name = os.environ["SQS_QUEUE_NAME"]
conn = boto.sqs.connect_to_region(region, aws_access_key_id = aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
queue = conn.get_queue(sqs_queue_name)
x = 0
while 1:
    try:
        result_set = queue.get_messages()
        if result_set != []:
            message = result_set[0]
            print str(time.time())
            message_body = message.get_body()
            m = json.loads(message_body)
            subject = m["Subject"]
            body = m["Message"]
            message_id = m["MessageId"]
            conn.delete_message(queue, message)
    except IndexError:
        pass