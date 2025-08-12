import asyncio

# no concurrency coroutine simulating time-consuming task
async def fetch_data_basic(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay)
    print("Data fetched, id:", id)
    return {"data": "some data", "id": id}

async def main_basic_nonconcurrent() -> object:
    print("start of main basic nonconcurrent coroutine")
    
    task1 = fetch_data_basic(2,1)
    task2 = fetch_data_basic(2,2)

    result1 = await task1
    print(f"received result: {result1}")

    result2 = await task2
    print(f"recieved result: {result2}")
    
    print("end of main coroutine")

# use tasks to run coroutines concurrently
# receive results at the end all at the same time
async def main_basic_concurrent() -> object:
    print("start of main basic concurrent coroutine")

    task1 = asyncio.create_task(fetch_data_basic(1,2))
    task2 = asyncio.create_task(fetch_data_basic(2,3))
    task3 = asyncio.create_task(fetch_data_basic(3,1))

    result1 = await task1
    result2 = await task2 
    result3 = await task3

    print(result1, result2, result3)
    print("end of main basic concurrent coroutine")

# use gather for a bunch of function calls, not great for errors
async def main_gather_concurrent() -> object:
    print("start of main gather concurrent coroutine")

    results = await asyncio.gather(fetch_data_basic(1,2), fetch_data_basic(2,1), fetch_data_basic(3,3))

    for result in results:
        print(f"received result: {result}")

    print("end of main gather concurrent coroutine")

# use task group which is a newer feature
async def main_task_group_concurrent() -> object:
    print("start of main task group concurrent coroutine")
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data_basic(sleep_time, i))
            tasks.append(task)
    
    # stop blocking
    results = [task.result() for task in tasks]

    for result in results:
        print(f"received result: {result}")

    print("end of main task group concurrent coroutine")

async def set_future_result(future, value):
    await asyncio.sleep(2)
    future.set_result(value)
    print(f"set future's result to: {value}")

# result will come in future, don't know when it will come
async def future_func():
    # probably will never do this in real life
    loop = asyncio.get_running_loop()
    # set this and await it - may or may not complete, waiting for it to be available, not waiting for a whole coroutine or task to finish
    future = loop.create_future()

    asyncio.create_task(set_future_result(future, "future result is ready"))

    # wait for future result, not the entire task (it might not complete)
    result = await future
    print(f"received future's result: {result}")

"""Synchronization"""
#shared variable - if 2 coroutines handling same data, weird errors, so lock it
shared_resource = 0

# an asyncio lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # check if coroutine is using the lock, wait for it to finish, or start:
        print(f"resource before mod: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(1) # simulate IO operation
        print(f"resource after mod: {shared_resource}")

async def main_mod_shared_resource():
    #* unpakcs into separate arguments
    await asyncio.gather(*(modify_shared_resource() for _ in range (5)))

# semaphore is like a lock but multiple coroutines access same resource at same time
async def access_resource(semaphore, resource_id):
    async with semaphore:
        print(f"accessing resource {resource_id}")
        await asyncio.sleep(2)
        print(f"releasing resource {resource_id}")

async def demo_semaphore():
    sempahore = asyncio.Semaphore(2) #allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

if __name__=="__main__":
    asyncio.run(main_basic_nonconcurrent())
    asyncio.run(main_basic_concurrent())
    asyncio.run(main_gather_concurrent())
    asyncio.run(main_task_group_concurrent())
    asyncio.run(future_func())
    asyncio.run(main_mod_shared_resource())
    asyncio.run(demo_semaphore())