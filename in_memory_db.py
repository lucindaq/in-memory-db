class InMemoryDB:
    def __init__(self):
        # Main DB
        self.db = {}
        self.transaction = None

    def get(self, key):
        if self.transaction is not None and key in self.transaction:
            return self.transaction[key]
        return self.db.get(key, None)

    def put(self, key, val):
        if self.transaction is None:
            raise Exception("No active transaction. Please start a transaction first.")
        self.transaction[key] = val

    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("Transaction already in progress")
        self.transaction = {}

    def commit(self):
        if self.transaction is None:
            raise Exception("No active transaction to commit")
        # Commit all changes from transaction to main DB
        self.db.update(self.transaction)
        self.transaction = None

    def rollback(self):
        if self.transaction is None:
            raise Exception("No active transaction to rollback")
        self.transaction = None


# Testing
if __name__ == "__main__":
    inmemoryDB = InMemoryDB()

    print(inmemoryDB.get("A"))  # Expect: None
    try:
        inmemoryDB.put("A", 5)  # Expect: error
    except Exception as e:
        print(e)

    inmemoryDB.begin_transaction()
    inmemoryDB.put("A", 5)
    print(inmemoryDB.get("A"))  # Expect: 5
    inmemoryDB.put("A", 6)
    inmemoryDB.commit()
    print(inmemoryDB.get("A"))  # Expect: 6

    try:
        inmemoryDB.commit()  # Expect: error
    except Exception as e:
        print(e)

    try:
        inmemoryDB.rollback()  # Expect: error
    except Exception as e:
        print(e)

    print(inmemoryDB.get("B"))  # Expect: None
    inmemoryDB.begin_transaction()
    inmemoryDB.put("B", 10)
    inmemoryDB.rollback()
    print(inmemoryDB.get("B"))  # Expect: None
