from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch, Comment
from .forms import PitchForm, CommentForm
from .. import db, photos
from flask_login import login_required, current_user
from datetime import datetime



@main.route('/')
def index():

    return render_template('index.html')