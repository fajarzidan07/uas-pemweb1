from flask import Flask,render_template, request, redirect, url_for, flash
from DB_Operations import fetch_all_items, insert_item, fetch_item_by_id, update_item, delete_item 

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    items = fetch_all_items() #Perintah untuk menampilkan data dari database
    return render_template('index.html',items=items)

@app.route('/add_item', methods=["POST","GET"])
def add_item():
    if request.method == 'POST':
        nama_paket = request.form['nama_paket']
        fasilitas = request.form['fasilitas']
        harga = request.form['harga']
        #insert item to db
        insert_item(nama_paket,fasilitas,harga)
        flash('Item Added Succesfully!')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=["GET","POST"])
def edit_item(id):
    item = fetch_item_by_id(id)
    if not item:
        flash("Item not found!")
        return redirect(url_for('index'))
    if request.method == 'POST':
        nama_paket = request.form['nama_paket']
        fasilitas = request.form['fasilitas']
        harga = request.form['harga']
        #update item
        update_item(id,nama_paket,fasilitas,harga)
        flash('Item Updated Succesfully!')
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<id>', methods=["GET","POST"])
def delete_item_route(id):
    delete_item(id)
    flash('Item Deleted Succesfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()