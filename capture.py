import cv2
import dropbox
import time
import random 

start_time = time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        start_time=time.time
        result=False
    return imageName
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token="sl.BHx2HWUwHGonawtIXfdyRA9pepu2guCXAI6hueexMCKrF-gEZb6SxRCEgMKZ185Azegtx4nEXf93nFFS-40hpizrbJf8162B0cdCrU-dsaHQlj2sTiy72xXwrPciOPicu1k0kNS6uhLD"
    file=imageName
    file_from=file
    file_to="/folder/"+(imageName)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()