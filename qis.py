import matplotlib.pyplot as plt

from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('fd3b7dde427065d5045932ab6939a3eee6f42786a83e274d8b620032e3912a47040d6e30fd0d2ec7625c5561dbe14867aad5f9168f15a5f70b6e984cb75d35d4')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')

    
q = QuantumRegister(8,'q')
c = ClassicalRegister(8,'c')

circuit = QuantumCircuit(q,c)


circuit.ch(q[0], q[1]);
circuit.x(q[2])
circuit.ch(q[2], q[3]);
circuit.x(q[4])
circuit.ch(q[4], q[5]);
circuit.x(q[6])
circuit.ch(q[6], q[7]);
circuit.measure(q,c)

print(circuit)

job = execute(circuit, backend, shots=20000)

job_monitor(job)
counts = job.result().get_counts()

probability = []
for value in counts.values():
	pro = value / 20000
	probability.append(pro) 

print(counts)
plt.hist(probability, edgecolor = 'black')
plt.show()

#prawdopobienstwo na osi y powinno byc