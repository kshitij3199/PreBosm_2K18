from django.db import models


class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id
class QuestionBank(models.Model):
    question_no = models.IntegerField()
    question_title = models.CharField(max_length=255)
    question_text = models.CharField(max_length=255)
    question_answer = models.CharField(max_length=255)
    question_hint = models.CharField(max_length=255,blank=True,null=True)

    def q_no(self):
        return self.question_no

    def q_title(self):
        return self.question_title
    def q_text(self):
        return self.question_text

    def q_answer(self):
        return self.question_answer
    def q_hint(self):
        return self.question_hint
    def __str__(self):
        return  self.question_text +" -  "+  self.question_answer
