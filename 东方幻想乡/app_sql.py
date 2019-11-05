from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,func
from sqlalchemy.orm import sessionmaker,relationship,query,backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT,DECIMAL
import enum


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'Oriental_Fantasy_town'
USERNAME = 'root'
PASSWORD = '000000'
#建立连接
DB_URI = 'mysql+mysqlconnector://{username}:{paswsword}@{hostname}/{database}'\
    .format(username=USERNAME,paswsword=PASSWORD,hostname=HOSTNAME,database=DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()
#所属势力表
class Subordinate_forces(Base):
    __tablename__ = 'subordinate_forces'
    id = Column(Integer,primary_key=True,autoincrement=True)
    #势力名称
    company = Column(String(100),nullable=False,unique=True)
    #从属角色信息绑定
    role_information = relationship('Role_information',backref=backref('subordinate_forces'))

    __mapper_args__ = {
        'order_by': id
    }

#角色信息表
class Role_information(Base):
    __tablename__ = 'role_information_list'
    id = Column(Integer,primary_key=True,autoincrement=True)
    #角色名
    role_name = Column(String(100),nullable=False,unique=True)
    #角色年龄
    age = Column(Integer,nullable=True)
    #所属势力
    company = Column(Integer,ForeignKey('subordinate_forces.id'))
    #详细信息绑定
    role_details = relationship('Role_details',backref='role_information_list')

    __mapper_args__ = {
        'order_by': company
    }
#角色详细信息表
class Role_details(Base):
    __tablename__ = 'role_details'
    id = Column(Integer,primary_key=True,autoincrement=True)
    #角色名编号
    role_name = Column(Integer,ForeignKey('role_information_list.id'))
    #角色简介
    brief_introduction = Column(LONGTEXT)

    __mapper_args__ = {
        'order_by': id
    }

Base.metadata.drop_all()
Base.metadata.create_all()
sub_1 = Subordinate_forces(company='迷途之家')
sub_2 = Subordinate_forces(company='白玉楼')
sub_3 = Subordinate_forces(company='博丽神社')
sub_4 = Subordinate_forces(company='妖怪山')
sub_5 = Subordinate_forces(company='人间之里')
sub_6 = Subordinate_forces(company='永远亭')
sub_7 = Subordinate_forces(company='幻梦境')
sub_8 = Subordinate_forces(company='魔界')
sub_9 = Subordinate_forces(company='香霖堂')
sub_10 = Subordinate_forces(company='守矢神社')
sub_11 = Subordinate_forces(company='命莲寺')
sub_12 = Subordinate_forces(company='天界')
sub_13 = Subordinate_forces(company='月面')
sub_14 = Subordinate_forces(company='旧地狱')
sub_15 = Subordinate_forces(company='地狱')
sub_16 = Subordinate_forces(company='要石')
sub_17 = Subordinate_forces(company='雾之湖')
sub_18 = Subordinate_forces(company='雾雨魔法店')
session.add_all([sub_1,sub_2,sub_3,sub_4,sub_5,sub_6,sub_7,sub_8,sub_9,sub_10,sub_11,sub_12,sub_13,sub_14,sub_15,sub_16,sub_17,sub_18])
session.commit()
role_1 = Role_information(role_name='八云紫',age=17,company=1)
role_2 = Role_information(role_name='西行寺幽幽子',age=17,company=2)
role_3 = Role_information(role_name='博丽灵梦',age=16,company=3)
role_4 = Role_information(role_name='射命丸文',age=17,company=4)
role_5 = Role_information(role_name='上白泽慧音',age=17,company=5)
session.add_all([role_1,role_2,role_3,role_4,role_5,])
session.commit()

#关联查询
# a = session.query(Role_information.role_name,Subordinate_forces.company).\
#     join(Subordinate_forces,Role_information.company==Subordinate_forces.id).\
#     order_by(Subordinate_forces.id.desc()).all()
# print(a)


#子查询

# a = session.query(Subordinate_forces.id.label('c_id')).\
#     filter(Subordinate_forces.company=='迷途之家').subquery()
# b = session.query(Role_information).filter(Role_information.company==a.c.c_id).all()
# print(b)


a = session.query(Subordinate_forces).all()
for i in a:
    print(i.company)


#
# ruler = "ruler"
# input(':')
# print(ruler)