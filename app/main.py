from fastapi import FastAPI
from app.database import engine
from app.auth import models, routers
import actions.accounts.routers 
import actions.categories.routers 
import actions.transactions.routers 

app = FastAPI(
    title="Financial API",
    description="API para consulta e gerenciamento de dados financeiros.",
    version="1.0.0",
    contact={
        "name": "Maria Claudino",
        "url": "https://github.com/mariacfclaudino", 
        "email": "mariacfclaudino@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
    {"name": "Financial", "description": "Consulta e gerenciamento de registros financeiros."},
    ]
)


models.Base.metadata.create_all(engine)
app.include_router(routers.router)
app.include_router(actions.accounts.routers.router)
app.include_router(actions.categories.routers.router)
app.include_router(actions.transactions.routers.router)