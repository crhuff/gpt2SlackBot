import gpt_2_simple as gpt2
import tensorflow as tf
from flask import Flask, json



api = Flask(__name__)


@api.route('/', methods=['GET', 'POST'])
def get_main():
	return "server running"

@api.route('/message', methods=['GET'])
def get_test():
	sess = gpt2.start_tf_sess(threads=1)
	gpt2.load_gpt2(sess)
	message = gpt2.generate(sess,
		length=30,
		temperature=0.7,
		nsamples=1,
		batch_size=1,
		return_as_list=True
		)[0]
	return message


if __name__ == '__main__':
	api.run()