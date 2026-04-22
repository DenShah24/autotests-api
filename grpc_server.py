import grpc
from concurrent import futures
import user_service_pb2_grpc  # Генерируемый импорт


class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    # Обязательный отступ! Добавьте методы или pass
    def GetUser(self, request, context):  # Пример метода из .proto
        # Логика метода
        return user_service_pb2.User(id=request.id, name="Test")  # Замените на ваш response

    # Добавьте ВСЕ методы из вашего .proto!


def serve():  # Без отступа от класса!
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    print("gRPC сервер запущен на порту 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()