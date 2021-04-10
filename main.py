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
        data = json.dumps({"prompt": prompt, "max_tokens": 100, 'temperature': 0.1, 'top_p': 1, 'frequency_penalty': 0,
                           'presence_penalty': 0, 'stop': '?', 'n': 1})
        r = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)


        # sanify response
        r = r.text
        r = r.replace('\\n','')
        r = json.loads(r)
        r = json.dumps(r["choices"][0]["text"])
        print(r)
        r = r.replace("\"",'')
        print(r)

        return r

if __name__ == "__main__":
    res = query('What is the html code for a red button??')
    print(res)

