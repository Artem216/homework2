from .models import User, Parametrs
from .loader import Session
from aiogram.types import Message

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


# User methods
def create_user(db: Session, msg: Message) -> User:
    """Получает пользователя 

    Args:
        db (Session): Сессия с бд 
        msg (Message): Сообщение от телеграм бота
    Returns:
        User: Модель пользователя
    """
    
    user = db.query(User).filter(User.id == msg.from_user.id).one_or_none()
    if user is None:
        user = User(
            id=msg.from_user.id,
            first_name=msg.from_user.first_name,
            last_name=msg.from_user.last_name,
            username=msg.from_user.username,
        )

        db.add(user)
        db.commit()
    return user


def get_user(db: Session, user_id: int) -> User | None:
    """Получение пользователя по user.id

    Args:
        db (Session): Сессия с бд 
        user_id (int): telegram id пользователя
    Returns:
        User | None: _description_
    """
    user = db.query(User).filter(User.id == user_id).one_or_none()
    return user
    

# Answers 
def get_user_answer(db: Session, user_id: int) -> Parametrs:
    """Получение ответа пользователя

    Args:
        db (Session): Сессия с бд 
        user_id (int): telegram id пользователя

    Returns:
        Parametrs: Последний ответ пользователя
    """
    answer = db.query(Parametrs).filter(Parametrs.user_id == user_id).one_or_none()
    if answer is None:
        answer = Parametrs(user_id=user_id)
    return answer


def save_answer(db: Session, answer: Parametrs) -> None:
    """Сохранение ответа в бд

    Args:
        db (Session): Сессия с бд 
        answer (Answer): Измененый ответ пользователя
    """
    db.add(answer)
    db.commit()