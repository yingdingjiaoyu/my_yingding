import pandas as pd
from peewee import *

df = pd.read_excel("E:\\练习数据\\2022年物理类本科院校专业组计划.xlsx")

db = SqliteDatabase('db.sqlite3')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = db

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = 'auth_group'

class DjangoContentType(BaseModel):
    app_label = CharField()
    model = CharField()

    class Meta:
        table_name = 'django_content_type'
        indexes = (
            (('app_label', 'model'), True),
        )

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType)
    name = CharField()

    class Meta:
        table_name = 'auth_permission'
        indexes = (
            (('content_type', 'codename'), True),
        )

class AuthGroupPermissions(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)

    class Meta:
        table_name = 'auth_group_permissions'
        indexes = (
            (('group', 'permission'), True),
        )

class AuthUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = BooleanField()
    is_staff = BooleanField()
    is_superuser = BooleanField()
    last_login = DateTimeField(null=True)
    last_name = CharField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        table_name = 'auth_user'

class AuthUserGroups(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'auth_user_groups'
        indexes = (
            (('user', 'group'), True),
        )

class AuthUserUserPermissions(BaseModel):
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'auth_user_user_permissions'
        indexes = (
            (('user', 'permission'), True),
        )

class DjangoAdminLog(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = TextField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType, null=True)
    object_id = TextField(null=True)
    object_repr = CharField()
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'django_admin_log'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    name = CharField()

    class Meta:
        table_name = 'django_migrations'

class DjangoSession(BaseModel):
    expire_date = DateTimeField(index=True)
    session_data = TextField()
    session_key = CharField(primary_key=True)

    class Meta:
        table_name = 'django_session'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

class YingdingAdmissionsData(BaseModel):
    annual_target = IntegerField(null=True)
    college_property = CharField()
    college_state = CharField(null=True)
    line_2019 = IntegerField(null=True)
    line_2020 = IntegerField(null=True)
    line_2021 = IntegerField(null=True)
    major_group_code = IntegerField()
    major_group_name = CharField()
    plan_change = IntegerField(null=True)
    provinces = CharField()
    ranking_2019 = IntegerField(null=True)
    ranking_2020 = IntegerField(null=True)
    ranking_2021 = IntegerField(null=True)
    region = CharField()
    subject_demand = CharField()

    class Meta:
        table_name = 'yingding_admissions_data'


for i in df.index:
    admissions_data = YingdingAdmissionsData.create(
        major_group_code = df['专业组代码'][i],
        major_group_name = df['专业组名称'][i],
        subject_demand = df['选科要求'][i],
        annual_target = df['计划数'][i],
        plan_change = df['计划增减'][i],
        provinces = df['所在省份'][i],
        region = df['所在地区'][i],
        college_property = df['院校性质'][i],
        college_state = df['院校说明'][i],
        line_2019 = df['2019F'][i],
        line_2020 = df['2020F'][i],
        line_2021 = df['2021F'][i],
        ranking_2019 = df['2019W'][i],
        ranking_2020 = df['2020W'][i],
        ranking_2021 = df['2021W'][i]
    )
