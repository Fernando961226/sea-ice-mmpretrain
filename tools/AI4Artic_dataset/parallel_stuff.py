import multiprocessing
from functools import partial

# def Parallel(function, iterable, *args):
#     '''
#     When the iterable is too long ~> 30000. Try to  distribute it 
#     in more than one run. Otherwise it takes too long to setup the 
#     parallel process.
#     '''
#     n_cores = multiprocessing.cpu_count() - 1
#     print('Configuring CPU multiprocessing...')
#     print('Number of cores: %d'%(n_cores))
#     p = multiprocessing.Pool(n_cores)
#     func = partial(function, *args)
#     x = p.map(func, iterable)
#     p.close()
#     p.join()

#     return x

def Parallel(function, iterable, max_processes=None, *args):
    '''
    When the iterable is too long ~> 30000. Try to distribute it 
    in more than one run. Otherwise it takes too long to setup the 
    parallel process.
    '''
    if max_processes is None:
        max_processes = multiprocessing.cpu_count() - 1
    else:
        max_processes = min(max_processes, multiprocessing.cpu_count() - 1)
    
    print('Configuring CPU multiprocessing...')
    print('Number of processes: %d' % (max_processes))
    
    with multiprocessing.Pool(max_processes) as p:
        func = partial(function, *args)
        x = p.map(func, iterable)
        
    return x