class TeamMember:
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def display(self):
        print(f"TeamMembers : {self.name}, UID: {self.uid}")

class worker:
    def __init__(self,pay,jobtitle):
        self.pay=pay
        self.jobtitle=jobtitle

    def display(self):
        print("worker: {self.jobtitle},pay: {self.pay}")

class TeamLeader(TeamMember,worker):
    def __init__(self,name,uid,pay,jobtitle,exp):
        self.exp=exp
        TeamMember.__init__(self,name,uid)
        worker.__init__(self,pay,jobtitle)
    
    def display(self):
        TeamMember.display(self)