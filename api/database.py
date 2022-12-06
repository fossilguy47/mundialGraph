from neo4j import GraphDatabase


class Database:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query):
        def do_cypher_tx(tx, cypher):
            result = tx.run(cypher)
            values = []
            for record in result:
                values.append(record.values())
            return values

        with self.driver.session() as session:
            return session.write_transaction(do_cypher_tx, query)


uri = "neo4j+s://da772eb2.databases.neo4j.io"
user = "neo4j"
password = "password"
db = Database(uri, user, password)


def execute(query):
    result = db.query(query)
    return result
