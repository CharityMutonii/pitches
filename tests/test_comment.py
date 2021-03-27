from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Preston = User(username = 'charity',password = 'chch', email = 'charity0@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_comment='This is a test pitch',category="product",user = self.user_charity,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_charity,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_Preston)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
