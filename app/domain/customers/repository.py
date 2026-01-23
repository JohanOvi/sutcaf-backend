from abc import ABC, abstractmethod

class CustomerRepository(ABC):

    @abstractmethod
    def create(self, db, customer):
        pass

    @abstractmethod
    def get_all(self, db):
        pass

    @abstractmethod
    def get_by_id(self, db, customer_id: int):
        pass

    @abstractmethod
    def update(self, db, customer):
        pass

    @abstractmethod
    def delete(self, db, customer):
        pass
