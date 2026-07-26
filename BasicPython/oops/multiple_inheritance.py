
class TeamMember:

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid


class Worker:

    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle
class TeamLeader(TeamMember,Worker):
    def __init__(self,name,uid,pay,jobtitle,exp):
        self.exp=exp
        TeamMember.__init__(self,name,uid)
        Worker.__init__(self,pay,jobtitle)
        print("name: {} ,pay : {} , exp :{}".format(self.name,self.pay,self.exp))

TL= TeamLeader("jake",10010,20203,"scrum master",5)