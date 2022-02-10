import json


class DB:
    def __init__(self, dbfile: object = "db.json") -> object:
        self.dbfile = dbfile

    def get_db(self):
        with open(self.dbfile, encoding="UTF-8") as f:
            db = json.load(f)
        return db

    def write_db(self,db):
        with open(self.dbfile,"w", encoding="UTF-8") as f:
            json.dump(db,f,indent = 4)

    def get_all_ids(self):
        db = self.get_db()
        return list(db.keys())

    def get_all_items(self):
        item_list = []
        db = self.get_db()
        for i in db.keys():
            item_list.append(db[i])
        return item_list

    def add_item_db(self, data):
        self.write_db(data)