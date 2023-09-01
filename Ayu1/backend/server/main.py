import grpc
import examples_pb2
import examples_pb2_grpc
#from config import database_auth
from concurrent import futures
# use the file db.json in the same folder
import json

class DataServer(examples_pb2_grpc.Data):
    
    def GetWeatherData(self, request, context):
        print("GetWeatherData")
        # use the file db.json in the same folder
        
        f = open('db.json')
        data = json.load(f)
        arr = []
        for i in data['weather']:
            # introduce the data from the db to the temperature dictionary
            temperature = {
                "id": i['id'],
                "temp": i['temp'],
                "time": i['time'],
                "date": i['date']
            }
            arr.append(temperature)
        # put an array into the temperature_response
        temperature_response = examples_pb2.WeatherResponse(**arr[0])
        return temperature_response
    
    def GetCoinsData(self, request, context):
        print("GetCoinsData")
        #cur.execute("SELECT * FROM cash where date = '"+ str(current_date) +"' order by id desc limit 1")
        # coins = cur.fetchall()
        coins = {
            "id": 1,
            "dolar": "800.0",
            "euro": "900.0",
            "uf": "10000.0",
            "time": "12:00:00",
            "date": "2020-01-01"
        }
        coins_response = examples_pb2.CoinsResponse(**coins)
        return coins_response
        
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    examples_pb2_grpc.add_DataServicer_to_server(DataServer(), server)
    #Exponer a cualquier IP en el puerto 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    
    print("GRPC persistor server working")
    server.wait_for_termination()


if __name__ == '__main__':
    #conn = database_auth.get_db()
    #cur = conn.cursor()
    main()