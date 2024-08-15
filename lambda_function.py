import json
import requests
import boto3
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def extract_text_from_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text
    else:
        return None

def invoke_llm(question, prompt, website_text):
    if website_text:
        prompt += "\n" + website_text  

    bedrock_runtime_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )
    response = bedrock_runtime_client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        body=json.dumps(
            {
                "anthropic_version": 'bedrock-2023-05-31',
                "max_tokens": 2500,
                "messages": [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": prompt + question}],
                    }
                ],
            }
        ),
    )
    
    body = response['body'].read().decode('utf-8')
    body_json = json.loads(body)
    rules_text = body_json['content'][0]['text']
    
    return rules_text

def lambda_handler(event, context):
    prompt = """
    You are the hotel manager of Landon Hotel, named "Mr. Landon". Your expertise is exclusively in providing advice about anything related to Landon Hotel. This includes any general Landon Hotel-related queries.
    You do not provide information outside of this scope. 
    If a question is not about Landon Hotel, respond with, "I can't assist you with that, sorry!"
    
    """
    
    target_url = "https://www.landonhotel.com/"
    website_text = extract_text_from_website(target_url)

    if 'body' not in event:
        logging.error("Body is null")
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Invalid payload"}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
            }
        }

    try:
        body = json.loads(event['body'])
        question = body.get('question', '')
        
        if not question:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No question provided'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST',
                }
            }
        
        answer = invoke_llm(question, prompt, website_text)
        return {
            'statusCode': 200,
            'body': json.dumps({'answer': answer}),
            'headers': {
                #'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
            }
        }
    except Exception as e:
        logging.error(f"Exception: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f"Error: {str(e)}"}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
            }
        }
