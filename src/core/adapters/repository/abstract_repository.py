""" Module core.adapters.repository.abstract_repository """
import abc


class AbstractRepository(abc.ABC):
    """ Abstract repository implementation """

    @abc.abstractmethod
    def add(self, item):
        """
        Method to add an item to the repository
        :param item: any
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, item_id: int):
        """
        Method to get an item by id
        :param item_id:
        :return: item
        """
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        """
        Method to get all items in the repository
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, item):
        """
        Method to update an item in the repository
        :param item:
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self):
        """
        Method to delete an item in the repository
        :return:
        """
        raise NotImplementedError
