
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzczZTQ1YzQtOGRhMi00ZDZmLWExYmYtODE5ZTM1MTQxNGUxIiwidHlwZSI6ImFwaV90b2tlbiJ9.6P3GFMvsrp5HQVhcM-Grvy6dko6F0alcFTjnLAy2AnM

import sys


import openai
from flask import Flask, render_template, request
from asgiref.wsgi import WsgiToAsgi  # Use asgiref to convert Flask to ASGI

app = Flask(__name__)

# Set your OpenAI API key securely from environment variables
openai.api_key = ''

def convert_to_support_tone(input_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or any other model you prefer
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Convert the following text into a professional and supportive tone:\n{input_text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error occurred: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_text = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        converted_text = convert_to_support_tone(user_input)
    return render_template('index.html', converted_text=converted_text)

# This is the ASGI entry point
asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    # Run the app using Uvicorn
    import uvicorn
    uvicorn.run(asgi_app, host="0.0.0.0", port=80)













sys.exit(0)

import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Set your OpenAI API key (make sure to use your own key here)
openai.api_key = ''


def convert_to_support_tone(input_text):
    # Call OpenAI API to convert text into a more professional tone using the correct method
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or any other model you prefer
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",
             "content": f"Convert the following text into a professional and supportive tone:\n{input_text}"}
        ]
    )

    # Return the generated text
    return response['choices'][0]['message']['content'].strip()


@app.route('/', methods=['GET', 'POST'])
def index():
    converted_text = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        converted_text = convert_to_support_tone(user_input)
    return render_template('index.html', converted_text=converted_text)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=80)




