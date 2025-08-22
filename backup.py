from backupcfg import backupFile
from backupcfg import srcDir
from backupcfg import srcFile
from backupcfg import dstDir

#!/usr/bin/python3

"""
This Python code demonstrates the following features:

* send an email using the elasticemail.com smtp server.

"""

import smtplib

smtp = {"sender": "",    # elasticemail.com verified sender
        "recipient": "", # elasticemail.com verified recipient
        "server": "in-v3.mailjet.com",      # elasticemail.com SMTP server
        "port": 587,                           # elasticemail.com SMTP port
       
   

# append all error messages to email and send
def sendEmail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")
import sys
import pathlib
import shutil
from datetime import datetime

def copyFileDirectory():
    """
    This Python code demonstrates the following features:
    
    * extracting the path component from a full file specification
    * copying a file
    * copying a directory.
    
    """
    try:
        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")  
        
      #  srcFile = "/home/ec2-user/environment/ICTPRGassdoc2/File1.txt"
      #  srcDir = "/home/ec2-user/environment/ICTPRGassdoc2/dir1"
        
        srcLoc = srcFile # change this srcLoc = srcDir to test copying a directory
        srcPath = pathlib.PurePath(srcLoc)
        
       # dstDir = "/home/ec2-user/environment/ICTPRGassdoc2/backups"
        dstLoc = dstDir + "/" + srcPath.name + "-" + dateTimeStamp
        
        print("Date time stamp is " + dateTimeStamp) 
        print("Source file is " + srcFile)
        print("Source directory is " + srcDir)
        print("Source location is " + srcLoc)
        print("Destination directory is " + dstDir)
        print("Destination location is " + dstLoc)
        
        if pathlib.Path(srcLoc).is_dir():
            shutil.copytree(srcLoc, dstLoc)
        else:
            shutil.copy2(srcLoc, dstLoc)
    except Exception as e:
        sendEmail(e)
        print("ERROR: An error occurred.")
    
#check job number
#!/usr/bin/python3

import sys
import logging
logging.basicConfig(filename="backup.log", level = logging.DEBUG)
loggerFile = logging.getLogger()

def main():
    """
    This Python code demonstrates the following features:
    
    * accessing command line arguments.
    
    """
    
    """arg1 below handles getting the job number if arg1 line 105 checks if the job number is correct the file is copied by copyFile directory then it print some text. the else handles the error log and sends an email 
    else = failure. """
    try:
        argCount = len(sys.argv)
        program = sys.argv[0]
        arg1 = sys.argv[1] #Getting job number. User provides job number
        
        print("The program name is " + program + ".")
        print("The number of command line items is " + str(argCount) + ".")
        print("Command line argument 2 is " + arg1 + ".")
        if arg1 == 'job1' or arg1 == 'job2' or arg1 == 'job3':  #Check if job number is correct
           copyFileDirectory() #copy the files by calling "copyFileDirectory() function
           #copy the file
           loggerFile.info("SUCCESS")
           print("coy the file")
        else: #If job number is incorrect

           #send email alert
           print("logging and sending email")
           sendEmail("Job number is incorrect") #send email - error message
           loggerFile.error("ERROR- FAIL: job number is incorrect.")

           #log the error and send email alert
    except Exception as e: #Catch the unexcepted error sends an email and logs the information prints on the terminal.
        sendEmail(f"Exception occurs {e}") #send email alert
        loggerFile.error("Exception occurs") #logging error
        print("ERROR: An error occured.")
    
if __name__ == "__main__":
    main()
    
#!/usr/bin/python3

