import requests
import json
import openai
from config import OPENAI_API_KEY

def gpt(prompt):
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
        data = json.dumps({"prompt": prompt, "max_tokens": 100, 'temperature':0.0, 'top_p':1, 'frequency_penalty':0, 'presence_penalty':0, 'stop':'?', 'n':1})
        headers = {'Content-type':'application/json','Authorization': 'Bearer {}'.format(OPENAI_API_KEY)}
        print(headers)
        r = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)

        # TODO parse response and trim to code elements
        # sample response:
        #('{"id": "cmpl-2l2DPoXWLq88CVKW3Kk0oC0PQURPr", "object": "text_completion", "created": 1617562607, "model": "davinci:2020-05-03", "choices": [{"text": "\\n\\n<div style=\\"background-color:red;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:blue;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:green;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:yellow;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:orange;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:", "index": 0, "logprobs": null, "finish_reason": "length"}]}\n', True)

        return r.text, True

if __name__ == "__main__":
    res = query('WHat is the html code for a red button??')
    print(res)

