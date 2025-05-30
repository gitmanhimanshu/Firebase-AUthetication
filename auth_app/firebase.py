import pyrebase
from decouple import config
import firebase_admin
from firebase_admin import credentials, auth as admin_auth
import os

# Firebase client config
firebase_config = {
    "apiKey": "AIzaSyAFASl35TNFmhkO-MgyNmmSBi6FoHErdDo",
    "authDomain": "dyzotest.firebaseapp.com",
    "projectId": "dyzotest",
    "storageBucket": "dyzotest.firebasestorage.app",
    "messagingSenderId": "621614076429",
    "appId": "1:621614076429:web:8ba77611fd824ec669bb44",
    "measurementId": "G-3M2C47VW9E",
    "databaseURL": "https://dyzotest-default-rtdb.firebaseio.com"
}

# Initialize Firebase client
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Initialize Firebase Admin SDK
# Make sure to place your service account key JSON file in a secure location
# and update the path accordingly
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "dyzotest",
  "private_key_id": "fbd945a738fe4cb040a74c401dd83d1df4324c45",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDv/4UzZ41UGsQm\nettQz9TzWtcT6DREuPG2HkY5WHqnpZ80Nuu4m73RZ3rOg2VP262pCusjW2CZrQbz\njnz4d2d3UQgDIpNMz1ZPRiqa14yxlRCUAGx/SCaJMgw2c9JkQnrOwzhw3ESwA4dI\noJ0pCT1fAthgZgxHR4PmOcCRO8BFiW1PTkSLjS3UEfMBfJ/PiIrGtN5f40xwJgO0\nggTZvNSW8fBhVhQxUEhEI78+1m5wIAw/+bFfxYvMEhYdgq9XeFxRdk5pm5bdjfVN\nvugKbhe/H0ITgeh8IXX9rMiM+C8MZwV4Y8oEnfwBK5M8DfoZ1frtmHcOY59tZlCR\n2xWCqFgfAgMBAAECggEAZvy0USG/oPa3c3fHAz+cNy2lG9LKEy918du98L/KKoTE\n86gZsSeL5f9M0K/L2t/+/opD6vE8W9XHJN7hO9IpYScxk/7TTOOwOuZ2Q+n5Yv7/\nlTM1W80/VCJY4UkEYKeygWV+o9ex1gI9nGnn5wMjBdF3vq4r2K6UqEfiHbCRSoTg\nw951pqn6poDZX7PL1a04jb+7kQvkPY9K8M3ADobIpi8C1DkdnlECnfE15VKBP84O\nxzOu1w+o3YevpRz9AjPMCmY0A/+C/5iyX+KgDY4PicQQruJ5kOSN4YFXELyY7ROk\n2tRxyVB/iIkm1gfkw02cA0720nWJNopoElw2JZOFIQKBgQD/JSLS1cmwzVR52qQ1\nmVU4eyNJdufNqcJM0HWlTgTuHjpqsiWX9mV+8I3fE7ajEUHug8IinhCp7d0mQSI+\nOG4cuHJ3fqIAjVeZBHp7qhH7BJ3N1GDkcYguMOCecdb9WYXRKf40bsrCT9QmdkbT\nizBQrlDRLBF36ClEw40/IiN57wKBgQDwzWQme5cujiG0wJdeuDdcbU0iY462m5w6\nxbYWoRflxVtmqzGY5nbOsENqC3X0/G9+JoQhbvv3n0O36pucAyHlPagIhtRY7C8G\nGqIep4sQYKVQt/MtwapcCP4m+VDJeU7XBAYNni3PNQIeVzCLpuJ6eeAQs8+j8mdO\nH1XQ5ib00QKBgQCUVyv69q8v6wFdY2ArhX2FvBoVAVveN/+ul1h/BnBZXRvLos22\nn1v9RLDHbPe3sTXrDZHWfJ3lnlUAg8f78uUaL6blkKtxtLukTHVF5uhTUCjLXdoD\nl3p8mJBPrpI3dFAX/tk79NpPxQfsYMHnBjrN/bshEgUJ+OHdh/BcL2X+4wKBgQCZ\nZAye4u2L72gTLvd9k9VYIBwZgte/BOMBIT57rcR+TjiJ7xVZ87zMrsVSwNgz5bXT\n4w8aCQuiUiad+mmDeQ9Xau4l+FU+C71sovyQkGNqXFYSVAspI4u0stnK09gdbxPE\nrcB5XkCKFJcz4pB+9SChqg8MNK5ZHimmPxm4R1ObcQKBgDNIWPUpr7rLrVE8dZVt\n2uuOh1Xr2e96rxmcQVW4UE1klpACcSH7jwhjzr+b/ECfyL+zTTc531t+6ERN1NA3\nYrDsP9nHjZgqCVpu+6ZbLr/kLfZJ+vxjETEb9pSbZopq4d7Hmhct4ov2nvnQg+B9\nSxfQqAPDMtlm7L2sYuCvKv5M\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@dyzotest.iam.gserviceaccount.com",
  "client_id": "106508900756861309164",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40dyzotest.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})
firebase_admin.initialize_app(cred)