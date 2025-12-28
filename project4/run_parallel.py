from concurrent.futures import ThreadPoolExecutor, as_completed

def run_parallel(func, inputs, max_workers=20):
    """Run func on each input in parallel threads."""
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(func, inp): inp for inp in inputs}
        for future in as_completed(futures):
            inp = futures[future]
            try:
                result = future.result()
            except Exception:
                result = None
            results.append((inp, result))
    return results


# to understand this code; imagine this example;
# you should have a function + some inputs on it:
# function;
# import time

# def square_number(n):
#     print(f"Starting {n}")
#     time.sleep(1)           # simulate slow work
#     print(f"Finished {n}")
#     return n * n
# inputs ;
# Starting 1
# Finished 1
# Starting 2
# Finished 2
# Starting 3
# Finished 3
# Starting 4
# Finished 4

# Takes 4 seconds

# Results:

# [(1, 1), (2, 4), (3, 9), (4, 16)]
# Now if you run the same function , input using this script above it will take 1sec;
# as all inputs will go to one thread -> each thread run it parallel with it's bro
# it will 1 sec
