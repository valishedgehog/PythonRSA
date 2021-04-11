def benchmark(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('[*] Time: {} секунд.'.format(end-start))
    return wrapper