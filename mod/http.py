import asyncio
import time


def fetch(url):
    """ Make req and return result """
    pass

def worker(name,queue,results):
    """ A func to take and make req from a queue and perform the work then add result to results list"""
    
    pass

async def distribute_work(url,requests,concurrency,result):
    """ Divide work into batches and collect final results"""
    queue =  asyncio.Queue()
    
    for _ in range(requests):
        queue.put_nowait(url)

    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1},queue,results"))
        tasks.append(task)
    started_at =  time.monotonic()
    await queue.join()
    total_time =  time.monotonic() - started_at
    for task in tasks:
        task.cancel()

    print("-------")
    print (
        f"{concurrency} workers took {total_time:.2f} seconds to complete {len(results)} requests"
    )


def duck(url,requests,concurrency):
    """Entry point to making requests"""
    results = []
    asyncio.run(distribute_work(url,requests,concurrency,results))
    print(results)
    pass

