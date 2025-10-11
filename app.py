from flask import Flask, render_template, request, redirect, flash,session,jsonify
import datetime
import infoitem

app = Flask(__name__)

@app.route('/')
def accueil():
    title="LootScope"
    current_year = datetime.datetime.now().year
    return render_template('accueil.html',title=title,annee=current_year)

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        item = request.form['item']
        x=infoitem.dropsearch(item)
        maxchance=infoitem.maxChance(x)
        trieChance = infoitem.trieChance(x)
        return render_template('search.html',ls=trieChance)
application = app

# Pour Vercel, on utilise app directement
if __name__ == '__main__':
    app.run(debug=True)
    