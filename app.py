from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
items = []
@app.route('/')
def checklist():
    return render_template('checklist.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['item']
    items.append(item)
    # flash('Item added')
    return redirect('/')

@app.route('/edit/<int:item:id', methods=['GET', 'POST'])
def edit_item(item_id):
    items = items[item_id]

    if request.method == 'POST':
        new_item = request.form['item']
        items[item_id - 1] = new_item
        return redirect('/')
    
    return render_template('edit.html', item=item, item_id=item_id)

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    del items[item_id - 1]
    return redirect('/')