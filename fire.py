from urllib import request
from firebase import firebase
f = open('C:\\Users\\PIYUSH\\Desktop\\04.jpg', 'wb')
firebase=firebase.FirebaseApplication("https://ambulance-85238.firebaseio.com/")
res=firebase.get("/samosa",None)
#print(res)
f.write(request.urlopen(res).read())
f.close()
