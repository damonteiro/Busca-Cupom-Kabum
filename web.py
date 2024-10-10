from flask import Flask, render_template

import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    file_path = "TabelaPrecos.csv"
    
    df = pd.read_csv(file_path)
    df['Link'] = '<a href="'+ df['Link'] + '" target="_blank">'+df['Link'] + '</a>'
    table_html = df.to_html(classes='table table-striped', index=False, escape=False)
    
    

    return render_template('table.html', table_html=table_html)


if __name__ == "__main__":
    app.run(debug=True)