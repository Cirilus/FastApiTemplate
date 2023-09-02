import uuid
from sqlalchemy.ext.declarative import declarative_base

EntityMeta = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())