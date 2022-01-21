import math

def translate(file_name='circuit_n53_m14_s0_e0_pEFGH'):
    n = int(file_name.split('_')[1][1:])
    with open(file_name+'.py', 'r') as f:
        lines = f.readlines()
    f.close()

    f_write = open(file_name+'.qsim', 'w')
    f_write.write('{}\n'.format(n))

    depth_current = -1
    for i in range(len(lines)):
        line = lines[i].strip().rstrip(',')
        if line == 'QUBIT_ORDER = [':
            qubits = []
            for j in range(i+1, i+1+n):
                line = lines[j].strip().rstrip(',')
                qubits.append(line)
            continue
        if line == 'cirq.Moment(operations=[':
            depth_current += 1
        elif line[:19] == 'cirq.PhasedXPowGate':
            tmp = lines[i+1].strip()
            f_write.write('{} hz_1_2 {}\n'.format(depth_current, qubits.index(tmp[17:37])))
            i += 1
        elif line[:13] == '(cirq.X**0.5)':
            f_write.write('{} x_1_2 {}\n'.format(depth_current, qubits.index(line[17:37])))
        elif line[:13] == '(cirq.Y**0.5)':
            f_write.write('{} y_1_2 {}\n'.format(depth_current, qubits.index(line[17:37])))
        elif line[:7] == 'cirq.Rz':
            l = line.split(' ', 2)[2].split(')', 1)
            f_write.write('{} rz {} {:.17f}\n'.format(depth_current,
                                                      qubits.index(l[1][4:24]),
                                                      math.pi * float(l[0])))
        elif line[:13] == 'cirq.FSimGate':
            l = line.split('=')
            theta = l[1].split(',')[0]
            phi = l[2].split(')')[0]
            l = lines[i+1].strip()
            qubit1 = qubits.index(l[:20])
            qubit2 = qubits.index(l[22:42])
            f_write.write('{} fs {} {} {} {}\n'.format(depth_current, qubit1, qubit2, theta, phi))
    f_write.close()


if __name__ == '__main__':
    import os
    raw_list = os.listdir('.')
    file_list = []
    for i in range(len(raw_list)):
        tmp = os.path.splitext(raw_list[i])
        if tmp[1] == '.py' and tmp[0][:7] == 'circuit':
            file_list.append(tmp[0])
    for file_name in file_list:
        translate(file_name)