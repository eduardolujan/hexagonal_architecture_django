# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, ForeignKey, Integer, Numeric, SmallInteger, String, Text, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Address(Base):
    __tablename__ = 'address'

    id = Column(UUID, primary_key=True)
    street = Column(String(200), nullable=False)
    interior_number = Column(String(200), nullable=False)
    outside_number = Column(String(200), nullable=False)
    zip_code = Column(String(200), nullable=False)
    city = Column(String(200), nullable=False)
    borough = Column(String(200), nullable=False)
    state = Column(String(200), nullable=False)
    country = Column(String(200), nullable=False)


class AppUser(Base):
    __tablename__ = 'app_user'

    password = Column(String(128), nullable=False)
    last_login = Column(DateTime(True))
    is_superuser = Column(Boolean, nullable=False)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_joined = Column(DateTime(True), nullable=False)
    id = Column(UUID, primary_key=True)


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_group_id_seq'::regclass)"))
    name = Column(String(150), nullable=False, unique=True)


class DjangoCeleryBeatClockedschedule(Base):
    __tablename__ = 'django_celery_beat_clockedschedule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_celery_beat_clockedschedule_id_seq'::regclass)"))
    clocked_time = Column(DateTime(True), nullable=False)
    enabled = Column(Boolean, nullable=False)


class DjangoCeleryBeatCrontabschedule(Base):
    __tablename__ = 'django_celery_beat_crontabschedule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_celery_beat_crontabschedule_id_seq'::regclass)"))
    minute = Column(String(240), nullable=False)
    hour = Column(String(96), nullable=False)
    day_of_week = Column(String(64), nullable=False)
    day_of_month = Column(String(124), nullable=False)
    month_of_year = Column(String(64), nullable=False)
    timezone = Column(String(63), nullable=False)


class DjangoCeleryBeatIntervalschedule(Base):
    __tablename__ = 'django_celery_beat_intervalschedule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_celery_beat_intervalschedule_id_seq'::regclass)"))
    every = Column(Integer, nullable=False)
    period = Column(String(24), nullable=False)


class DjangoCeleryBeatPeriodictask(Base):
    __tablename__ = 'django_celery_beat_periodictasks'

    ident = Column(SmallInteger, primary_key=True)
    last_update = Column(DateTime(True), nullable=False)


