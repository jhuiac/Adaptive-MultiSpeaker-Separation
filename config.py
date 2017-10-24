########################
## DATA CONFIGURATION ##
########################
import os


workdir = os.path.dirname(__file__)
floydhub = (workdir == '/output') #We are on Floydhub


if floydhub:
	print 'We are on Floydhub'
	h5py_root = '/h5py_files'
else:
	print 'We are on PC'
	h5py_root = os.path.join(workdir, 'h5py_files')

log_dir = os.path.join(workdir,'log')


###
## Raw data
###

data_root = 'data/LibriSpeech'
data_subset = 'dev-clean'
dev_clean_speakers = 40

#########################
## AUDIO CONFIGURATION ##
#########################

fs = 16000 
fftsize = 256
overlap = 2
window = 'hann'


#########################

embedding_size = 40
threshold = 1e-8
chunk_size = 40
batch_size = 32
batch_test = 1
stop_iterations = 10000
max_iterations = 1000000