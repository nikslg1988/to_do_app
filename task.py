class Task:
    '''Класс Task для перехода в ООП'''
    def __init__(self, task_id, title, tag, priority, done, created):
        '''Инициализатор'''
        self.id = task_id
        self.title = title
        self.tag = tag
        self.priority = priority
        self.done = done
        self.created = created
   
    def to_dict(self):
        return{
           "id": self.id,
            "title": self.title,
            "tag": self.tag,
            "priority": self.priority,
            "done": self.done,
            "created": self.created 
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            task_id=data['id'],
            title=data['title'],
            tag=data['tag'],
            priority=data['priority'],
            done=data['done'],
            created=data['created']
        )       
        
    def __str__(self):
        status = "✅" if self.done else "⏳"
        return f"[{self.id}] {self.title} | тег: {self.tag} | приоритет: {self.priority} | создана: {self.created} {status}"