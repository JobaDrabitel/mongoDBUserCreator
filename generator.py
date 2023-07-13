import json
import random
import string
import pymongo
from bson.objectid import ObjectId
import datetime

def generate_referral_accounts( user_email, num_referrals):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["main"]
    collection = db["test"]
    cursor = collection.find().sort('_id', -1).limit(1)
    for document in cursor:
        user_id = document["userId"]

    referrals = []
    password = 'c93cab31dea169dbef9b803525a5721627e5c62dc1ab24449167e74e75fd4948'
    result = collection.find_one({"email": user_email})
    base_id = result["_id"]
    iter = 0
    for i in range(num_referrals):
        iter+=1;
        random_email = user_email.split('@')[0] + str(iter) + "@" + user_email.split('@')[1]
        first_ref_id = ObjectId()
        referral_account = generate_account(first_ref_id, iter, random_email, password, base_id, 'consutant', user_id)
        collection.insert_one(referral_account)
        for k in range(num_referrals):
            iter += 1;
            random_email = user_email.split('@')[0] + str(iter) + "@" + user_email.split('@')[1]
            second_ref_id = str(ObjectId())
            referral_account = generate_account(second_ref_id, iter, random_email, password, first_ref_id, 'agent', user_id)
            referrals.append(referral_account)
            collection.insert_one(referral_account)
            print(iter)
            for j in range(num_referrals-1):
                iter += 1;
                random_email = user_email.split('@')[0] + str(iter) + "@" + user_email.split('@')[1]
                third_ref_id = str(ObjectId())
                referral_account = generate_account(third_ref_id, iter, random_email, password, second_ref_id, 'investor', user_id)
                referrals.append(referral_account)
                collection.insert_one(referral_account)
                print(iter)
    client.close()


def generate_account(id, i, email, password, ref_id, status, userid):
   return {
        "_id": ObjectId(id),
        "registerDate": datetime.datetime.now(),
        "userId": userid+i,
        "admin": False,
        "avatar": None,
        "email": email,
        "password": password,
        "balance": 0,
        "pendingBalance": 0,
        "withdrawal": 0,
        "deposit": 0,
        "myTurnover": 0,
        "turnover": 0,
        "firstName": f'{email.split("@")[0]}{random.randint(100, 999)}',
        "middleName": None,
        "lastName": None,
        "telegram": None,
        "phone": "+79111111111",
        "ref": {"$oid": ref_id},
        "refProfit": 0,
        "nonce": 0,
        "wallet": None,
        "walletInKey": "1",
        "walletIn": "1",
        "recoveryCode": 0,
        "recoveryTries": 0,
        "recoveryTime": 0,
        "country": None,
        "passportNum": None,
        "passportBirthDate": None,
        "gender": None,
        "passportIssuedBy": None,
        "passportIssueDate": None,
        "passportCode": None,
        "passportAddress": None,
        "passportPhoto1": None,
        "passportPhoto2": None,
        "passportPhoto3": None,
        "verified": None,
        "referrals": 0,
        "refInvestor": 0,
        "refAgent": 0,
        "refConsultant": 0,
        "refSeniorConsultant": 0,
        "refManager": 0,
        "refSeniorManager": 0,
        "refTopManager": 0,
        "refVicePresident": 0,
        "status": status,
        "__v": 0
    }


