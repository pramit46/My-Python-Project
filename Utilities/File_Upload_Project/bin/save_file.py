#!/usr/bin/python
#author: Pramit
#Purpose: Python File-Save module using flask

import os
import deprecation
import logging as logger
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

__version__ = "1.0"
#This needs to be dynamically populated, instead of hard coding. But not a priority right now
baseLocation= os.path.join('C:\\','Users','prambasu','Downloads','Personal Docs','python_projects','MyPython','File_Upload_Project')
uploadedFileLocation = os.path.join(baseLocation,'Storage')
logFileLocation=  os.path.join(baseLocation,'Logs')
templateLocation =  os.path.join(baseLocation,'templates')
    
app = Flask(__name__, template_folder=templateLocation)
app.config["DEBUG"] = True #This will also ensure auto reloading of the app in case of any changes done
logger.basicConfig(level=logger.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                   filename=os.path.join(logFileLocation,'save_file_program.log'),
                   filemode='a')
    

class SaveFile:

 
    @deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                        current_version=__version__,
                        details="This is just for the testing purpose and is not yet ready. Create the folder structure manually instead")
    def createLocations():
        if not os.path.exists(uploadedFileLocation):
            try:
                # By setting exist_ok as True 
                # error caused due already 
                # existing directory can be suppressed 
                # but other OSError may be raised 
                # due to other error like 
                # invalid path name 
                os.mkdirs(uploadedFileLocation, mode = 0o777, dir_fd = None, exist_ok = True)
            except OSError as error: 
                logger.debug("Path '%s' can not be created" % uploadedFileLocation)
                
        if not os.path.exists(logFileLocation):
            try:
                # By setting exist_ok as True 
                # error caused due already 
                # existing directory can be suppressed 
                # but other OSError may be raised 
                # due to other error like 
                # invalid path name 
                os.mkdirs(logFileLocation, mode = 0o777, dir_fd = None, exist_ok = True)
            except OSError as error: 
                logger.debug("Path '%s' can not be created" % logFileLocation) 
                
    #Path for landing page which is also the browse/upload page
    @app.route('/')
    def index():
        return render_template('fileUploadHomePage.html')
    
    #Route here in case of error
    @app.route('/error/<errorMessage>')
    def errorPage(errorMessage):
        finalString=("Content-Type: text/html\n<html><body><p>Some Error Occurred. Please Retry. %s </p></body></html>" % errorMessage)
        return finalString
    
    #Route here in case of success    
    @app.route('/success/<filename>')
    def successPage(filename):
        #Just acknowledge the successful upload
        finalString=("Content-Type: text/html\n<html><body><p>Upload of %s Successful</p></body></html>" % filename)
        return finalString

        #Show/download the content of the uploaded file
        #return send_from_directory(uploadedFileLocation,filename)

    #Intermediatary Path. It saves the file and also decide to route to the user to success or error page based on the end result.
    @app.route('/upload-result', methods=['GET', 'POST'])
    def uploadFile():
        '''execute whatever code you want when the button gets clicked here'''
        # Get filename here.
        #request.files=''
        message= ""
        fileName=""
        try:
            if(request.files and len(request.files)>0):
                fileitem = request.files['filename']
                # Test if the file was uploaded
                if fileitem.filename:
                    # strip leading path from file name to avoid
                    # directory traversal attacks
                    fileName = os.path.basename(fileitem.filename)
                    #fileName = os.path.basename(fileitem.filename.replace("\\", "/" )) #FOR UNIX
                    fileitem.save(os.path.join(uploadedFileLocation, fileName))
                    message = 'The file "' + fileName + '" was uploaded successfully'
                else:
                    message='No file was uploaded'
                    return redirect(url_for('errorPage'), message)
            else:
                return redirect(url_for('errorPage', errorMessage=message))
        except:
            return redirect(url_for('errorPage', errorMessage=message))
        
        return redirect(url_for('successPage', filename=fileName))

if __name__ == '__main__':
    app.run()