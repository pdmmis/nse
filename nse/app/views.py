from django.shortcuts import render
import requests
import zipfile
from datetime import datetime
# Create your views here.
# currentdate = datetime.date(1869, 10, 2)
# formatDate = currentdate.strftime("%d/%B/%Y")   
def show(request):
    print(type(str(datetime.now())))
    y=str(datetime.now())[:4]
    d=str(datetime.now())[8:10]
    url="https://www1.nseindia.com/content/historical/EQUITIES/2023/FEB/cm"+d+"FEB2023bhav.csv.zip"
    r=requests.get(url, stream=True)
    path='cm'+d+'FEB2023bhav.csv.zip'
    with open(path,'wb') as file:
        for chunk in r.iter_content(chunk_size=1024):
            file.write(chunk)
    
    with zipfile.ZipFile(path,'r') as c_file:
        c_file.extractall("")
    return render(request,'index.html')
