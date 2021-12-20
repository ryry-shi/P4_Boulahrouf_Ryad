import json
from tinydb import TinyDB
from tinydb.table import Document


class Manager:
    """La classe Manager sert a charger,créer les tournois et player.
    elle factorise aussi les fonction commune"""

    def __init__(self, item_type: type):
        """Constructeur de la classe Manager"""
        self.collection = {}
        self.item_type = item_type
        self.max_id = 0
        db = TinyDB("db.json", sort_keys=True, indent=4)
        self.table = db.table(item_type.__name__.lower() + "s")
        for data in self.table:
            self.create(**data)

    def load_file(self, path):
        """
            Méthode pour charger a partir d'un fichier json des variable
            et ensuite créer une classe
        """
        with open(path) as f:
            for data in json.load(f):
                self.create(**data)

    def create(self, **params):
        """Créations d'une classe on passont par leur id"""
        if "id" not in params:
            params["id"] = self.max_id + 1
        item = self.item_type(**params)
        self.collection[item.id] = item
        self.max_id = max(self.max_id, item.id)
        return item

    def find_all(self):
        """
            Méthode pour récupérer toute les variables
            d'une classe en les désérialisons
        """
        return list(self.collection.values())

    def find_by_id(self, id):
        """Méthode pour trouver un tournois ou un player en particulier """
        return self.collection[id]

    def insert_item(self, id):
        item = self.find_by_id(id)
        self.table.upsert(Document(item.serialize(), doc_id=id))
