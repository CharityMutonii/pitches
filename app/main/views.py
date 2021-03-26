from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch, Comment
from .forms import PitchForm, CommentForm
from .. import db
from flask_login import login_required, current_user
from datetime import datetime



@main.route('/')
def index():

    return render_template('index.html')

@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitch = PitchForm()
    if pitch.validate_on_submit():
        title = pitch.pitch_title.data
        pitch = pitch.pitch.data
        category = pitch.pitch_category.data

    
        new_pitch = Pitch(pitch_title=title, pitch_content=pitch,category=category, user=current_user, likes=0, dislikes=0)

       
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html', title=title, pitch_form=pitch)

@main.route('/pitches/interview_pitches')
def interview_pitches():

    pitches = Pitch.get_pitches('interview')
    return render_template("interview_pitches.html", pitches=pitches)

@main.route('/pitches/product_pitches')
def product_pitches():

    pitches = Pitch.get_pitches('product')
    return render_template("product_pitches.html", pitches=pitches)

@main.route('/pitches/pickup_pitches')
def pickup_pitches():

    pitches = Pitch.get_pitches('pickup')
    return render_template("pickup_pitches.html", pitches=pitches)

@main.route('/pitches/promotion_pitches')
def promotion_pitches():

    pitches = Pitch.get_pitches('promotion')
    return render_template("promotion_pitches.html", pitches=pitches)


@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.posted.strftime('%b %d, %Y')

    if request.args.get("like"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment=comment, user=current_user, pitch_id=pitch)

        new_comment.save_comment()

    comments = Comment.get_comments(pitch)

    return render_template("pitch.html", pitch=pitch, comment_form=comment_form, comments=comments, date=posted_date)
