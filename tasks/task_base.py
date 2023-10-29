from abc import (ABC, abstractmethod)


class TaskBase(ABC):

    @abstractmethod
    def execute(self):
        """
        this abstract method should return a string
        :return: string
        """
        pass
