import os

run_cmd_1 = 'cd frontend'
run_cmd_2 = 'npm install'
run_cmd_3 = 'npm run build'

os.chdir('frontend')
os.system(run_cmd_2)
os.system(run_cmd_3)