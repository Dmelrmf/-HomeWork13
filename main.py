import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Ads_board, Users_board

DSN = 'postgresql://postgres:1230-=@localhost:5432/buletrin_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = Users_board(name='John')
print(user1.id)

session.add(user1)
session.commit()

ad_1 = Ads_board(number=1, description='первое объявление')
ad_2 = Ads_board(number=2, description='второе объявление')
session.add_all([ad_1, ad_2])
session.commit()

#session.query(Users_board).update()
#session.query(Ads_board).update()
#session.query(Ads_board).delete()

for c in session.query(Ads_board).all():
    print(c)


session.close()