from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get(
    'MONGODB_URI', 'mongodb://localhost:27017/Mythril_Spellbook')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
sheets = db.sheets

app = Flask(__name__)


@app.route('/')
def index():
    """Display all Characters"""
    return render_template('index.html', msg='This page will show Character Sheets', sheets=sheets.find())


@app.route('/sheets', methods=['POST'])
def sheets_submit():
    """Submit a new Character."""
    sheet = {
        'name': request.form.get('name'),
        'race': request.form.get('race'),  # dropdown
        'class': request.form.get('class'),  # dropdown
        'sub_class': request.form.get('sub_class'),  # dropdown
        'level': request.form.get('level'),
        'alignment': request.form.get('alignment'),
        'background': request.form.get('background'),
        'static_prof': request.form.get('static_prof'),
        'prof_die': request.form.get('prof_die'),
        'courage': request.form.get('courage'),
        'inspiration': request.form.get('inspiration'),
        'strength': request.form.get('strength'),
        'dexterity': request.form.get('dexterity'),
        'constitution': request.form.get('constitution'),
        'intelligence': request.form.get('intelligence'),
        'wisdom': request.form.get('wisdom'),
        'charisma': request.form.get('charisma'),
        'armor_training': request.form.get('armor_training'),
        'combat_training': request.form.get('combat_training'),
        'weapon_prof': request.form.get('weapon_prof'),
        'armor_class': request.form.get('armor_class'),
        'max_hp': request.form.get('max_hp'),
        'hit_die_type': request.form.get('hit_die_type'),
        'max_hit_die': request.form.get('level'),
        'hit_die_remaining': request.form.get('hit_die_remaining'),
        'death_saves': request.form.get('death_saves'),
        'varient_points': request.form.get('varient_points'),
        'xp': request.form.get('xp'),
        'initative_bonus': request.form.get('initative_bonus'),
        'speed': request.form.get('speed'),
        'feats': request.form.get('feats'),
        'racial_traits': request.form.get('racial_traits'),
        'languages': request.form.get('languages'),
        'height': request.form.get('height'),
        'class_feats': request.form.get('class_feats'),
        'multiclass': request.form.get('multiclass'),  # toggle?
        # image upload vs url, maybe multiple images
        'appearance': request.form.get('appearance'),
        # small image/icon must be unique
        'symbol': request.form.get('symbol'),
        'backstory': request.form.get('backstory'),
        'friends': request.form.get('friends'),
        'family': request.form.get('family'),
        'foes': request.form.get('foes'),
        'personalty_traits': request.form.get('personality_traits'),
        'ideals': request.form.get('ideals'),
        'bonds': request.form.get('bonds'),
        'flaws': request.form.get('flaws'),
        'copper': request.form.get('copper'),  # int
        'silver': request.form.get('silver'),  # int
        'gold': request.form.get('gold'),  # int
        'platinum': request.form.get('platinum'),  # int
        'mythril': request.form.get('mythril'),  # int
        'backpack': request.form.get('backpack'),  # in bag
        # in a safe, unaccesible location
        'storage': request.form.get('storage'),
        # being worn/carried ...may affect stats
        'accessible': request.form.get('accessible'),
    }
    sheet_id = sheets.insert_one(sheet).inserted_id
    return redirect(url_for('sheets_show', sheet_id=sheet_id))


@app.route('/sheets/new')
def sheets_new():
    """Add new Character
    TODO: Lock this behind amin login after flask login set up """
    return render_template('sheets_new.html', sheet={}, title="New Character")


@app.route('/sheets/<sheet_id>')
def sheets_show(sheet_id):
    """Show an individual sheet."""
    sheet = sheets.find_one({'_id': ObjectId(sheet_id)})
    return render_template('sheets_show.html', sheet=sheet)


@app.route('/sheets/<sheet_id>/edit')
def sheets_edit(sheet_id):
    """Display edit form"""
    sheet = sheets.find_one({'_id': ObjectId(sheet_id)})
    return render_template('sheets_edit.html', sheet=sheet, title='Edit Character/Track Changes')


@app.route('/sheets/<sheet_id>', methods=['POST'])
def sheets_update(sheet_id):
    """Submit edited sheet"""
    updated_sheet = {
        'name': request.form.get('name'),
        'race': request.form.get('race'),  # dropdown
        'class': request.form.get('class'),  # dropdown
        'sub_class': request.form.get('sub_class'),  # dropdown
        'level': request.form.get('level'),
        'alignment': request.form.get('alignment'),
        'background': request.form.get('background'),
        'static_prof': request.form.get('static_prof'),
        'prof_die': request.form.get('prof_die'),
        'courage': request.form.get('courage'),
        'inspiration': request.form.get('inspiration'),
        'strength': request.form.get('strength'),
        'dexterity': request.form.get('dexterity'),
        'constitution': request.form.get('constitution'),
        'intelligence': request.form.get('intelligence'),
        'wisdom': request.form.get('wisdom'),
        'charisma': request.form.get('charisma'),
        'armor_training': request.form.get('armor_training'),
        'combat_training': request.form.get('combat_training'),
        'weapon_prof': request.form.get('weapon_prof'),
        'armor_class': request.form.get('armor_class'),
        'max_hp': request.form.get('max_hp'),
        'hit_die_type': request.form.get('hit_die_type'),
        'max_hit_die': request.form.get('level'),
        'hit_die_remaining': request.form.get('hit_die_remaining'),
        'death_saves': request.form.get('death_saves'),
        'varient_points': request.form.get('varient_points'),
        'xp': request.form.get('xp'),
        'initative_bonus': request.form.get('initative_bonus'),
        'speed': request.form.get('speed'),
        'feats': request.form.get('feats'),
        'racial_traits': request.form.get('racial_traits'),
        'languages': request.form.get('languages'),
        'height': request.form.get('height'),
        'class_feats': request.form.get('class_feats'),
        'multiclass': request.form.get('multiclass'),  # toggle?
        # image upload vs url, maybe multiple images
        'appearance': request.form.get('appearance'),
        # small image/icon must be unique
        'symbol': request.form.get('symbol'),
        'backstory': request.form.get('backstory'),
        'friends': request.form.get('friends'),
        'family': request.form.get('family'),
        'foes': request.form.get('foes'),
        'personalty_traits': request.form.get('personality_traits'),
        'ideals': request.form.get('ideals'),
        'bonds': request.form.get('bonds'),
        'flaws': request.form.get('flaws'),
        'copper': request.form.get('copper'),  # int
        'silver': request.form.get('silver'),  # int
        'gold': request.form.get('gold'),  # int
        'platinum': request.form.get('platinum'),  # int
        'mythril': request.form.get('mythril'),  # int
        'backpack': request.form.get('backpack'),  # in bag
        # in a safe, unaccesible location
        'storage': request.form.get('storage'),
        # being worn/carried ...may affect stats
        'accessible': request.form.get('accessible'),
    }
    sheets.update_one(
        {'_id': ObjectId(sheet_id)},
        {'$set': updated_sheet})
    return redirect(url_for('sheets_show', sheet_id=sheet_id))


@app.route('/sheets/<sheet_id>/delete', methods=['POST'])
def sheets_delete(sheet_id):
    """Delete Character."""
    sheets.delete_one({'_id': ObjectId(sheet_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
