import json
import datetime
import boto3


def lambda_handler(event, context):
    if event["source"] != "aws.ecs":
        raise ValueError("Function only supports input from events with a source type of: aws.ecs")

    if event["detail-type"] == "ECS Task State Change" and event["detail"]["lastStatus"] == "STOPPED":

        # get stoppedReason
        task_stopped_reason = event["detail"]["stoppedReason"].replace(" ", "-")

        print('Here is the event:')
        print(json.dumps(event))

        cloudwatch = boto3.client('cloudwatch')

        # 前回の値を取得
        # data = cloudwatch.get_metric_statistics(
        #     Namespace='maehachi08/Ecs/StoppedReasonCount',
        #     MetricName='EcsStoopedEventCount',
        #     Dimensions=[
        #         {
        #             'Name': 'EventName',
        #             'Value': task_stopped_reason
        #         },
        #     ],
        #     StartTime=datetime.datetime.now() - datetime.timedelta(days=1),
        #     EndTime=datetime.datetime.now(),
        #     Period=300,
        #     Statistics=['Sum']
        # )

        # print(json.dumps(data))
        # sum_count = data["Datapoints"][0]["Sum"] + 1

        PutMetricData = cloudwatch.put_metric_data(
            Namespace='AWS/ECS',
            MetricData=[
                {
                    'MetricName': task_stopped_reason,
                    'MetricName': 'haste_t1_development_us-west-2-01_ecs-shrd01',
                    'Value': 1,
                    'Unit': 'Count',
                    'Dimensions': [
                        {
                            'Name': 'ClusterName',
                            'Value': 'test',
                        }
                    ]
                }
            ]
        )

        for container in event["detail"]["containers"]:
            # each container
            #  {
            #      "containerArn":
            #      "lastStatus":
            #      "name":
            #      "taskArn":
            #  }
            if container["lastStatus"] == "STOPPED":
                pass

