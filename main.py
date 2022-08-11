from hc12 import HC12
import objfunc
import numpy as np
import matplotlib.pyplot as plot
import hc12

# params
dimensions = 10
n_bit_param = 10
n_runs = 1
# objective function
# objective = objfunc.rastrigin
# objective = objfunc.rosenbrock
objective = objfunc.schwefel
# bounds
# bounds rastrigin
if objective == objfunc.rastrigin:
    dod_param = [-5.12, 5.12]
    print('rastrigin')
# bounds rosenbrock
elif objective == objfunc.rosenbrock:
    dod_param = [-5, 10]
    print('rosenbrock')
# bounds schwefel
elif objective == objfunc.schwefel:
    dod_param = [-500, 500]
    print('schwefel')

hc12_instance = HC12(dimensions, n_bit_param, dod_param)
x, fx = hc12_instance.run(objective, n_runs)
best_index = np.argmin(fx)
iteration = []
print(f'x_n: {x[best_index, :]},\nfval ={fx[best_index]}')

for i in range(len(hc12_instance.P)):
    iteration.append(i)
best_lower_index = hc12_instance.N[best_index]
best_upper_index = hc12_instance.N[best_index + 1]
best = hc12_instance.P[best_lower_index:best_upper_index]
best_iter = iteration[best_lower_index:best_upper_index]

plot.step(best_iter, best)
plot.xlabel('Iterations')
plot.ylabel('Fitness Value')
plot.grid(True)
plot.title('Prubeh nejlepsiho reseni, %dD' % dimensions)
plot.show()


