from fastapi import FastAPI

from presentation.controllers.users_controller import router as users_router
from presentation.controllers.roles_controller import router as roles_router
from presentation.controllers.activity_types_controller import router as activity_types_router
from presentation.controllers.business_values_controller import router as business_values_router
from presentation.controllers.priorities_controller import router as priorities_router
from presentation.controllers.status_controller import router as status_router


app = FastAPI(
    title="Scrum Planning API",
    version="1.0.0"
)


app.include_router(users_router)
app.include_router(roles_router)
app.include_router(activity_types_router)
app.include_router(business_values_router)
app.include_router(priorities_router)
app.include_router(status_router)
