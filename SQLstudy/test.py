from app import db,Note

# 向数据库中添加三条留兰
note1 = Note(body='remember Sammy Jankis')
note2 = Note(body='SHAVE')
note3 = Note(body='DON NOT BELIEVE HIS LIES, HE IS THE ONE , KILL HIM')

db.session.add(note1)
db.session.add(note2)
db.session.add(note3)
db.session.commit()