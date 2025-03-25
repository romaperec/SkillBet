from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine = create_async_engine("sqlite+aiosqlite:///skillbet.sqlite3")
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
    