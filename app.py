from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('stations.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    keyword = request.args.get('keyword', '').strip()
    results = df[df['StationName'].str.contains(keyword, case=False, na=False)]
    data = results[['StationName', 'Address']].to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
