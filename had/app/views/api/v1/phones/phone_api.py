# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.infrastructure.bus.message.in_memory import InMemoryMessageBus
from modules.shared.infrastructure.requests.django import Request as DjangoRequest
from modules.shared.infrastructure.responses.django import RestResponse as DjangoRestResponse
from modules.shared.infrastructure.persistence.django import UnitOfWork as DjangoUnitOfWork
from modules.shared.infrastructure.serializers.django.serializer_manager import SerializerManager
from modules.persons.infrastructure.serializers.django.phone import GetPhoneSerializer
from modules.persons.infrastructure.serializers.django.phone import PhoneSerializer
from modules.persons.infrastructure.repository.django import PhoneRepository
# Application
from modules.persons.application.controllers.v1.phone import GetPhoneController
from modules.persons.application.controllers.v1.phone import CreatePhoneController


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class PhoneApi(APIView):
    """
    Address API
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, id):
        """
        Get User
        @param request:
        @type request:
        @param _id:
        @type _id:
        @return:
        @rtype:
        """
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        phone_repository = PhoneSerializer()
        request_serializer_manager = SerializerManager(GetPhoneSerializer)
        response_serializer_manager = SerializerManager(PhoneSerializer)
        in_memory_message_bus = InMemoryMessageBus()
        get_phone_controller = GetPhoneController(
            request,
            response,
            phone_repository,
            request_serializer_manager,
            response_serializer_manager,
            in_memory_message_bus)

        response = get_phone_controller(id)
        return response

    def post(self, request):
        """
        POST VERB
        @param request: request
        @type request: Request
        @return: Response
        @rtype: Response
        """

        request = DjangoRequest(request)
        response = DjangoRestResponse()
        phone_repository = PhoneRepository()
        unit_of_work = DjangoUnitOfWork()
        phone_serializer_manager = SerializerManager(PhoneSerializer)
        in_memory_message_bus = InMemoryMessageBus()

        create_user_controller = CreatePhoneController(
            request,
            response,
            phone_serializer_manager,
            phone_repository,
            unit_of_work,
            in_memory_message_bus)

        response = create_user_controller()
        return response


