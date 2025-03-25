from fastapi import FastAPI, status
import uvicorn

from auth.router import router
from database import engine
from models import Base

app = FastAPI(
    title="SkillBet",
    version="0.1.0",
    description="SkillBet — a platform for skill-based challenges where users bet on their abilities, compete, and prove their expertise to earn rewards.",
)
app.include_router(router)


@app.post("/create_database/")
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        return {"status": status.HTTP_200_OK}


if __name__ == "__main__":
    uvicorn.run("main:app")
