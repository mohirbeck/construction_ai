from fastapi import FastAPI
from app import routes, database
from app.database import engine
from app import models
import asyncio
import random
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

models.Base.metadata.create_all(bind=engine)

async def simulate_task_completion(db: Session, project_id: int):
    while True:
        await asyncio.sleep(5)
        project = db.query(models.Project).filter(models.Project.id == project_id).first()
        if not project or project.status == models.ProjectStatus.completed:
            break

        pending_tasks = [task for task in project.tasks if task.status == models.TaskStatus.pending]
        if pending_tasks:
            task_to_complete = random.choice(pending_tasks)
            task_to_complete.status = models.TaskStatus.completed
            db.commit()
            all_tasks_completed = all(task.status == models.TaskStatus.completed for task in project.tasks)
            if all_tasks_completed:
                project.status = models.ProjectStatus.completed
                db.commit()

async def startup_event():
    db = database.SessionLocal()
    try:
        projects = db.query(models.Project).filter(models.Project.status != models.ProjectStatus.completed).all()
        for project in projects:
            asyncio.create_task(simulate_task_completion(db, project.id))
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await startup_event()
    yield
    # Shutdown
    pass

app = FastAPI(lifespan=lifespan)

app.include_router(routes.router)