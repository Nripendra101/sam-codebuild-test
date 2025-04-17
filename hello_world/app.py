import json
import pandas as pd


def lambda_handler(event, context):
    count=int(event['count'])
    data=[]
    for i in range(count):
        data.append(i*10)
    df=pd.DataFrame(data,columns=['Numbers'])
    print('data:')
    print(df)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world and i am in Hyderabad",
            "count":count
            # "location": ip.text.replace("\n", "")
        }),
    }
