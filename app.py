from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('patients.db')

# Create table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten TEXT NOT NULL,
            can_nang INTEGER NOT NULL CHECK(can_nang BETWEEN 30 AND 90),
            chieu_cao REAL NOT NULL CHECK(chieu_cao BETWEEN 1.5 AND 1.9),
            nhom_mau TEXT CHECK(nhom_mau IN ('A', 'B', 'O')),
            gioi BOOLEAN NOT NULL,
            ngay_nhap_vien DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    conn.close()
    return render_template('index.html', patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        ten = request.form['ten']
        can_nang = request.form['can_nang']
        chieu_cao = request.form['chieu_cao']
        nhom_mau = request.form['nhom_mau']
        gioi = request.form['gioi']
        ngay_nhap_vien = request.form['ngay_nhap_vien']
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO patients (ten, can_nang, chieu_cao, nhom_mau, gioi, ngay_nhap_vien)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (ten, can_nang, chieu_cao, nhom_mau, gioi, ngay_nhap_vien))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients WHERE id = ?', (id,))
    patient = cursor.fetchone()
    conn.close()
    
    if request.method == 'POST':
        ten = request.form['ten']
        can_nang = request.form['can_nang']
        chieu_cao = request.form['chieu_cao']
        nhom_mau = request.form['nhom_mau']
        gioi = request.form['gioi']
        ngay_nhap_vien = request.form['ngay_nhap_vien']
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE patients
            SET ten = ?, can_nang = ?, chieu_cao = ?, nhom_mau = ?, gioi = ?, ngay_nhap_vien = ?
            WHERE id = ?
        ''', (ten, can_nang, chieu_cao, nhom_mau, gioi, ngay_nhap_vien, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('edit.html', patient=patient)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM patients WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    