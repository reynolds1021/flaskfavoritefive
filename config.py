import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows = Documents\codingtemple-sept2020\week5\day1\intro_to_flask\
# Mac = Mac = Documents/codingtemple-sept2020/week5/day1/introtoflask/

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess...'