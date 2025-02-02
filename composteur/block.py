import hashlib
import json
from time import time
from django.core.serializers.json import DjangoJSONEncoder
from .models import *

class Blockchain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(
            block, sort_keys=True, cls=DjangoJSONEncoder).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def get_previous_block(self):
        return self.chain[-1]

    def add_transaction(self,id, greeneur,quantite,totale_point):
        self.current_transactions.append({
            'id':id,
            'greeneur': greeneur,
            'totale_point':totale_point,
            'quantite':quantite
        })
        transaction = TransactionCoins.objects.create(
            Identification=id,
            pseudo_G=greeneur,
            totale_point=totale_point,
            quantite=quantite
        )
        transaction.save()

    def mine_block(self):
        previous_block = self.get_previous_block
        previous_hash = self.hash(previous_block)
        block = self.create_block(previous_hash)
        return block

    def get_chain(self):
        chain = []
        for block in self.chain:
            chain.append({
                'index': block['index'],
                'timestamp': block['timestamp'],
                'transactions': block['transactions'],
                'previous_hash': block['previous_hash'],
            })
        return chain

