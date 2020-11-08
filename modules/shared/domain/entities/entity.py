import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from uuid import UUID as UUID4

from modules.shared.domain.aggregate import AggregateRoot


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID4):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class Entity(AggregateRoot, ABC):
    def as_str(self):
        _dict = asdict(self)
        parsed_dict = json.dumps(_dict, cls=UUIDEncoder)
        return parsed_dict

    def as_dict(self):
        parsed_dict = json.loads(self.as_str())
        return parsed_dict
