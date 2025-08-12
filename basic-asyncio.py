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

if __name__=="__main__":
    asyncio.run(main_basic_nonconcurrent())
    asyncio.run(main_basic_concurrent())
    asyncio.run(main_gather_concurrent())
    asyncio.run(main_task_group_concurrent())