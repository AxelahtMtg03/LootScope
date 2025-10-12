from flask import Flask, render_template, request, redirect, flash,session,jsonify
import datetime
import infoitem

app = Flask(__name__)
title="LootScope"

@app.route('/')
def accueil():
    current_year = datetime.datetime.now().year
    return render_template('accueil.html',title=title,annee=current_year)

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        item = request.form['item']
        x=infoitem.dropsearch(item)
        maxchance=infoitem.maxChance(x)
        trieChance = infoitem.trieChance(x)
        for elem in trieChance:
            elem["image"] = infoitem.get_place_image(elem["place"])
        return render_template('search.html',title=title,ls=trieChance)


# Pour Vercel, on utilise app directement
if __name__ == '__main__':
    app.run(debug=True)
    