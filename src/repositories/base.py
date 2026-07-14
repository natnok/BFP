from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base


class BaseRepository:
    def __init__(self, session):
        self.session = session

    model: type[Base]
    schema: type[BaseModel]
    session: AsyncSession

    async def get_all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        print(query.compile(compile_kwargs={"literal_binds": True}))
        return [self.schema.model_validate(model, from_attributes=True) for model in result.scalars().all()]

    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        print(query.compile(compile_kwargs={"literal_binds": True}))
        model = result.scalars().one_or_none()

        if model is None:
            return None

        return self.schema.model_validate(model, from_attributes=True)

    async def post(self, data: BaseModel):
        query = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(query)
        print(query.compile(compile_kwargs={"literal_binds": True}))
        model = result.scalars().one()
        return self.schema.model_validate(model, from_attributes=True)

    async def put(self, data: BaseModel, exclude_unset: bool = False, **filter_by):
        query = (
            update(self.model)
            .filter_by(**filter_by)
            .values(**data.model_dump(exclude_unset=exclude_unset))
            .returning(self.model)
        )
        result = await self.session.execute(query)
        print(query.compile(compile_kwargs={"literal_binds": True}))
        model = result.scalars().one()
        return self.schema.model_validate(model, from_attributes=True)

    async def delete(self, **filter_by):
        query = delete(self.model).filter_by(**filter_by).returning(self.model)
        result = await self.session.execute(query)
        print(query.compile(compile_kwargs={"literal_binds": True}))
        model = result.scalars().one()
        return self.schema.model_validate(model, from_attributes=True)
