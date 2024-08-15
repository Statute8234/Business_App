"""
Could not find the documentation for this pysqlitecipher. According to github the link to the doc is: https://www.blog.letscodeofficial.com/@harshnative/encrypting-sqlite-database-in-python-using-pysqlitecipher-module-easy-and-secure-encryption-in-python-sqlite/
I will add the link in the description down bellow.
"""

from pysqlitecipher import sqlitewrapper
table_name = "BusinessUsers"
database = sqlitewrapper.SqliteCipher(dataBasePath="BusinessUsers.db", checkSameThread=False, password="Example_Password")
def create_table():
    global table_name, database
    database.createTable(table_name, [["ID", "INTEGER PRIMARY KEY AUTOINCREMENT"],['Business_Name','TEXT'],['Symbol_Emblem','TEXT'],['Email','TEXT'],['Password','TEXT']], makeSecure=False, commit=True)

def insert_user(Business_Name, Symbol_Emblem, Email, Password):
    global table_name, database
    data_row = [Business_Name, Symbol_Emblem, Email, Password]
    database.insertIntoTable(table_name, data_row, commit=True)

def get_user_id(Email):
    global table_name, database
    result = database.getDataFromTable(tableName=table_name, columns=["ID"], whereDict={"Email": Email}, omitID=True, extractAsList=True)
    if result:
        user_id = result[0][0]
        return user_id
    else:
        return None

def update_user(user_id, Business_Name = None, Symbol_Emblem = None, Email = None, Password = None):
    global table_name, database
    update_data = {}
    if Business_Name is not None:
        update_data['Business_Name'] = Business_Name
    if Symbol_Emblem is not None:
        update_data['Symbol_Emblem'] = Symbol_Emblem
    if Email is not None:
        update_data['Email'] = Email
    if Password is not None:
        update_data['Password'] = Password
    # update the row
    database.updateRecord(table_name=table_name, updateDict=update_data, whereDict={'ID': user_id}, commit=True)

def check_sign_up(Email):
    global table_name, database
    result = database.getDataFromTable(tableName=table_name, where={"Email": Email}, omitID=True, extractAsList=True, raiseConversionError=True)
    return len(result) > 0  # Returns True if user exists, False otherwise

def check_forgot_password(Business_Name, Symbol_Emblem, Email):
    global table_name, database
    result = database.getDataFromTable(tableName=table_name, columns=["ID"], Dict={"Business_Name": Business_Name, "Symbol_Emblem": Symbol_Emblem, "Email": Email}, omitID=True, extractAsList=True)
    return len(result) > 0  # Returns True if user exists, False otherwise

def check_login(Business_Name, Symbol_Emblem, Password):
    global table_name, database
    result = database.getDataFromTable(tableName=table_name, columns=["ID"], Dict={"Business_Name": Business_Name, "Symbol_Emblem": Symbol_Emblem, "Password": Password}, omitID=True, extractAsList=True)
    return len(result) > 0  # Returns True if login credentials are correct, False otherwise

if __name__ == "__main__":
    create_table()