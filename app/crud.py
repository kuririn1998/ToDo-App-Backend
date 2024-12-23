from sqlalchemy.orm import Session
from . import models, schemas

def get_tasks(db: Session, owner_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == owner_id).all()

def create_task(db: Session, task: schemas.TaskCreate, owner_id: int):
    db_task = models.Task(**task.dict(), owner_id=owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, owner_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == owner_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
