import os
import boto3
import sys
from datetime import datetime


def main():
    key = os.environ["AWS_KEY"]
    secret = os.environ["AWS_SECRET"]
    region = os.environ["AWS_REGION"]
    project = os.environ["CODEBUILD_PROJET_NAME"]

    codebuild = boto3.client(
        'codebuild',
        region_name=region,
        aws_access_key_id=key,
        aws_secret_access_key=secret,
    )

    response = codebuild.list_builds_for_project(
        projectName=project,
        sortOrder='DESCENDING'
    )

    log_stream_name = response['ids'][0].split(":")[1]

    logs = boto3.client(
        'logs',
        region_name=region,
        aws_access_key_id=key,
        aws_secret_access_key=secret,
    )

    response = logs.get_log_events(
        logGroupName=f'/aws/codebuild/{project}',
        logStreamName=log_stream_name,
        startFromHead=True
    )

    for log in response['events']:
        time = datetime.fromtimestamp(log['timestamp'] / 1000)
        event = log['message']
        if len(event.strip()) > 1:
            print(f'{time.strftime("%Y-%m-%d %H:%M:%S")}: {event.strip()}')

    sys.exit(0)


if __name__ == "__main__":
    main()
