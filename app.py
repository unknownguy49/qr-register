from flask import Flask, render_template, request
import qrcode
import io
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        regno = request.form['regno']
        email = request.form['email']
        error = None
        import re
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not re.match(email_pattern, email):
            error = "Invalid email address."
        elif len(regno) > 10:
            error = "Registration number must not exceed 10 characters."
        elif len(name) > 40:
            error = "Name must not exceed 40 characters."
        if error:
            return render_template('register.html', error=error, name=name, regno=regno, email=email)
        qr_data = f"REG-NAME: {name}\nREGNO: {regno}\nEMAIL: {email}"
        img = qrcode.make(qr_data)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        import base64
        qr_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        return render_template('qr.html', qr_base64=qr_base64, name=name, regno=regno, email=email)
    return render_template('register.html')



if __name__ == '__main__':
    app.run()
