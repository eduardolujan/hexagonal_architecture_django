import json
from dataclasses import dataclass, asdict
from uuid import UUID as UUID4

from modules.shared.domain.aggregate import AggregateRoot


class UUIDEncoder(json.JSONEncoder):
    """
    UUID Encoder
    """
    def default(self, obj):
        """
        Default encoder
        @param obj:
        @type obj:
        @return:
        @rtype:
        """
        if isinstance(obj, UUID4):
            return str(obj)

        return json.JSONEncoder.default(self, obj)


class Entity(AggregateRoot):
    """
    Entity
    """

    def as_str(self):
        """
        Entity as str
        """
        _dict = asdict(self)
        parsed_dict = json.dumps(_dict, cls=UUIDEncoder)
        return parsed_dict

    def as_dict(self):
        """
        Entity as dict
        """
        parsed_dict = json.loads(self.as_str())
        return parsed_dict

    def __repr__(self):
        return self.as_dict()
