from flask import Flask, render_template, request #bir kutucuk varsa oranin icinde ki degeri cekmek icin request kullaniriz

app = Flask(__name__)#obje olusturuyoruz

def convert(decimal_num): #girilensayiyi romen sayisina cevrilen yer
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    num_to_roman = ''

    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i) 
        decimal_num %= i
    return num_to_roman


@app.route('/', methods=['POST', 'GET'])
def main_post():
    if request.method == 'POST': #eger method post ise girilen sayiyi cek
        alpha = request.form['number']
        if not alpha.isdecimal():
            return render_template('index.html', developer_name='Mine', not_valid=True)
        number = int(alpha)#alpha integerini number a atamis.
        if not 0 < number < 4000: #alpha da 0-4000 arasi olacak. romen sayilarinin kurali
            return render_template('index.html', developer_name='Mine', not_valid=True)#eger verilen aralik da degilse hata msji cikar.
        return render_template('result.html', number_decimal = number , number_roman= convert(number), developer_name='Mine') 
    else:
        return render_template('index.html', developer_name='Mine', not_valid=False)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
