import redis
import json

redis_connection=redis.Redis("localhost","6379",charset="utf-8", decode_responses=True,db=4)



class agency:

    trip_pk,tour_pk=0,0

    def user_creator(self,name,phone_number,age):
        redis_connection.hset(f"user:{name}",mapping={"name":name,"phonenumber":phone_number,"age":age})

        print("ok done!!")
    def trip_creator(self,source,destination,time,vehicle,users):
        passengers={}
        while True:
            i=0
            for elm in users.split(","):
                 passengers[i]=redis_connection.hgetall(f"user:{elm}")
                 i+=1
            else:
                break
            
        redis_connection.hset(f"trip:{source}:{destination}:{time}",mapping={"source":source,"destination":destination,
        "time":time,"vehicle":vehicle,"user":json.dumps(passengers)})

        self.trip_pk+=1

        print("ok done!!")
    def tour_creator(self,leader,users,days,price,source,destination,details):
        passengers={}
        while True:
            i=0
            for elm in users.split(","):
                 passengers[i]=redis_connection.hgetall(f"user:{elm}")
                 i+=1
            else:
                break



        redis_connection.hset(f"tour:{leader}:{source}:{destination}",mapping={"leader":leader,"user":json.dumps(passengers),"days":days,"price":price,
        "source":source,"destination":destination,"details":details})

        self.tour_pk+=1

        print("ok done!!")
    def show_user(self,name):

        return (redis_connection.hgetall(f"user:{name}"))

    
    def show_trip(self,source,destination,time):
        return (redis_connection.hgetall(f"trip:{source}:{destination}:{time}"))

    def show_tour(self,source,destination,leader):
        return (redis_connection.hgetall(f"tour:{leader}:{source}:{destination}"))
        
