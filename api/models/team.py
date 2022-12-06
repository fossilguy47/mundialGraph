from api.database import execute


class Team:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def index():
        result = execute("MATCH (a:Team) RETURN a")
        return result

    def exists(self):
        result = execute("MATCH (a:Team {name: '%s'}) RETURN a" % self.name)
        return len(result) > 0

    def add(self):
        if self.exists():
            return False
        else:
            execute("CREATE (a:Team {name: '%s'}) RETURN a" % self.name)
            return True

    def delete(self):
        if self.exists():
            execute("MATCH (a:Team {name: '%s'}) DETACH DELETE a" % self.name)
            return True
        else:
            return False

    

    def duel(self, team, duel_result):
        if self.exists() and team.exists():
            return execute(
                "MATCH (a:Team {name: '%s'}), (p:Team {name:'%s'}) MERGE(a)<-[d:DUEL {duel_result: '%s' }]->(p) RETURN a,p" % ( 
                    self.name,  team.name,self.name[:3].upper() +" " + duel_result +" "+ team.name[:3].upper()))
        else:
            return False


    def duel_info(self):
        if self.exists():
            return execute("OPTIONAL MATCH (a:Team {name:'%s'})-[r:DUEL]-(p:Team) RETURN a, r, p" % self.name)
        else:
            return False
