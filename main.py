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

        # construct post request for completion
        headers = {'Content-type':'application/json','Authorization': 'Bearer {}'.format(OPENAI_API_KEY)}
        #r = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)

        # TODO - implement sanification on live responses and return


        # prototyping string sanification
        test_res = '{"id": "cmpl-2l2DPoXWLq88CVKW3Kk0oC0PQURPr", "object": "text_completion", "created": 1617562607, "model": "davinci:2020-05-03", "choices": [{"text": "\\n\\n<div style=\\"background-color:red;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:blue;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:green;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:yellow;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:orange;\\">\\n\\n</div>\\n\\n<div style=\\"background-color:", "index": 0, "logprobs": null, "finish_reason": "length"}]}'
        # strip escape characters
        test_res = test_res.replace('\\n', '')
        test_res = test_res.replace('\\', '')
        print(test_res)
        test_res = json.loads(test_res)
        test_res = json.dumps(test_res["choices"][0]["text"])
        return test_res #r.text, True

if __name__ == "__main__":
    res = query('What is the html code for a red button??')
    print(res)

