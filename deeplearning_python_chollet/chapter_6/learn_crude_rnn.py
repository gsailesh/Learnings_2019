import numpy as np

INPUT_FEATURES = 32
OUTPUT_FEATURES = 64
TIMESTEPS = 100

inputs = np.random.random((TIMESTEPS, INPUT_FEATURES))

def learn_crude_rnn(inputs, input_features=INPUT_FEATURES, output_features=OUTPUT_FEATURES):

	state_t = np.zeros(output_features)
	W = np.random.random((input_features, output_features))
	U = np.random.random((output_features, output_features))
	b = np.random.random((output_features,))
	
	print("Dims: W {} U {} b {}".format(W.shape, U.shape, b.shape))
	successive_outputs = []
	
	for input_t in inputs:

		output_t = np.tanh(np.dot(input_t, W) + np.dot(U, state_t) + b)
		successive_outputs.append(output_t)
		
		state_t = output_t
		print(state_t)
	
	output_sequence = np.concatenate(successive_outputs, axis=0)
	return output_sequence
	

print(learn_crude_rnn(inputs))
