import configparser
import paramiko as paramiko
import mysql.connector
from mysql.connector import Error


def getconfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')

    return config


server_config = {
    'hostname': getconfig()['server']['host'],
    'port': getconfig()['server']['port'],
    'username': getconfig()['server']['user_name'],
    'password': getconfig()['server']['password'],
}


def getServerconfig():
    try:
        server = paramiko.SSHClient()
        server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        server.connect(**server_config)
        print("ssh connection to server is successful")
        return server
    except Error as e:
        print(e)


def UploadFilesToServer(server, sourcepath, destinationpath):
    try:
        sftp = server.open_sftp()
        sftp.put(sourcepath, destinationpath)
        print("moved file from source local  to destination server via FTP")
        return sftp
    except Error as e:
        print(e)


def DownloadFilesFromServer(server, sourcepath, destinationpath):
    try:
        sftp = server.open_sftp()
        sftp.get(sourcepath, destinationpath)
        print("downloaded file from server to local via FTP")
        return sftp
    except Error as e:
        print(e)
