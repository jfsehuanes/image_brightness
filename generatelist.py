import sys
import glob
import numpy as np

from IPython import embed

if len(sys.argv) != 2:
    print("No has mencionado de cual carpeta quieres analizar!")
    quit()

folder_path = sys.argv[1]

if folder_path[-1] != '/':
    folder_path += '/'

im_ls = glob.glob(folder_path + '*.JPG')

# correct files with spaces
ind = np.where(np.array([' ' in e for e in im_ls]))[0]

# create parallel jobs for user specific folder:
job_name = 'task_list.txt'

task_list = ['python3 img_brigthness.py ' + '"%s"' % e for e in im_ls]
task_list = np.sort(task_list)
if len(task_list) > 0:
    np.savetxt(job_name, task_list, fmt="%s")

print('Task-list terminated. Tasks stored in %s' % job_name)
