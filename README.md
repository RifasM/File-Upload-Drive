# File Uploader for Google Drive
This python script can be used to upload a file to the users google drive via the google drive API.

-----

# Requirements:
- Pydrive
- Python 3.x.x
- Google Drive API

----

- Download and store file, "clent-secrets.json" in the working directory.
- Add client secret and client id in the settings.yaml file for successive authenticated logins

----

# Run
- python upload.py
    - To upload to Root directory of Google Drive
- python UploadtoFolder.py
    - To upload to a folder "Folder" in Google Drive


----
Authenticate the first time, may show a unauthorised warning, click advanced and proceed.
