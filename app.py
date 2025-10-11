from flask import Flask, render_template, request, redirect, flash,session,jsonify
import datetime
import requests
import infoitem

app = Flask(__name__)
URLDROP = "https://api.warframestat.us/drops/"
URLINFO = "https://api.warframestat.us/items/"
@app.route('/')
def accueil():
    title="LootScope"
    current_year = datetime.datetime.now().year
    return render_template('index.html',title=title,annee=current_year)

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        item = request.form['item']
        x=infoitem.dropsearch(item)
        maxchance=infoitem.maxChance(x)
        trieChance = infoitem.trieChance(x)
        return render_template('search.html',ls=trieChance,max=maxchance)

# Pour Vercel, on utilise app directement
# if __name__ == '__main__':
#     app.run(debug=True)
    