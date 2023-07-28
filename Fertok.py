import pathlib
from datetime import datetime
import mariadb  # type: ignore
from cryptography.fernet import Fernet  # type: ignore
from dateutil.relativedelta import relativedelta  # type: ignore

path = pathlib.Path().resolve()

#Open the Fernet Key you generated
with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
fernet = Fernet(key)

def connectDB():
    mydb = mariadb.connect(
    host = "localhost",
    user = "join-dev",
    password = "joindev",
    database = "join_dev"
    )
    return mydb

def disconnectDB(commit, mydb):
    if commit:
        mydb.commit()
    mydb.close()

def tokenGeneration(infoYouWantToEncrypt):
    token = fernet.encrypt(infoYouWantToEncrypt.encode('utf-8'))
    return str(token)

def tokenToDB(infoYouWantToEncypt):
    mydb = connectDB()
    cursor = mydb.cursor()  # type: ignore
    token = tokenGeneration(infoYouWantToEncypt)
    #Get the expiry date 3 months from now if you want days its relativedelta(days=+3)
    now = datetime.now()
    exp = (now + relativedelta(months=+3)).strftime("%Y/%m/%d")
    #Insert the token and expiry date into the database
    query = "INSERT INTO tokenStorage VALUES (" + "'" + token + "'" + "," + "'" + str(exp) + "'" + ")"
    cursor.execute(query)
    mydb.commit()  # type: ignore
    disconnectDB(True, mydb)
    return token

def tokenValidation(token,InfoYouEcrypted):
    mydb = connectDB()
    cursor = mydb.cursor()  # type: ignore
    query = "SELECT * FROM token_valid WHERE token =" + '"' + tok + '"'
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        return False
    else:
        exp = row[1]
        now = datetime.now()
        now = now.strftime("%Y/%m/%d")
        #Force date format from DB to be the same as now
        exp = exp.strftime("%Y/%m/%d")  # type: ignore 
        if (now > exp):  # type: ignore
            return False
        else:
            tokar = token.split("b'") #fernet token is in the format b'encryptedinfo' so you need to split it to get your info back
            tok = fernet.decrypt(tokar[1].encode('utf-8')).decode()
            if (InfoYouEcrypted == str(tok)):
                return True
            else:
                return False

def extractTokenEncryptedInfo(token):
    if authenticate(token):
        tokar = token.split("b'")
        decryptedinfo = fernet.decrypt(tokar[1].encode('utf-8')).decode()
        return decryptedinfo

def extractUsernameFromToken(token):
    if authenticate(token):
        #Using the encrypted info from the token, get the username from the database (I encrypted the Mail in my case)
        tokar = token.split("b'")
        decrypted = fernet.decrypt(tokar[1].encode('utf-8')).decode()
        mydb = connectDB()
        cursor = mydb.cursor() #type: ignore
        query =  'select username from users where EncryptedInfo = "' + decrypted + '"'
        cursor.execute(query)
        decryptedinfo = cursor.fetchone()[0]
        disconnectDB(False, mydb)
        return decryptedinfo

def authenticate(token):
    mydb = connectDB()
    cursor = mydb.cursor() #type: ignore
    query = 'SELECT * FROM tokenStorage WHERE token = "' + str(token) + '"'
    cursor.execute(query)
    for (tokens) in cursor:
        if (tokens[0] == token and (tokens[1] == datetime.now().date() or tokens[1] > datetime.now().date())):
            disconnectDB(False, mydb)
            return True
        else:
            disconnectDB(False, mydb)
            return False