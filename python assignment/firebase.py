
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

#python-demo-letsupgrade-18583-firebase-adminsdk-xz9la-0299c0489b (1)

cred = credentials.Certificate("python-demo-letsupgrade-18583-firebase-adminsdk-xz9la-0299c0489b (1).json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'users').document(u'abc')

doc_ref.set({
    u'first': u'jadhav',
    u'last': u'Gokle',
    u'born': 1997
})

def enterDataInDB():
    doc_ref = db.collection(u'LetsUpgradeUsers').document()
    
    name = input("Enter Name - ")
    lastName = input("Enter Last Name - ")
    age = int(input("Enter Age - "))
    
    dit = {}
    dit["firstName"] = name
    dit["lastName"] = lastName
    dit["age"] = age
    
    doc_ref.set(dit)

    enterDataInDB("sairam","shaikh",22)
    enterDataInDB("Yogen","patil",29)
    enterDataInDB("mangesh","Khade",23)
    enterDataInDB("kedar","khan",71)
    enterDataInDB("ravi","kulkarni",17)
    enterDataInDB("Tejas","ks",27)
    enterDataInDB()

    docs = db.collection(u'pyhton-demo-letsupgrade').stream()

for doc in docs:

    
    print("ID - ", doc.id)
    
    print("First Name - ", doc.to_dict().get("firstName"))
    print("Last Name - ", doc.to_dict().get("lastName"))
    print("Age - ", doc.to_dict().get("age") )
    
    print("---------------")
    print("---------------")

    def updateDatainFirebase(uid, updatedAge):
    doc_ref = db.collection(u'pyhton-demo-letsupgrade').document(uid)
    
    doc_ref.update({"age":updatedAge})

updateDatainFirebase("zslFTBzZl8BKFhSI4Yxw",26)

def deleteDataInFirebase(uid):
    db.collection(u'LetsUpgradeUsers').document(uid).delete()
    deleteDataInFirebase("0rg4glbfc8l7cuTbl2MD")