class DjangoCeleryBeatSolarschedule(Base):
    __tablename__ = 'django_celery_beat_solarschedule'
    __table_args__ = (
        UniqueConstraint('event', 'latitude', 'longitude'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_celery_beat_solarschedule_id_seq'::regclass)"))
    event = Column(String(24), nullable=False)
    latitude = Column(Numeric(9, 6), nullable=False)
    longitude = Column(Numeric(9, 6), nullable=False)


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        UniqueConstraint('app_label', 'model'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_content_type_id_seq'::regclass)"))
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class DjangoMigration(Base):
    __tablename__ = 'django_migrations'

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_migrations_id_seq'::regclass)"))
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DateTime(True), nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(String(40), primary_key=True, index=True)
    session_data = Column(Text, nullable=False)
    expire_date = Column(DateTime(True), nullable=False, index=True)


class DjangoSite(Base):
    __tablename__ = 'django_site'

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_site_id_seq'::regclass)"))
    domain = Column(String(100), nullable=False, unique=True)
    name = Column(String(50), nullable=False)


class Phone(Base):
    __tablename__ = 'phone'

    id = Column(UUID, primary_key=True)
    number = Column(String(200), nullable=False)
    extension = Column(String(200), nullable=False)


class SocialaccountSocialapp(Base):
    __tablename__ = 'socialaccount_socialapp'

    id = Column(Integer, primary_key=True, server_default=text("nextval('socialaccount_socialapp_id_seq'::regclass)"))
    provider = Column(String(30), nullable=False)
    name = Column(String(40), nullable=False)
    client_id = Column(String(191), nullable=False)
    secret = Column(String(191), nullable=False)
    key = Column(String(191), nullable=False)


class AccountEmailaddres(Base):
    __tablename__ = 'account_emailaddress'

    id = Column(Integer, primary_key=True, server_default=text("nextval('account_emailaddress_id_seq'::regclass)"))
    email = Column(String(254), nullable=False, unique=True)
    verified = Column(Boolean, nullable=False)
    primary = Column(Boolean, nullable=False)
    user_id = Column(ForeignKey('app_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    user = relationship('AppUser')


class AppUserGroup(Base):
    __tablename__ = 'app_user_groups'
    __table_args__ = (
        UniqueConstraint('user_id', 'group_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_user_groups_id_seq'::regclass)"))
    user_id = Column(ForeignKey('app_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    group_id = Column(ForeignKey('auth_group.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    group = relationship('AuthGroup')
    user = relationship('AppUser')


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        UniqueConstraint('content_type_id', 'codename'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_permission_id_seq'::regclass)"))
    name = Column(String(255), nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    codename = Column(String(100), nullable=False)

    content_type = relationship('DjangoContentType')


class AuthtokenToken(Base):
    __tablename__ = 'authtoken_token'

    key = Column(String(40), primary_key=True, index=True)
    created = Column(DateTime(True), nullable=False)
    user_id = Column(ForeignKey('app_user.id', deferrable=True, initially='DEFERRED'), nullable=False, unique=True)

    user = relationship('AppUser', uselist=False)


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'
    __table_args__ = (
        CheckConstraint('action_flag >= 0'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_admin_log_id_seq'::regclass)"))
    action_time = Column(DateTime(True), nullable=False)
    object_id = Column(Text)
    object_repr = Column(String(200), nullable=False)
    action_flag = Column(SmallInteger, nullable=False)
    change_message = Column(Text, nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id', deferrable=True, initially='DEFERRED'), index=True)
    user_id = Column(ForeignKey('app_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    content_type = relationship('DjangoContentType')
    user = relationship('AppUser')


class DjangoCeleryBeatPeriodictask(Base):
    __tablename__ = 'django_celery_beat_periodictask'
    __table_args__ = (
        CheckConstraint('expire_seconds >= 0'),
        CheckConstraint('priority >= 0'),
        CheckConstraint('total_run_count >= 0')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_celery_beat_periodictask_id_seq'::regclass)"))
    name = Column(String(200), nullable=False, unique=True)
    task = Column(String(200), nullable=False)
    args = Column(Text, nullable=False)
    kwargs = Column(Text, nullable=False)
    queue = Column(String(200))
    exchange = Column(String(200))
    routing_key = Column(String(200))
    expires = Column(DateTime(True))
    enabled = Column(Boolean, nullable=False)
    last_run_at = Column(DateTime(True))
    total_run_count = Column(Integer, nullable=False)
    date_changed = Column(DateTime(True), nullable=False)
    description = Column(Text, nullable=False)
    crontab_id = Column(ForeignKey('django_celery_beat_crontabschedule.id', deferrable=True, initially='DEFERRED'), index=True)
    interval_id = Column(ForeignKey('django_celery_beat_intervalschedule.id', deferrable=True, initially='DEFERRED'), index=True)
    solar_id = Column(ForeignKey('django_celery_beat_solarschedule.id', deferrable=True, initially='DEFERRED'), index=True)
    one_off = Column(Boolean, nullable=False)
    start_time = Column(DateTime(True))
    priority = Column(Integer)
    headers = Column(Text, nullable=False)
    clocked_id = Column(ForeignKey('django_celery_beat_clockedschedule.id', deferrable=True, initially='DEFERRED'), index=True)
    expire_seconds = Column(Integer)

    clocked = relationship('DjangoCeleryBeatClockedschedule')
    crontab = relationship('DjangoCeleryBeatCrontabschedule')
    interval = relationship('DjangoCeleryBeatIntervalschedule')
    solar = relationship('DjangoCeleryBeatSolarschedule')


class Person(Base):
    __tablename__ = 'person'

    id = Column(UUID, primary_key=True)
    name = Column(String(200))
    last_name = Column(String(200))
    second_last_name = Column(String(200))
    address_id = Column(ForeignKey('address.id', deferrable=True, initially='DEFERRED'), index=True)
    phone_id = Column(ForeignKey('phone.id', deferrable=True, initially='DEFERRED'), index=True)

    address = relationship('Addres')
    phone = relationship('Phone')


class SocialaccountSocialaccount(Base):
    __tablename__ = 'socialaccount_socialaccount'
    __table_args__ = (
        UniqueConstraint('provider', 'uid'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('socialaccount_socialaccount_id_seq'::regclass)"))
    provider = Column(String(30), nullable=False)
    uid = Column(String(191), nullable=False)
    last_login = Column(DateTime(True), nullable=False)
    date_joined = Column(DateTime(True), nullable=False)
    extra_data = Column(Text, nullable=False)
    user_id = Column(ForeignKey('app_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    user = relationship('AppUser')


class SocialaccountSocialappSite(Base):
    __tablename__ = 'socialaccount_socialapp_sites'
    __table_args__ = (
        UniqueConstraint('socialapp_id', 'site_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('socialaccount_socialapp_sites_id_seq'::regclass)"))
    socialapp_id = Column(ForeignKey('socialaccount_socialapp.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    site_id = Column(ForeignKey('django_site.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    site = relationship('DjangoSite')
    socialapp = relationship('SocialaccountSocialapp')


class AccountEmailconfirmation(Base):
    __tablename__ = 'account_emailconfirmation'

    id = Column(Integer, primary_key=True, server_default=text("nextval('account_emailconfirmation_id_seq'::regclass)"))
    created = Column(DateTime(True), nullable=False)
    sent = Column(DateTime(True))
    key = Column(String(64), nullable=False, unique=True)
    email_address_id = Column(ForeignKey('account_emailaddress.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    email_address = relationship('AccountEmailaddres')


class AppUserUserPermission(Base):
    __tablename__ = 'app_user_user_permissions'
    __table_args__ = (
        UniqueConstraint('user_id', 'permission_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('app_user_user_permissions_id_seq'::regclass)"))
    user_id = Column(ForeignKey('app_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    permission_id = Column(ForeignKey('auth_permission.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    permission = relationship('AuthPermission')
    user = relationship('AppUser')


class AuthGroupPermission(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        UniqueConstraint('group_id', 'permission_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_group_permissions_id_seq'::regclass)"))
    group_id = Column(ForeignKey('auth_group.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    permission_id = Column(ForeignKey('auth_permission.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    group = relationship('AuthGroup')
    permission = relationship('AuthPermission')


class SocialaccountSocialtoken(Base):
    """
    SocialaccountSocialtoken
    """
    __tablename__ = 'socialaccount_socialtoken'
    __table_args__ = (
        UniqueConstraint('app_id', 'account_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('socialaccount_socialtoken_id_seq'::regclass)"))
    token = Column(Text, nullable=False)
    token_secret = Column(Text, nullable=False)
    expires_at = Column(DateTime(True))
    account_id = Column(ForeignKey('socialaccount_socialaccount.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    app_id = Column(ForeignKey('socialaccount_socialapp.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    account = relationship('SocialaccountSocialaccount')
    app = relationship('SocialaccountSocialapp')
