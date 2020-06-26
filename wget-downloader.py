import subprocess
command = 'wget'
arg1 = '--mirror'
arg2 = '--convert-links'
arg3 = '--adjust-extension' 
arg4 = '--page-requisites'
arg5 = '--no-parent'

url = 'https://python.org'

try:
    subprocess.check_output([command, arg1, arg2, arg3, arg4, arg5, url])
except subprocess.CalledProcessError as e:
    print(e.output)
