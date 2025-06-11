import json
import boto3

# Create Bedrock Runtime client
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

# Model ID for Claude 3 Haiku
model_id = 'anthropic.claude-3-haiku-20240307-v1:0'

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_input = body.get('message', '')

        if not user_input:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No message provided'})
            }

        # Claude 3 uses Messages API
        response = bedrock.invoke_model(
            modelId=model_id,
            contentType='application/json',
            accept='application/json',
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [
                    {"role": "user", "content": user_input}
                ],
                "max_tokens": 300,
                "temperature": 0.7,
                "top_p": 0.9
            })
        )


        response_body = json.loads(response['body'].read())
        answer = response_body['content']

        return {
            'statusCode': 200,
            'body': json.dumps({'response': answer})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
