#!python

import flask_wtf as w
import wtforms as f
import wtforms.validators as v
import wtforms.widgets

class CampaignForm(w.Form):
  search_key = f.StringField(
    'Search Key',
    validators=[
      v.InputRequired('Search Key is a required field')
    ],
  )

  latitude = f.FloatField(
    'Latitiude',
    validators=[
      v.Optional(),
      v.NumberRange(min=-180, max=180),
    ],
    id='latitude',
  )

  longitude = f.FloatField(
    'Longitude',
    validators=[
      v.Optional(),
      v.NumberRange(min=-180, max=180),
    ],
    id='longitude',
  )

  radius = f.FloatField(
    'Radius (mi)',
    validators = [
      v.Optional(),
      v.NumberRange(min=0),
      v.NoneOf([0,]),
    ],
    id='radius',
  )

  submit = f.SubmitField('Submit')
