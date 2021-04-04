import requests
import json
import openai
from config import OPENAI_API_KEY

# set OpenAi options
openai.organization = "org-hN5K4IM6TydLmGiuBRWbzJvs"
openai.api_key = OPENAI_API_KEY
openai.Engine.list()

# construct post request for completion
data = json.dumps({"prompt": "Q: What is the html code for a table with twelve columns, one for each month of the year, containing the average temperature in Rome?", "max_tokens": 100, 'temperature':0.1, 'top_p':1, 'frequency_penalty':0, 'presence_penalty':0, 'stop':'?', 'n':1})
headers = {'Content-type':'application/json','Authorization': 'Bearer {}'.format(OPENAI_API_KEY)}
print(headers)
r = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)
print(r.text)


