# Readme

## Install

Install [python3](https://www.python.org/downloads/), pip3 (comes with python). 

### To get virtualenv set up

Navigate to `/gptBot`

	pip3 install virtualenv
	virtualenv venv
		
Windows
	
	call venv/Scripts/activate

MacOS/Linux

	source venv/Scripts/activate

Install dependencies

	pip3 install -r requirements.txt

To freeze dependencies

	pip3 freeze > requirements.txt


You might need to `sudo apt-get update` and `sudo apt-get upgrade`

You might also need to install the latest setuptools for tensorflow (if it throws a warning during install)

	pip3 install setuptools

## Files

Make sure you have a folder in the root of this project called `checkpoint` with the models inside.

Extracting the `checkpoint_run1.tar` file should create this checkpoint folder.

Note: currently we are only using the run named `run1`.

## Run

	python3 server.py

Hit the server with a GET request at `localhost:5000/message` and it should respond with generated text. 

Note: it takes ~10-15 seconds to generate the text and respond as it has to create the session and load the model on each call (need to find a way to create/load before the call and just generate on api call)

I am not training the model locally



### Resources
https://github.com/minimaxir/gpt-2-simple
https://www.tensorflow.org/install/pip
https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce
