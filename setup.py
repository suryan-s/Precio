import os

run_cmd_1 = 'python -m venv .venv'
run_cmd_2 = 'source .venv/Scripts/activate'
run_cmd_3 = 'pip install -r requirements.txt'
run_cmd_4 = 'cd frontend'
run_cmd_5 = 'npm install'
run_cmd_6 = 'npm run build'

jobs = [run_cmd_1, run_cmd_2, run_cmd_3, run_cmd_4, run_cmd_5, run_cmd_6]
for i in range(len(jobs)):
    if jobs[i].startswith(run_cmd_4):     
        os.chdir('frontend')
    else:
        os.system(jobs[i])