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

# Insert example data
def insert_example_data():
    example_data = [
        ('John Doe', 70, 1.75, 'O', True, '2023-01-01'),
        ('Jane Smith', 60, 1.65, 'A', False, '2023-02-01'),
        ('Alice Johnson', 55, 1.60, 'B', False, '2023-03-01'),
        ('Bob Brown', 80, 1.80, 'O', True, '2023-04-01'),
        ('Charlie Davis', 68, 1.70, 'A', True, '2023-05-01'),
        ('Diana Evans', 58, 1.68, 'B', False, '2023-06-01'),
        ('Eve Foster', 65, 1.72, 'O', False, '2023-07-01'),
        ('Frank Green', 75, 1.78, 'A', True, '2023-08-01'),
        ('Grace Harris', 62, 1.66, 'B', False, '2023-09-01'),
        ('Hank Irving', 85, 1.85, 'O', True, '2023-10-01'),
        ('Ivy Johnson', 59, 1.63, 'A', False, '2023-11-01'),
        ('Jack King', 77, 1.77, 'B', True, '2023-12-01')
    ]
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO patients (ten, can_nang, chieu_cao, nhom_mau, gioi, ngay_nhap_vien)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', example_data)
    conn.commit()
    conn.close()

create_table()
insert_example_data()

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients ORDER BY id DESC')
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