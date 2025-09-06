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
        qr_data = f"REG-NAME:{name}-REGNO:{regno}-EMAIL:{email}"
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
