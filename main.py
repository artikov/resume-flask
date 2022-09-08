from flask import Flask, render_template
from data import MY_DATA

app = Flask(__name__)


@app.route('/')
def index():
    address = MY_DATA['address']
    name = MY_DATA['name']
    email = MY_DATA['email']
    phone = MY_DATA['phone']
    info = MY_DATA['info']
    socials = MY_DATA['socials']
    experience = MY_DATA['experience']
    education = MY_DATA['education']
    interests = MY_DATA['interests']
    certificates = MY_DATA['certificates']
    return render_template('index.html',
                           my_address=address,
                           my_name=name,
                           my_email=email,
                           my_phone=phone,
                           my_info=info,
                           linkedin=socials['linkedin'],
                           github=socials['github'],
                           twitter=socials['twitter'],
                           facebook=socials['facebook'],
                           experience=experience,
                           education=education,
                           interests=interests,
                           certificates=certificates)


if __name__ == '__main__':
    app.run(debug=True)