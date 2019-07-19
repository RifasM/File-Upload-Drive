from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

#Name of the folder where I'd like to upload the files
upload_folder = "Folder"
#Id of the folder where I'd like to upload files
upload_folder_id = None

#Check if folder exists. If not then create one with the given name
#List the files and folders in the root folder
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file_folder in file_list:
    if file_folder['title'] == upload_folder:
        #Get the matching folder id
        upload_folder_id = file_folder['id']
        print('File will be uploaded to EXISTING folder: ' + file_folder['title'])
        #We need to break out of this if it's done
        break
    else:
        #If there is no existing folder, create a new one
        file_new_folder = drive.CreateFile({'title': 'Folder',
            "mimeType": "application/vnd.google-apps.folder"})
        file_new_folder.Upload() #Upload the folder to the drive
        print('New folder created: ' + file_new_folder['title'])
        upload_folder_id = file_new_folder['id'] #Get the folder id
        print('File will be uploaded to the NEW folder: ' + file_new_folder['title'])
        break #We need to break out of this if it's done

#Create new file in the_folder
file1 = drive.CreateFile({"parents":  [{"kind": "drive#fileLink","id": upload_folder_id}],'title':"Hello.txt"})

file1.SetContentString('Hello')
file1.Upload() # Files.insert()

file1['title'] = 'HelloWorld.txt'  # Change title of the file
file1.Upload() # Files.patch()

content = file1.GetContentString()  # 'Hello'
file1.SetContentString(content+' World!')  # 'Hello World!'
file1.Upload() # Files.update()

print("Uploaded file '%s' to Folder" %file1['title'])
"""
file2 = drive.CreateFile()
file2.SetContentFile('hello.png')
file2.Upload()
print('Created file %s with mimeType %s' % (file2['title'],
file2['mimeType']))
# Created file hello.png with mimeType image/png

file3 = drive.CreateFile({'id': file2['id']})
print('Downloading file %s from Google Drive' % file3['title']) # 'hello.png'
file3.GetContentFile('world.png')  # Save Drive file as a local file

# or download Google Docs files in an export format provided.
# downloading a docs document as an html file:
#docsfile.GetContentFile('test.html', mimetype='text/html')"""
