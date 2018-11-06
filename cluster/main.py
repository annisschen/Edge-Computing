import urllib.request as urllib2
import time
import requests
while True:
    # url = "http://www.annisshong.xyz:3000/api/poll"
    # response = urllib2.urlopen(url).read().decode("utf-8")
    # response = response.split('/')[-1]
    response = "test.zip"
    print(response)
    if (response == "notask"):
        time.sleep(10)
    else:

        print ("downloading with requests")

        url = 'http://www.annisshong.xyz:3000/api/download/'+response
        print(url)
        import httplib2
        h = httplib2.Http()
        resp,content = h.request(url)

        if resp['status'] =='200':
            with open('./documents/'+response,'wb') as f:
                f.write(content)

        import zipfile

        z = zipfile.ZipFile('./documents/'+response,'r')
        z.extractall(path=r"./documents/")
        z.close()

        import os
        import sys

        path = sys.path
        doc_name = response.split('.')[0]
        download_file_path = os.listdir(path[0] + '/documents/' + doc_name)
        print(download_file_path)

        python_file_name = ''
        for item in download_file_path:
            if item.split('.')[1] == 'py':
                python_file_name = item
        print("python_file_name：")
        print(python_file_name)
        f = open('a.txt', 'w')
        A = []
        A.append('CD documents')
        A.append('CD ' + doc_name)
        A.append('python ' + python_file_name)
        print(A)

        for i in range(len(A)):
            f.write(A[i] + '\n')
        f.close()

        bat_filename = ''

        bat_file_path = os.listdir(path[0])
        print(bat_file_path)
        for item in bat_file_path:
            if item.split('.')[1] == 'txt':
                bat_filename = item.split('.')[0] + '.bat'
                os.rename(item, bat_filename)
                break

        import subprocess


        def bat_document(file_output):
            child = subprocess.Popen('a.bat', shell=False, stdout=file_output).wait()

        print(response.split('.')[0])
        file_output = open(response.split('.')[0]+'.txt', "w")

        bat_document(file_output)

        print("运行结束")
        os.remove(bat_filename)
        # 上传文件到服务器
        import requests
        files = {'result': open(response.split('.')[0]+'.txt', 'rb')}

        url = 'http://www.annisshong.xyz:3000/api/result'
        resp = requests.post(url, files=files)
        print(resp.text)


        time.sleep(30)