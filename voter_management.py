class VoterRegistry:
    def __init__(self):
        # stores hashed_id => {'registered':bool, 'voted':bool}
        self.registry = {}

    def register(self, voter_id):
        hashed = hashlib.sha256(voter_id.encode()).hexdigest()
        if hashed in self.registry:
            return hashed
        self.registry[hashed] = {'registered': True, 'voted': False, 'voter_id': voter_id}
        return hashed

    def is_registered(self, hashed_id):
        return hashed_id in self.registry and self.registry[hashed_id]['registered']

    def has_voted(self, hashed_id):
        return self.registry.get(hashed_id, {}).get('voted', False)

    def mark_voted(self, hashed_id):
        if hashed_id in self.registry:
            self.registry[hashed_id]['voted'] = True
            return True
        return False
