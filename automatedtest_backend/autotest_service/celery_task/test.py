from celery_task.autotask import tasks

def test():
    tasks.add.delay(1)

if __name__ == '__main__':
    test()
