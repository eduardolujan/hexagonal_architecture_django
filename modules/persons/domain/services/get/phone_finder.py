# -*- coding: utf-8 -*-


from modules.persons.domain.entities.phone import GetPhone as GetPhoneEntity
from modules.persons.domain.value_objects.address_values import AddressID


class PhoneFinderService:
    """
    Nameconstructors to get Phone
    """

    @staticmethod
    def create_phone_entity(phone_id: AddressID):
        """

        @param phone_id:
        @type phone_id:
        @return:
        @rtype:
        """

        get_phone_entity = GetPhoneEntity(
            id=phone_id
        )
        return get_phone_entity
