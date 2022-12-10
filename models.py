import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Users_board(Base):
    __tablename__ = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    # ads_board = relationship("Ads_board", back_populates='users_board')
    def __str__(self):
        return f'Users{self.id}: {self.name}'


class Ads_board(Base):
    __tablename__ = 'ads'

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)

    users_board = relationship(Users_board, backref='ads_board')

    def __str__(self):
        return f'Ads{self.id}: ({self.name}, {self.description})'


def create_tables(engine):
    Base.metadata.create_all(engine)
