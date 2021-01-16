
import json
import uuid


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
        if isinstance(obj, uuid.UUID4):
            return str(obj)

        return json.JSONEncoder.default(self, obj)
