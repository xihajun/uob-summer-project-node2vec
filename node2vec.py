from multiprocessing import Pool
from subprocess import Popen, PIPE
import glob
import os
import subprocess
from multiprocessing.dummy import Pool # use threads
from subprocess import check_output

f_list = glob.glob('node2vec_input/*.txt')

# get the outputlist
def outputlist(input_filename):
    temp = input_filename.split('/')
    temp[0] = 'node2vec_output'
    return "/".join(temp)

output_filename = [outputlist(f_list[i]) for i in range(len(f_list))]

file_name = [[f_list[i],output_filename[i]] for i in range(len(f_list))]


node2vec_input_dir = '.' + "/node2vec_output/"
os.makedirs(node2vec_input_dir, exist_ok=True)
cmds_list = [['python', './src/main.py','--input',input_filename, '--output', output_filename] for input_filename, output_filename in file_name]


for i in range(len(cmds_list)):
    try:
        subprocess.run(cmds_list[i])
        #temp = cmds_list[i].split(' ')
        print(cmds_list[i])
        subprocess.run(["rm",cmds_list[i][3]])
    except:
        print("fail")
