# Autocoder

Autocoder is a frontend to OpenAI's GPT-3, made with access to the beta generously provided by OpenAI at the recent [Scale Transform Conference](https://scale.com/events/transform). 

It takes a description of a webpage and renders the page automatically. It is currently trained on simple html elements and uses the ```ada``` and ```davinci``` semantic and completion models respectively. The API endpoint used is ```/answers```.

Inspired by the demo of [Sharif Shameem](https://twitter.com/sharifshameem).

It is written in Python, with a Bootstrap frontend. The API was implemented in Flask and there are a series of unit tests in ```test_suite.py```.

## Installation

Install requirements

```bash
pip install -r requirements.txt
```

## Usage

Start the server:

```python
python app.py
```
Navigate to ```localhost:5000``` in your browser, enter your prompt and click ```Submit```.

Please note: you will need an API key from OpenAI to construct the post request - save it in a file called ```config.py``` as ```OPENAI_API_KEY```.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)