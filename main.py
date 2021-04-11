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

        # construct post request for answer
        headers = {'Content-type':'application/json','Authorization': 'Bearer {}'.format(OPENAI_API_KEY)}
        data = json.dumps({"search_model": "ada",
                           "model": "davinci",
                           "question": prompt,
                           "examples": [["A button with 'Submit' written on it", "<button type=\"button\">Submit</button>"],
                                        ["A form to enter your name and surname and an enter button","<form action=\"/action_page.php\"><label for=\"fname\">First name:</label><br><input type=\"text\" id=\"fname\" name=\"fname\" value=\"John\"><br><label for=\"lname\">Last name:</label><br><input type=\"text\" id=\"lname\" name=\"lname\" value=\"Doe\"><br><br><input type=\"submit\" value=\"Submit\"></form>"]],
                           "examples_context":"Generate the html and javascript code to realise the description given.",
                           "documents": [],
                           "max_tokens": 250, 'temperature': 0.3, 'n': 1})
        r = requests.post('https://api.openai.com/v1/answers', headers=headers, data=data)
        #print(r.content)


        # sanify response
        r = r.text
        r = r.replace('\\n','')
        r = json.loads(r)
        r = json.dumps(r["answers"][0])
        print(r)
        r = r.replace("\\\"",'"')
        r = r.replace("---", "")
        print(r)

        return r

if __name__ == "__main__":
    res = query('What is the html code for a red button??')
    print(res)

