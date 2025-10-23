class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """
        data: dictionary containing vote info e.g. {'voter_hash':..., 'candidate':..., 'constituency':...}
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_data = {'note': 'genesis'}
        genesis_block = Block(0, str(datetime.now(timezone.utc)), genesis_data, '0')
        self.chain.append(genesis_block)

    def latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_index = self.latest_block().index + 1
        new_block = Block(new_index, str(datetime.now(timezone.utc)), data, self.latest_block().hash)
        if new_block.previous_hash != self.latest_block().hash:
            raise Exception("Previous hash mismatch")
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            cur = self.chain[i]
            prev = self.chain[i-1]
            if cur.previous_hash != prev.hash:
                return False, f"Broken link at index {i}"
            if cur.hash != cur.compute_hash():
                return False, f"Invalid hash at index {i}"
        return True, "Chain is valid"
