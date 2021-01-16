

class AllianzeAccountCreator:
    """
    Allianze Account Creator
    """

    def __init__(self, allanze_account_command):
        self.allanze_account_command = allanze_account_command


    def __call__(self):
        self.__repo.update_or_create()



allianze_serializer = AllianzeAccountSerializer(data=request.data)
if not allianze_serializer.is_valid():
    exception =  Exception(f"Not valid")
    exception.errors = allianze_serializer.errors
    raise exception


allizance_data = allianze_serializer.data

allianze_account_creator = AllianzeAccountCreator(**allizance_data)
allianze_account_creator()
