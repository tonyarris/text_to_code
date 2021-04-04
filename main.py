import requests
import json
import openai
from config import OPENAI_API_KEY

def query(prompt):
    # convert to string
    prompt = str(prompt)

    # check prompt is not whitespace or empty
    if (prompt.isspace() == True) | (len(prompt) == 0):
        return False
    else:
        # set OpenAi options
        openai.organization = "org-hN5K4IM6TydLmGiuBRWbzJvs"
        openai.api_key = OPENAI_API_KEY
        #openai.Engine.list()

        # construct post request for completion
        data = json.dumps({"prompt": prompt, "max_tokens": 100, 'temperature':0.1, 'top_p':1, 'frequency_penalty':0, 'presence_penalty':0, 'stop':'?', 'n':1})
        headers = {'Content-type':'application/json','Authorization': 'Bearer {}'.format(OPENAI_API_KEY)}
        print(headers)
        r = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)

        return r.text, True

# if __name__ == "__main__":
#     res = query('What is your name?')
#     print(res)

