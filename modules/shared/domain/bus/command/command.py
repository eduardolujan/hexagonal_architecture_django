

from abc import ABC, abstractmethod
from json import dumps, loads, JSONEncoder


class CommandFieldParser:
    """
    Command Field Parser
    """

    def parse_key(self, key):
        index = key.index('__')
        if index <= 0:
            return key
        return key[index + 2:]


class CommandJsonEncoder(JSONEncoder):
    """
    Command JSON Encoder
    """

    command_field_parser = CommandFieldParser()

    def default(self, _object):
        """

        @param _object:
        @type _object:
        @return:
        @rtype:
        """
        return {self.command_field_parser.parse_key(k): v for k, v in vars(_object).items()}


class CommandUtils:
    """
    CommandUtils
    """

    def get_as_json(self):
        """
        Get command as json
        """
        return dumps(self, indent=4, cls=CommandJsonEncoder)

    def get_as_dict(self):
        """
        Get command as dict
        """
        return {self.beautify_key(k): v for k, v in vars(self).items()}


class Command(ABC):
    """
    Command Port Interface
    """
