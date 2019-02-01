class Game(object):
    def __init__(self):
        self.score=0
        self.throw_attempt = 0




    def throw(self, pins):
        if self.throw_attempt>=2:
            self.score += pins
            self.throw_attempt +=1


    def get_score(self):
        if self.throw_attempt== 1:
            return 0
        else:
         return self.score
