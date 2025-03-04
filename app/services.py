import google.generativeai as genai
from app import models
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_tasks(project_name, location):
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = f"Generate a list of construction tasks for building a {project_name} in {location}. Tasks should be separated with a new line. Don't include anything other than task name. Number of tasks mustn't exceed 10."
    response = model.generate_content(prompt)
    task_list = response.text.split("\n")
    return [{"name": task.strip(), "status": models.TaskStatus.pending} for task in task_list if task.strip()]

def create_project_and_tasks(db: Session, project_data):
    db_project = models.Project(project_name=project_data.project_name, location=project_data.location)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    tasks = generate_tasks(project_data.project_name, project_data.location)

    for task in tasks:
        db_task = models.Task(project_id=db_project.id, name=task["name"], status=task["status"])
        db.add(db_task)
    db.commit()
    db.refresh(db_project)
    return db_project