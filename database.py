from models import Session, User

def get_or_create_user(user_id, username=None, first_name=None):
    session = Session()
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            user = User(user_id=user_id, username=username, first_name=first_name)
            session.add(user)
            session.commit()
        return user
    finally:
        session.close()