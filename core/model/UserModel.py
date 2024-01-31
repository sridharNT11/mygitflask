from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete,text
from sqlalchemy.sql import and_, or_
from core import app
import json

engine = create_engine(app.config['DATABASE_URI'])

class UserModel():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.users = Table("users", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)

    def get(self,user_id):       
        conn = engine.connect()
        stmt = select([self.users]).where(self.users.c.user_id.in_([user_id]))
        result = conn.execute(stmt)
        output = result.fetchone()
        conn.close()
        return output
    
    def insert(self,data):
        conn = engine.connect()
        result = conn.execute(self.users.insert(), data)
        conn.close()
        user_id = [r for r in result.inserted_primary_key] if result.inserted_primary_key else None
        return user_id
    
    def update(self,user_id,data):
        stmt = self.users.update().where(self.users.c.user_id.in_([user_id])).values(data)
        conn = engine.connect()
        result = conn.execute(stmt)
        conn.close()
        if result:
            return 'success'
        else :
            return 'fail'



    def is_exsits_user(self,email,mobile):       
        conn = engine.connect()
        stmt = text("select * from users where email = :email or mobile = :mobile")
        results = conn.execute(stmt,email=email,mobile=mobile)
        conn.close()
        return [dict(r) for r in results] if results else None
            
    def get_move_data(self):       
        conn = engine.connect()
        stmt = text("select * from  tmp_asset_to_move where new_user_id is not null and is_data_moved is null;")
        results = conn.execute(stmt)
        conn.close()
        return [dict(r) for r in results] if results else None
    

