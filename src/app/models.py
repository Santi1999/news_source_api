

# # from .database import Base

# # class Articles(BaseModel):
# #     __tablename__ = "articles"

    
# #     _id = Column(Integer, primary_key=True, index=True)
# #     title = Column(String, nullable=False)
# #     url = Column(String, nullable=False)
# #     description = Column(String, nullable=False)
# #     sources = Column(String, nullable=False)

# # class User(BaseModel):
# #     __tablename__ = "users"

# #     id = Column(Integer, primary_key=True, index=True)
# #     first_name = Column(String, nullable=False)
# #     last_name = Column(String, nullable=False)
# #     email = Column(String, nullable=False, unique=True)
# #     password = Column(String, nullable=False)
# #     created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))


# from pydantic import BaseModel, Field
# from bson import ObjectId
# from typing import Optional

# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid ObjectId')
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type='string')

# class ItemModel(BaseModel):
#     id: Optional[PyObjectId] = Field(alias='_id')
#     name: str
#     description: Optional[str] = None

#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {
#             ObjectId: str
#         }