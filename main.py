from celery_hello_world.tasks import hello_world

if __name__ == "__main__":
    
    result = hello_world.delay()
    print('Task result:', result.get())

