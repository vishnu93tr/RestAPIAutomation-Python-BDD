import paramiko as paramiko
from utilities.configuration import *
import time
import csv

server = getServerconfig()

# Run commands from server

UploadFilesToServer(server, 'BatchFiles/script.py', 'script.py')
UploadFilesToServer(server, 'BatchFiles/loanapp.csv', 'loanapp.csv')

stdin, stdout, stderr = server.exec_command('python script.py')
time.sleep(5)
print(stdout.readlines())

DownloadFilesFromServer(server, 'loanapp.csv', 'output/loanapp.csv')

# Parse output file
with open('output/loanapp.csv') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    for row in reader:
        if row[0] == 'Srinivas':
            assert row[1] == 'rejected'
server.close()
