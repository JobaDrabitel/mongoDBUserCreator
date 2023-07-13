import json
import random
import string
from bson.objectid import ObjectId


def generate_referral_accounts(user_id, user_email, num_referrals):
    referrals = []
    password = 'c93cab31dea169dbef9b803525a5721627e5c62dc1ab24449167e74e75fd4948'
    base_id = str(ObjectId())
    base_user = generate_base_user(user_email, password, base_id)
    referrals.append(base_user)
    for i in range(num_referrals):
        random_email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@" + user_email.split('@')[1]
        first_ref_id = str(ObjectId())
        referral_account = generate_account(first_ref_id, i, random_email, password, base_id, 'consutant')
        referrals.append(referral_account)
        for i in range(num_referrals):
            random_email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@" + user_email.split('@')[1]
            second_ref_id = str(ObjectId())
            referral_account = generate_account(second_ref_id, i, random_email, password, first_ref_id, 'agent')
            referrals.append(referral_account)
            for i in range(num_referrals-1):
                random_email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@" + user_email.split('@')[1]
                third_ref_id = str(ObjectId())
                referral_account = generate_account(third_ref_id, i, random_email, password, second_ref_id, 'investor')
                referrals.append(referral_account)


    # Записываем объекты аккаунтов рефералов в JSON-файл
    with open('referral_accounts.json', 'w') as file:
        json.dump(referrals, file, indent=4)


def generate_account(id, i, email, password, ref_id, status):
   return {
        "_id": {"$oid": id},
        "registerDate": {"$date": "2023-07-13T09:41:27.258Z"},
        "userId": i + 2,
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


def generate_base_user(user_email, password, id):
    random_email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@" + user_email.split('@')[1]
    return generate_account(id, 0, user_email, password, None, 'seniorConsultant')
