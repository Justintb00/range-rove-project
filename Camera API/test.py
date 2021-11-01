import requests

for i in requests.get('http://localhost:3005/video'):
    print("Image {image}", image=i)

print('finish')