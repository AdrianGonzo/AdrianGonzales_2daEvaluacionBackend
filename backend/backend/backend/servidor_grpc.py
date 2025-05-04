import grpc
from concurrent import futures
import os
import sys
import django


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Configurar entorno de Django para acceso a su ORM
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from grpc_client import seguimientos_pb2, seguimientos_pb2_grpc
from django.db import connection

class SeguimientosService(seguimientos_pb2_grpc.SeguimientosServiceServicer):
    def ObtenerSeguimientosProcesados(self, request, context):
        try:
            user_id = request.usuarios_idusuario
            print(f"Llamada gRPC recibida con usuarios_idusuario={user_id}")

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT creadores_idcreador 
                    FROM backend_listaseguidos 
                    WHERE usuarios_idusuario = %s
                """, [user_id])
                rows = cursor.fetchall()
                creadores = [str(row[0]) for row in rows]

            return seguimientos_pb2.SeguimientosResponse(
                total=len(creadores),
                creadores=creadores,
                error=""
            )
        except Exception as e:
            return seguimientos_pb2.SeguimientosResponse(
                total=0,
                creadores=[],
                error=str(e)
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    seguimientos_pb2_grpc.add_SeguimientosServiceServicer_to_server(SeguimientosService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC activo en puerto 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()