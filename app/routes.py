from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import List, Spell
from app.forms import ListForm, SpellForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # form = ListForm()
    # spells = db.session.query(Spell).all()
    # spell_list = [(i.spells, i.sname) for i in spells]
    form = SpellForm()
    if request.method == 'POST' and form.validate_on_submit():
        spell = Spell(
        sname=form.sname.data, slevel=form.slevel.data, verbal=form.verbal.data, somatic=form.somatic.data, material=form.material.data, concentration=form.concentration.data, ritual=form.ritual.data, description=form.description.data)
        db.session.add(spell)
        db.session.commit()
        return redirect(url_for('index'))
    spells = Spell.query.all()
    return render_template("home.html", title='Main', form=form, spells=spells)