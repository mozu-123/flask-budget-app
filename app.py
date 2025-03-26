from flask import Flask, render_template, request, redirect,url_for


app = Flask(__name__)
app.config["DEBUG"] = True

income_list=[]
outlay_list=[]
outlay_id = 1
income_id = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/income' ,methods=['GET' ,'POST'])
def income():
    global income_id

    if request.method == 'POST':

        if not request.form.get('number'):

            return redirect('/')

        else:    
            id = income_id 
            number = int(float(request.form.get('number')))
            category = request.form.get('category')
            date = request.form.get('date')
            memo = request.form.get('memo')

            income_list.append({

                'id':income_id,
                'amount':number,
                'category':category,
                'date':date,
                'memo':memo
            })

            income_id = income_id + 1 

            return redirect('/')
    
      #post = Post(income_amount=number,income_how=category,income_when=date,memo=memo)    
    else :

         return render_template('income.html')

@app.route('/outlay' , methods=['GET','POST'])
def outlay():

    global outlay_id

    if request.method == 'POST':
        if not request.form.get('number'):

            return redirect('/')
        else:
            id = outlay_id 
            number = int(request.form.get('number'))
            category = request.form.get('category')
            date = request.form.get('date')
            memo = request.form.get('memo')

            outlay_list.append({

                'id':outlay_id,
                'amount':number,
                'category':category,
                'date':date,
                'memo':memo
            })

            outlay_id = outlay_id + 1

            return redirect('/')

    else:
        return render_template('outlay.html')
@app.route('/result')
def result():
    
    return render_template('result.html')

@app.route('/income_result' ,methods=['GET','POST'])
def income_result():
   
    return render_template('income_result.html' , lists=income_list)

@app.route('/outlay_result', methods=['GET','POST'])
def outlay_result():
    
    return render_template('outlay_result.html',lists=outlay_list)

@app.route('/income_update/<int:id>' ,methods=['GET' ,'POST'])
def income_update(id): 

    global income_list

    if request.method == 'POST':

        number = request.form.get('number')
        category = request.form.get('category')
        date = request.form.get('date')
        memo = request.form.get('memo')

        for item in income_list:
           if item['id'] == id:
                item['date'] = date
                item['amount'] = number
                item['category'] = category
                item['memo'] = memo
                break

        return redirect(url_for('income_result'))

    else:
        number = None
        category = None
        date = None
        memo = None
        for item in income_list:
            if id == item['id']:
                number = int(float(item['amount']))
                category = item['category']
                date = item['date']
                memo = item['memo']
                break  
        return render_template('income_update.html',
                               number=number,
                               date = date,
                               memo = memo
                               )
              #post = Post(income_amount=number,income_how=category,income_when=date,memo=memo) 

@app.route('/outlay_update/<int:id>' ,methods=['GET' ,'POST'])
def outlay_update(id): 

    global outlay_list

    if request.method == 'POST':

        number = request.form.get('number')
        category = request.form.get('category')
        date = request.form.get('date')
        memo = request.form.get('memo')

        for item in outlay_list:
           if item['id'] == id:
                item['date'] = date
                item['amount'] = number
                item['category'] = category
                item['memo'] = memo
                break

        return redirect(url_for('outlay_result'))

    else:
        number = None
        category = None
        date = None
        memo = None
        for item in outlay_list:
            if id == item['id']:
                number = int(float(item['amount']))
                category = item['category']
                date = item['date']
                memo = item['memo']
                break  
        return render_template('outlay_update.html',
                               number=number,
                               date = date,
                               memo = memo
                               )               
                 

@app.route('/income_delete/<int:id>' ,methods=['GET'])
def income_delete(id): 

    global income_list

    income_list = [item for item in income_list if item['id'] != id]

    return redirect('/income_result')

@app.route('/outlay_delete/<int:id>' ,methods=['GET'])
def outlay_delete(id): 

    global outlay_list

    outlay_list = [item for item in outlay_list if item['id'] != id]
    
    return redirect('/outlay_result')
 

