import cirq
import numpy as np

QUBIT_ORDER = [
    cirq.GridQubit(0, 5),
    cirq.GridQubit(0, 6),
    cirq.GridQubit(1, 4),
    cirq.GridQubit(1, 5),
    cirq.GridQubit(1, 6),
    cirq.GridQubit(1, 7),
    cirq.GridQubit(2, 4),
    cirq.GridQubit(2, 5),
    cirq.GridQubit(2, 6),
    cirq.GridQubit(2, 7),
    cirq.GridQubit(2, 8),
    cirq.GridQubit(3, 2),
    cirq.GridQubit(3, 3),
    cirq.GridQubit(3, 4),
    cirq.GridQubit(3, 5),
    cirq.GridQubit(3, 6),
    cirq.GridQubit(3, 7),
    cirq.GridQubit(3, 8),
    cirq.GridQubit(3, 9),
    cirq.GridQubit(4, 1),
    cirq.GridQubit(4, 2),
    cirq.GridQubit(4, 3),
    cirq.GridQubit(4, 4),
    cirq.GridQubit(4, 5),
    cirq.GridQubit(4, 6),
    cirq.GridQubit(4, 7),
    cirq.GridQubit(4, 8),
    cirq.GridQubit(5, 1),
    cirq.GridQubit(5, 2),
    cirq.GridQubit(5, 3),
    cirq.GridQubit(5, 4),
    cirq.GridQubit(5, 5),
    cirq.GridQubit(5, 6),
    cirq.GridQubit(5, 7),
    cirq.GridQubit(6, 1),
    cirq.GridQubit(6, 2),
    cirq.GridQubit(6, 3),
    cirq.GridQubit(6, 4),
    cirq.GridQubit(6, 5),
    cirq.GridQubit(6, 6),
    cirq.GridQubit(6, 7),
    cirq.GridQubit(7, 2),
    cirq.GridQubit(7, 3),
    cirq.GridQubit(7, 4),
    cirq.GridQubit(7, 5),
    cirq.GridQubit(7, 6),
    cirq.GridQubit(8, 3),
    cirq.GridQubit(8, 4),
]

CIRCUIT = cirq.Circuit(
    [
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.3448162225275961).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.24851733121171846).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -2.079870303178702).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 2.0436918407499873).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 1.2371391697444234).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -1.2825274365288457).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.6529975013575373).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.21248377848559125).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -2.0638841157306445).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 2.10101302367136).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.2767373377033284).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.18492941569567625).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.02232591119805812).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.030028573876142287).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.7202887499204607).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.7234018331756271).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.8467509808142173).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.8164932597686655).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -1.00125113388313).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 1.1224546746752684).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.16310561378711827).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.1766183348870303).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.22542387771877406).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.2814659583608806).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.33113463396189063).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.40440704518468423).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.254599699022151).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.3888269305757545).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.4081262439699967).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.3666829187201306).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.3507308388473503).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.37554649493270875).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.46476180085128416).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.8746667712773398).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -1.4187954353764791).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 1.5102819373895253).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.1516394851691686).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.23575835453119093).on(cirq.GridQubit(7, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.545844435173598, phi=0.5163254336997252).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5033136051987404, phi=0.5501439149572028).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5930079664614663, phi=0.5355369376884288).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.59182423935832, phi=-5.773664463980115).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5886126292316385, phi=0.4838919055156303).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.5862983338115253, phi=0.5200148508319427).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5286450573669954, phi=0.5113953905811602).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.4887741478969256, phi=0.7140224757490621).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.565622495548066, phi=0.5127256481964074).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5289739216684795, phi=0.5055240639761313).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5384796865621224, phi=0.5293381306162406).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.4727562833004122, phi=0.4552443293379814).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5346175385256955, phi=0.5131039467233695).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.558221035096814, phi=0.4293113178636455).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5169062231051558, phi=0.46319906116805815).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5705414623224259, phi=0.4791699064049766).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.2445075810671158, phi=0.36440873167184756).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5516764540193888, phi=0.505545707839895).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5699606675525557, phi=0.48292170263262457).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 1.2570424650348733).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -1.3533413563507508).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 1.3803105504474993).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -1.4164890128762133).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.7660705551087533).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.7206822883243308).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 1.3183560383893944).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -1.7588697612613406).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.9354142698937665).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.8982853619530515).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.6722145774944012).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.7640224995020534).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.5799079899133832).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.5876106525914674).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.40802714165944654).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.40491405840427996).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 1.0843371101222938).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -1.1145948311678457).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.7990757781248072).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.6778722373326689).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -1.6258237067659351).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 1.6393364278658469).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.7948295009385445).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.7387874202964381).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.049341949396894985).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.02393046182589869).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.07085461727529008).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.06337261427831344).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.4710627118441926).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.5125060370940587).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 2.1645856475342256).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -2.1397699914488673).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -1.1742149239472004).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.7643099535211447).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 1.2773117920270392).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -1.1858252900139932).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.5606941860998265).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.6448130554618487).on(cirq.GridQubit(7, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -2.0179756248661533).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 2.064958427369896).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -5.435868884042397).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 5.438497289344933).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -5.19048555249959).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 5.170988862096221).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 3.362366769065076).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -3.655232369531361).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 2.5333591271878086).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -2.4748096263683066).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -4.480708067260001).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 4.525888267898699).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 2.763288476134621).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -2.7382876075948173).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -4.882352366676035).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 4.924090864144291).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 2.135954522972214).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -2.1822665205802965).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -3.7780476633662574).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 3.817335880513747).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 3.493947788627223).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -3.4959511719278638).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -2.8819419896554686).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 2.9028256034569604).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.7811374803446167).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.6780279413275597).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 1.863573798571082).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -2.150412392135508).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 2.2532274955007456).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -2.5360843333016145).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 2.3134893226730737).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -2.238493420699622).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -4.378582817568972).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 4.459782783273393).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 1.42630741834175).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -1.5270341780432073).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -5.727962526439221).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 5.724551729056993).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 2.004655903613833).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -2.037595034198167).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5454967174552687, phi=0.5074540278986153).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.5233234922971755, phi=0.6681144400379464).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5644541080112795, phi=0.5439498075085039).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5866139110090092, phi=0.5693597810559818).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.2947043217999283, phi=0.4859467238431821).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.541977006124425, phi=0.6073798124875975).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5573072833358306, phi=0.5415514987622351).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5345751514593928, phi=0.472462117170605).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.5138652502397498, phi=0.47710618607286504).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5849169442855044, phi=0.54346233613361).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5317226133698079, phi=0.6723463192657011).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4838884067961586, phi=0.5070681071136852).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5398075246432927, phi=0.5174515645943538).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4593314109380113, phi=0.5230636172671492).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.4902099797510393, phi=0.4552057582549894).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5376836849431186, phi=0.46265685930712236).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.555185434982808, phi=0.6056351386305033).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.4749003996237158, phi=0.4353609222411594).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5249018931362641, phi=0.7521905394129447).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.4908753240086248, phi=0.47848614251537785).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 1.6292875119692507).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -1.5823047094655076).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 5.79385605258612).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -5.791227647283584).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 5.223139057027918).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -5.242635747431287).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -2.7477760804704774).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 2.454910480004192).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -2.346072351850546).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 2.404621852670048).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 5.048199817882042).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -5.0030196172433445).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -2.578152260365417).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 2.60315312890522).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 4.080045044703728).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -4.038306547235473).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -2.6543362735839113).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 2.6080242759758283).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 3.9045088495271663).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -3.8652206323796765).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -2.794685929171329).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 2.7926825458706883).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 1.9770644223044243).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -1.9561808085029322).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -1.5516585295358842).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 1.6547680685529413).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -1.8933072151541963).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 1.6064686215897703).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.5449135022758093).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.2620566644749405).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -2.3490397609251703).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 2.424035662898622).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 5.25154083730089).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -5.170340871596469).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -1.8655832225378013).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 1.7648564628363437).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 5.618255473178423).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -5.621666270560651).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.9199486914996435).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.8870095609153098).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 2.8643854265554056).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -2.9033805954708463).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -2.3793800740028206).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 2.142523606048688).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -6.214223110662173).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 6.24431588336413).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -6.196295096608877).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 6.191833422443152).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -5.367868774756692).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 5.257156584109544).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -1.6118072404137829).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 1.5665192386902935).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -1.5736126437571512).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 1.5796534031340996).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -8.599392694559281).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 8.58638977635296).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -5.408932498710608).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 5.396221422935972).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -3.2786928385561493).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 3.339006443218924).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -5.390755870544794).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 5.4172568990486605).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -5.620144773112766).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 5.630469153514815).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 4.367652291347506).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -3.9105776028384707).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 3.0814399461790716).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -3.1208364909653903).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 7.0181466269225865).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -7.000766026200176).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 5.700873278515409).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -5.683378195921049).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 4.586335789661189).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -4.76537552715921).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 5.424178494472165).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -5.503525609076518).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 5.401133511743327).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -5.367614604132787).on(cirq.GridQubit(7, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4937034321050129, phi=0.5388459463555662).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5015413274420961, phi=0.51076415920643).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.505206014385737, phi=0.5177720559789512).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5588791081427968, phi=0.559649620487243).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5907035825834708, phi=0.5678223287662552).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5296321276792553, phi=0.537761951313038).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.619276265426104, phi=0.48310297196088736).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.6116663075637374, phi=0.5343172366969327).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.5306030283605572, phi=0.5257102080843467).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.589821065740506, phi=0.5045391214115686).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5472406430590444, phi=0.5216932173558055).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5124128267683938, phi=0.5133142626030278).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5707871303628709, phi=0.5176678491729374).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5337916352034444, phi=0.5123546847230711).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.596346344028619, phi=0.5104319949477776).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.53597466118183, phi=0.5584919013659856).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.385350861888917, phi=0.5757363921651084).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.614843449053755, phi=0.5542252229839564).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.505922331941178, phi=0.4892027060568212).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -3.72824674565976).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 3.6892515767443195).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 2.8795906763472114).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -3.116447144301344).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 6.89944406229822).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -6.869351289596263).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 6.506615138479995).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -6.511076812645719).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 6.150506057270183).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -6.2612182479173315).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 2.4087294851133443).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -2.4540174868368334).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 2.8100043579049445).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -2.8039635985279965).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 9.032480388130898).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -9.04548330633722).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 4.737705877923889).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -4.750416953698525).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 2.9425087256630427).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -2.882195121000268).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 4.466531408750767).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -4.440030380246901).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 4.486471496440378).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -4.476147116038329).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -4.89701654221443).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 5.354091230723465).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -3.0747241437239694).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 3.0353275989376507).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -5.629287261948809).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 5.646667862671219).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -5.760627714067928).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 5.778122796662288).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -3.985782702743221).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 3.806742965245199).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -5.681609363423969).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 5.602262248819616).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -5.7141613785167875).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 5.747680286127327).on(cirq.GridQubit(7, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -9.272134780175643).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 9.311987288909458).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -2.4865845873665364).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 2.4890814068883764).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -2.4240781150731663).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 2.419398026235366).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 2.3861256785493166).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -2.392456163642626).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 10.821685325451792).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -10.785875071150537).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 12.703597923836748).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -12.7869629079138).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 12.184253063938954).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -12.108584830758572).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 3.782562501914174).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -3.873596611893716).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 4.772639843256901).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -4.771314675186062).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 8.49593730829863).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -8.479908941862229).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 10.137093854976465).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -10.128280753387683).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 1.639481743922408).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -1.9319083897827265).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 9.60223181672896).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -9.605639326034064).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 6.330499004273446).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -6.2177071019033425).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 9.851852381617888).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -9.926465199012979).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 6.431104618355057).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -6.38660616379351).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -7.792071921009969).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 8.097358555271011).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -4.453064758242544).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 4.646094149860723).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -6.763306761471101).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 6.721685791226169).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -6.633345575529405).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 6.640976196126138).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5423469235530667, phi=0.5388088498512879).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.5684106752459124, phi=0.5414007317481024).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.6152322695478165, phi=0.5160697976136035).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5040835324508275, phi=0.6761565725975858).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5144175462386844, phi=0.4680444728781228).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.4668587973263782, phi=0.4976074601121169).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.47511091993527, phi=0.538612093835262).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.603651215218248, phi=0.46649538437100246).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.6160334279232749, phi=0.4353897326147861).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5909523830878005, phi=0.5244700889486827).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.3600051446284807, phi=0.8279317402937687).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.2635580943707443, phi=0.3315124918059815).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5245711693927642, phi=0.4838906581970925).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5542388360689805, phi=0.5186534637665338).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5109427139358562, phi=0.4939388316289224).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.57896484905089, phi=0.5081656554152614).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5287198766338426, phi=0.5026095497404074).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.5377964198555438, phi=0.4705476574089381).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.501781688539034, phi=0.46799927805932284).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.576106529022596, phi=0.5431425261570397).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 9.460207801277338).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -9.420355292543523).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 2.557874433792943).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -2.555377614271102).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 1.9789952328325573).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -1.9836753216703575).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -2.805807436079691).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 2.7994769509863815).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -9.972491731044423).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 10.00830198534568).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -12.477250219528523).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 12.39388523545147).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -11.31088974563283).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 11.386557978813212).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -5.4898636407973544).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 5.398829530817813).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -5.863871460773714).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 5.8651966288445525).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -8.850693052252502).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 8.866721418688904).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -10.000141180758883).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 10.008954282347664).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -2.40381552479658).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 2.1113888789362614).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -10.03456101076628).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 10.031153501461176).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -5.434421382024706).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 5.54721328439481).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -9.17988634353845).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 9.10527352614336).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -6.5670035038476025).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 6.61150195840915).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 7.3504318409498035).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -7.045145206688761).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 4.8547834958469975).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -4.6617541042288195).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 7.956630846615096).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -7.998251816860028).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 7.8139063343273065).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -7.806275713730574).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -4.192816222527567).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 4.096517331211689).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -13.031870303178678).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 12.995691840749963).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 5.381139169744492).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -5.426527436528915).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -6.86899750135751).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 6.428483778485565).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -8.1318841157307).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 8.169013023671415).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 5.16073733770325).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -5.068929415695599).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.7176740888019262).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.7099714261238419).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -5.160288749920498).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 5.163401833175665).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -4.694750980814187).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 4.664493259768636).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -4.701251133883051).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 4.82245467467519).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 3.5368943862129347).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -3.523381665113022).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -1.113423877718808).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 1.1694659583609144).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -3.587134633961795).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 3.6604070451845887).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 1.3734003009778666).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -1.2391730694242633).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -5.2921262439699195).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 5.250682918720053).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -6.349327548997941).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 6.3741432050833).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 5.200761800851288).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -5.610666771277345).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -7.486795435376533).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 7.578281937389579).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -3.5483605148308843).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 3.464241645468862).on(cirq.GridQubit(7, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.545844435173598, phi=0.5163254336997252).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5033136051987404, phi=0.5501439149572028).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5930079664614663, phi=0.5355369376884288).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.59182423935832, phi=-5.773664463980115).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5886126292316385, phi=0.4838919055156303).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.5862983338115253, phi=0.5200148508319427).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5286450573669954, phi=0.5113953905811602).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.4887741478969256, phi=0.7140224757490621).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.565622495548066, phi=0.5127256481964074).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5289739216684795, phi=0.5055240639761313).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5384796865621224, phi=0.5293381306162406).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.4727562833004122, phi=0.4552443293379814).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5346175385256955, phi=0.5131039467233695).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.558221035096814, phi=0.4293113178636455).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5169062231051558, phi=0.46319906116805815).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5705414623224259, phi=0.4791699064049766).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.2445075810671158, phi=0.36440873167184756).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5516764540193888, phi=0.505545707839895).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5699606675525557, phi=0.48292170263262457).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 5.1050424650348445).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -5.201341356350722).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 12.332310550447476).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -12.36848901287619).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -4.910070555108823).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 4.864682288324399).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 7.534356038389369).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -7.974869761261314).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 7.00341426989382).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -6.966285361953106).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -5.556214577494324).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 5.648022499501975).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 1.3199079899133674).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -1.3276106525914517).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 4.848027141659483).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -4.844914058404317).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 4.932337110122265).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -4.9625948311678165).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 4.499075778124728).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -4.37787223733259).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -5.325823706765988).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 5.3393364278658995).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 1.682829500938578).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -1.6267874202964716).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 3.305341949396799).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -3.232069538174005).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -1.5571453827247277).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 1.691372614278331).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 5.3550627118441145).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -5.39650603709398).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 8.163182357684818).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -8.138366701599459).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -5.910214923947206).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 5.500309953521149).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 7.345311792027093).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -7.253825290014047).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 4.260694186099879).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -4.344813055461901).on(cirq.GridQubit(7, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -5.865975624866123).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 5.912958427369866).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -17.867868884042345).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 17.87049728934488).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -17.622485552499665).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 17.602988862096296).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 11.206366769065067).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -11.499232369531354).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 7.565359127187911).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -7.506809626368408).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -15.28470806725993).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 15.329888267898626).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 9.27528847613456).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -9.250287607594759).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -14.50235236667596).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 14.544090864144218).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 7.019954522972137).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -7.066266520580219).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -13.842047663366333).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 13.881335880513822).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 11.63394778862718).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -11.635951171927823).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -7.765941989655391).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 7.786825603456883).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 3.001137480344569).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -2.8980279413275123).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 5.563573798571002).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -5.8504123921354285).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 5.509227495500649).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -5.792084333301517).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 7.868086032823645).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -7.793090130850194).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -16.218582817568983).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 16.299782783273404).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 4.3863074183418185).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -4.487034178043276).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -18.307962526439212).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 18.30455172905699).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 5.704655903613886).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -5.737595034198219).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5454967174552687, phi=0.5074540278986153).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.5233234922971755, phi=0.6681144400379464).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5644541080112795, phi=0.5439498075085039).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5866139110090092, phi=0.5693597810559818).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.2947043217999283, phi=0.4859467238431821).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.541977006124425, phi=0.6073798124875975).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5573072833358306, phi=0.5415514987622351).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5345751514593928, phi=0.472462117170605).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.5138652502397498, phi=0.47710618607286504).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5849169442855044, phi=0.54346233613361).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5317226133698079, phi=0.6723463192657011).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4838884067961586, phi=0.5070681071136852).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5398075246432927, phi=0.5174515645943538).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4593314109380113, phi=0.5230636172671492).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.4902099797510393, phi=0.4552057582549894).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5376836849431186, phi=0.46265685930712236).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.555185434982808, phi=0.6056351386305033).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.4749003996237158, phi=0.4353609222411594).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5249018931362641, phi=0.7521905394129447).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.4908753240086248, phi=0.47848614251537785).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 5.477287511969221).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -5.430304709465478).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 18.225856052586064).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -18.223227647283533).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 17.655139057028).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -17.674635747431363).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -10.591776080470469).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 10.298910480004182).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -7.378072351850649).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 7.436621852670151).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 15.852199817881967).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -15.80701961724327).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -9.090152260365358).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 9.11515312890516).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 13.700045044703652).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -13.658306547235396).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -7.538336273583833).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 7.492024275975751).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 13.968508849527241).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -13.929220632379753).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -10.93468592917129).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 10.932682545870646).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 6.861064422304347).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -6.840180808502855).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -3.771658529535837).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 3.874768068552894).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -5.593307215154117).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 5.30646862158969).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -3.800913502275713).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 3.5180566644748446).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -7.9036364710757425).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 7.978632373049194).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 17.0915408373009).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -17.01034087159648).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -4.825583222537869).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 4.724856462836412).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 18.198255473178417).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -18.201666270560644).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -4.619948691499696).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 4.587009560915362).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 8.044385426555426).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -8.083380595470867).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -5.783380074002775).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 5.546523606048641).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -16.574223110662086).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 16.60431588336404).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -15.816295096608934).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 15.811833422443211).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -13.3598687747566).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 13.249156584109453).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -4.127807240413703).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 4.082519238690215).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -5.421612643757122).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 5.42765340313407).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -21.179392694559272).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 21.166389776352954).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -13.252932498710596).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 13.24022142293596).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -8.162692838556204).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 8.223006443218978).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -12.938755870544817).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 12.965256899048683).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -12.724144773112773).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 12.73446915351482).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 11.027652291347495).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -10.570577602838458).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 7.6694399461790255).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -7.7088364909653455).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 17.082146626922658).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -17.06476602620025).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 14.58087327851535).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -14.563378195920992).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 10.871739079510629).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -11.050778817008649).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 14.00817849447214).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -14.087525609076494).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 13.245133511743317).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -13.211614604132775).on(cirq.GridQubit(7, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4937034321050129, phi=0.5388459463555662).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5015413274420961, phi=0.51076415920643).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.505206014385737, phi=0.5177720559789512).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5588791081427968, phi=0.559649620487243).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5907035825834708, phi=0.5678223287662552).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5296321276792553, phi=0.537761951313038).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.619276265426104, phi=0.48310297196088736).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.6116663075637374, phi=0.5343172366969327).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.5306030283605572, phi=0.5257102080843467).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.589821065740506, phi=0.5045391214115686).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5472406430590444, phi=0.5216932173558055).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5124128267683938, phi=0.5133142626030278).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5707871303628709, phi=0.5176678491729374).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5337916352034444, phi=0.5123546847230711).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.596346344028619, phi=0.5104319949477776).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.53597466118183, phi=0.5584919013659856).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.385350861888917, phi=0.5757363921651084).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.614843449053755, phi=0.5542252229839564).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.505922331941178, phi=0.4892027060568212).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -8.908246745659781).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 8.869251576744341).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 6.283590676347165).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -6.520447144301299).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 17.259444062298133).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -17.229351289596174).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 16.126615138480055).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -16.131076812645777).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 14.142506057270092).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -14.253218247917241).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 4.924729485113265).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -4.9700174868367535).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 6.6580043579049155).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -6.651963598527967).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 21.61248038813089).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -21.625483306337212).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 12.581705877923879).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -12.594416953698515).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 7.826508725663096).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -7.7661951210003215).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 12.014531408750791).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -11.988030380246926).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 11.590471496440383).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -11.580147116038336).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -11.55701654221442).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 12.014091230723457).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -7.662724143723925).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 7.623327598937605).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -15.693287261948884).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 15.710667862671292).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -14.640627714067872).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 14.658122796662232).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -10.271185992592658).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 10.092146255094638).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -14.265609363423946).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 14.186262248819594).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -13.558161378516775).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 13.591680286127318).on(cirq.GridQubit(7, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -19.484134780175637).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 19.523987288909453).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -4.706584587366488).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 4.709081406888329).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -4.644078115073251).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 4.639398026235451).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 4.902125678549236).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -4.908456163642546).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 21.92168532545182).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -21.88587507115056).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 26.023597923836856).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -26.106962907913907).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 25.356253063938887).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -25.2805848307585).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 8.370562501914259).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -8.461596611893802).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 10.100639843256841).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -10.099314675186001).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 18.263937308298605).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -18.247908941862203).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 21.53309385497646).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -21.524280753387675).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 4.303481743922509).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -4.595908389782827).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 20.40623181672889).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -20.409639326033993).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 13.138499004273484).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -13.02570710190338).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 19.994449091768548).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -20.069061909163636).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 13.831104618355031).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -13.786606163793484).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -15.932071921009928).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 16.237358555270973).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -9.485064758242517).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 9.678094149860694).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -15.051306761471112).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 15.009685791226179).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -14.181345575529425).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 14.188976196126161).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5423469235530667, phi=0.5388088498512879).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.5684106752459124, phi=0.5414007317481024).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.6152322695478165, phi=0.5160697976136035).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5040835324508275, phi=0.6761565725975858).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5144175462386844, phi=0.4680444728781228).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.4668587973263782, phi=0.4976074601121169).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.47511091993527, phi=0.538612093835262).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.603651215218248, phi=0.46649538437100246).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.6160334279232749, phi=0.4353897326147861).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5909523830878005, phi=0.5244700889486827).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.3600051446284807, phi=0.8279317402937687).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.2635580943707443, phi=0.3315124918059815).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5245711693927642, phi=0.4838906581970925).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5542388360689805, phi=0.5186534637665338).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5109427139358562, phi=0.4939388316289224).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.57896484905089, phi=0.5081656554152614).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5287198766338426, phi=0.5026095497404074).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.5377964198555438, phi=0.4705476574089381).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.501781688539034, phi=0.46799927805932284).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.576106529022596, phi=0.5431425261570397).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 19.672207801277334).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -19.632355292543515).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 4.777874433792896).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -4.775377614271054).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 4.198995232832642).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -4.203675321670441).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -5.321807436079611).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 5.315476950986302).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -21.072491731044448).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 21.1083019853457).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -25.79725021952863).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 25.713885235451578).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -24.48288974563276).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 24.55855797881315).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -10.07786364079744).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 9.986829530817898).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -11.191871460773655).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 11.193196628844492).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -18.61869305225248).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 18.63472141868888).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -21.396141180758875).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 21.404954282347656).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -5.067815524796681).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 4.775388878936363).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -20.83856101076621).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 20.835153501461107).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -12.242421382024746).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 12.35521328439485).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -19.32248305368911).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 19.24787023629402).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -13.967003503847575).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 14.01150195840912).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 15.49043184094976).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -15.185145206688718).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 9.886783495846968).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -9.693754104228791).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 16.244630846615102).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -16.286251816860037).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 15.361906334327331).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -15.354275713730596).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -8.040816222527539).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 7.944517331211661).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -23.983870303178655).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 23.947691840749943).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 9.52513916974456).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -9.570527436528984).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -13.084997501357485).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 12.644483778485537).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -14.199884115730756).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 14.23701302367147).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 10.044737337703173).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -9.952929415695523).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -1.4576740888019104).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 1.4499714261238263).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -9.600288749920535).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 9.603401833175703).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -8.542750980814159).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 8.512493259768608).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -8.401251133882973).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 8.52245467467511).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 7.236894386212986).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -7.223381665113074).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -2.0014238777188416).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 2.057465958360948).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -6.843134633961698).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 6.916407045184491).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 3.0014003009778842).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -2.8671730694242803).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -10.176126243969842).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 10.134682918719976).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -12.347924259148533).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 12.372739915233888).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 9.936761800851292).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -10.346666771277349).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -13.554795435376587).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 13.646281937389634).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -7.248360514830936).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 7.1642416454689135).on(cirq.GridQubit(7, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.545844435173598, phi=0.5163254336997252).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5033136051987404, phi=0.5501439149572028).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5930079664614663, phi=0.5355369376884288).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.59182423935832, phi=-5.773664463980115).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5886126292316385, phi=0.4838919055156303).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.5862983338115253, phi=0.5200148508319427).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5286450573669954, phi=0.5113953905811602).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.4887741478969256, phi=0.7140224757490621).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.565622495548066, phi=0.5127256481964074).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5289739216684795, phi=0.5055240639761313).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5384796865621224, phi=0.5293381306162406).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.4727562833004122, phi=0.4552443293379814).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5346175385256955, phi=0.5131039467233695).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.558221035096814, phi=0.4293113178636455).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5169062231051558, phi=0.46319906116805815).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5705414623224259, phi=0.4791699064049766).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.2445075810671158, phi=0.36440873167184756).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5516764540193888, phi=0.505545707839895).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5699606675525557, phi=0.48292170263262457).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 8.953042465034816).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -9.049341356350693).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 23.28431055044745).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -23.320489012876163).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -9.054070555108892).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 9.008682288324469).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 13.750356038389338).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -14.190869761261286).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 13.071414269893877).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -13.034285361953161).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -10.440214577494247).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 10.5320224995019).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 2.0599079899133517).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -2.067610652591436).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 9.288027141659521).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -9.284914058404354).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 8.780337110122234).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -8.810594831167785).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 8.199075778124648).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -8.07787223733251).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -9.025823706766039).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 9.039336427865951).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 2.570829500938612).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -2.5147874202965053).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 6.561341949396702).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -6.48806953817391).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -3.1851453827247447).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 3.3193726142783486).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 10.239062711844038).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -10.280506037093904).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 14.161779067835406).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -14.136963411750049).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -10.646214923947209).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 10.236309953521156).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 13.413311792027148).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -13.3218252900141).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 7.960694186099931).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -8.044813055461953).on(cirq.GridQubit(7, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -9.713975624866094).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 9.760958427369838).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -30.29986888404229).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 30.302497289344824).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -30.054485552499738).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 30.034988862096366).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 19.050366769065057).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -19.343232369531343).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 12.597359127188014).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -12.538809626368511).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -26.08870806725985).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 26.13388826789855).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 15.787288476134503).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -15.762287607594697).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -24.12235236667589).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 24.164090864144143).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 11.90395452297206).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -11.950266520580142).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -23.906047663366408).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 23.945335880513902).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 19.77394778862714).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -19.77595117192778).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -12.64994198965531).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 12.670825603456805).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 5.221137480344522).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -5.118027941327464).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 9.263573798570924).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -9.55041239213535).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 8.765227495500554).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -9.048084333301423).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 13.422682742974219).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -13.34768684100077).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -28.058582817569).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 28.139782783273418).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 7.346307418341885).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -7.447034178043343).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -30.887962526439214).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 30.884551729056984).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 9.404655903613937).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -9.437595034198273).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5454967174552687, phi=0.5074540278986153).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.5233234922971755, phi=0.6681144400379464).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5644541080112795, phi=0.5439498075085039).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5866139110090092, phi=0.5693597810559818).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.2947043217999283, phi=0.4859467238431821).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.541977006124425, phi=0.6073798124875975).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5573072833358306, phi=0.5415514987622351).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5345751514593928, phi=0.472462117170605).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.5138652502397498, phi=0.47710618607286504).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5849169442855044, phi=0.54346233613361).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5317226133698079, phi=0.6723463192657011).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4838884067961586, phi=0.5070681071136852).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5398075246432927, phi=0.5174515645943538).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4593314109380113, phi=0.5230636172671492).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.4902099797510393, phi=0.4552057582549894).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5376836849431186, phi=0.46265685930712236).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.555185434982808, phi=0.6056351386305033).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.4749003996237158, phi=0.4353609222411594).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5249018931362641, phi=0.7521905394129447).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.4908753240086248, phi=0.47848614251537785).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 9.325287511969192).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -9.278304709465448).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 30.657856052586013).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -30.65522764728348).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 30.087139057028068).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -30.106635747431437).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -18.435776080470458).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 18.142910480004172).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -12.410072351850753).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 12.468621852670255).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 26.656199817881895).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -26.611019617243198).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -15.602152260365296).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 15.627153128905102).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 23.32004504470358).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -23.27830654723533).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -12.422336273583753).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 12.376024275975672).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 24.032508849527318).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -23.993220632379824).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -19.074685929171245).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 19.072682545870606).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 11.745064422304269).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -11.724180808502775).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -5.991658529535789).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 6.094768068552847).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -9.293307215154037).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 9.006468621589612).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -7.056913502275617).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 6.774056664474749).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -13.45823318122632).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 13.53322908319977).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 28.931540837300908).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -28.850340871596494).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -7.785583222537938).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 7.68485646283648).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 30.77825547317841).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -30.781666270560642).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -8.319948691499748).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 8.287009560915415).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 13.22438542655545).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -13.26338059547089).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -9.187380074002728).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 8.950523606048595).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -26.934223110661993).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 26.964315883363945).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -25.436295096608994).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 25.43183342244327).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -21.351868774756507).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 21.24115658410936).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -6.643807240413623).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 6.598519238690134).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -9.269612643757092).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 9.27565340313404).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -33.75939269455927).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 33.74638977635295).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -21.096932498710586).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 21.084221422935954).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -13.046692838556257).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 13.107006443219033).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -20.486755870544844).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 20.51325689904871).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -19.82814477311278).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 19.838469153514826).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 17.687652291347487).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -17.230577602838448).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 12.257439946178984).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -12.296836490965301).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 27.146146626922736).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -27.128766026200324).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 23.46087327851529).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -23.443378195920936).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 17.157142369360066).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -17.33618210685809).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 22.592178494472112).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -22.671525609076465).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 21.089133511743302).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -21.055614604132767).on(cirq.GridQubit(7, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4937034321050129, phi=0.5388459463555662).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5015413274420961, phi=0.51076415920643).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.505206014385737, phi=0.5177720559789512).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5588791081427968, phi=0.559649620487243).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5907035825834708, phi=0.5678223287662552).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5296321276792553, phi=0.537761951313038).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.619276265426104, phi=0.48310297196088736).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.6116663075637374, phi=0.5343172366969327).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.5306030283605572, phi=0.5257102080843467).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.589821065740506, phi=0.5045391214115686).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5472406430590444, phi=0.5216932173558055).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5124128267683938, phi=0.5133142626030278).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5707871303628709, phi=0.5176678491729374).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5337916352034444, phi=0.5123546847230711).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.596346344028619, phi=0.5104319949477776).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.53597466118183, phi=0.5584919013659856).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.385350861888917, phi=0.5757363921651084).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.614843449053755, phi=0.5542252229839564).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.505922331941178, phi=0.4892027060568212).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -14.088246745659802).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 14.049251576744364).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 9.687590676347119).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -9.924447144301253).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 27.61944406229804).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -27.589351289596088).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 25.746615138480117).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -25.75107681264584).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 22.13450605727).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -22.245218247917148).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 7.440729485113184).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -7.486017486836674).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 10.506004357904885).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -10.499963598527936).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 34.19248038813088).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -34.20548330633721).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 20.425705877923868).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -20.4384169536985).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 12.71050872566315).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -12.650195121000372).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 19.562531408750814).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -19.53603038024695).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 18.69447149644039).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -18.684147116038343).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -18.21701654221441).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 18.674091230723448).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -12.250724143723879).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 12.21132759893756).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -25.757287261948953).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 25.774667862671368).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -23.52062771406781).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 23.538122796662165).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -16.556589282442097).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 16.377549544944078).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -22.849609363423916).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 22.770262248819563).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -21.402161378516766).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 21.435680286127305).on(cirq.GridQubit(7, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -29.696134780175626).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 29.735987288909445).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -6.926584587366442).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 6.929081406888282).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -6.864078115073335).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 6.859398026235534).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 7.418125678549155).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -7.424456163642465).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 33.02168532545184).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -32.98587507115059).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 39.34359792383697).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -39.42696290791402).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 38.52825306393881).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -38.452584830758425).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 12.958562501914345).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -13.049596611893888).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 15.428639843256777).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -15.42731467518594).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 28.031937308298577).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -28.01590894186218).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 32.92909385497645).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -32.92028075338767).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 6.967481743922609).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -7.259908389782927).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 31.210231816728815).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -31.213639326033913).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 19.946499004273523).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -19.833707101903418).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 30.137045801919207).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -30.211658619314296).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 21.231104618355).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -21.186606163793456).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -24.07207192100989).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 24.377358555270934).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -14.517064758242485).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 14.710094149860666).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -23.339306761471114).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 23.297685791226186).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -21.72934557552945).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 21.736976196126186).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5423469235530667, phi=0.5388088498512879).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.5684106752459124, phi=0.5414007317481024).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.6152322695478165, phi=0.5160697976136035).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5040835324508275, phi=0.6761565725975858).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5144175462386844, phi=0.4680444728781228).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.4668587973263782, phi=0.4976074601121169).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.47511091993527, phi=0.538612093835262).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.603651215218248, phi=0.46649538437100246).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.6160334279232749, phi=0.4353897326147861).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5909523830878005, phi=0.5244700889486827).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.3600051446284807, phi=0.8279317402937687).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.2635580943707443, phi=0.3315124918059815).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5245711693927642, phi=0.4838906581970925).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5542388360689805, phi=0.5186534637665338).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5109427139358562, phi=0.4939388316289224).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.57896484905089, phi=0.5081656554152614).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5287198766338426, phi=0.5026095497404074).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.5377964198555438, phi=0.4705476574089381).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.501781688539034, phi=0.46799927805932284).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.576106529022596, phi=0.5431425261570397).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 29.884207801277327).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -29.844355292543508).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 6.997874433792849).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -6.995377614271008).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 6.418995232832726).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -6.423675321670527).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -7.8378074360795305).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 7.831476950986221).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -32.172491731044474).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 32.20830198534573).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -39.11725021952874).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 39.03388523545169).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -37.65488974563269).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 37.730557978813074).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -14.665863640797525).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 14.574829530817984).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -16.519871460773594).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 16.52119662884443).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -28.386693052252454).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 28.402721418688852).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -32.79214118075887).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 32.800954282347654).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -7.731815524796781).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 7.439388878936463).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -31.64256101076613).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 31.63915350146103).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -19.050421382024783).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 19.16321328439489).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -29.465079763839764).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 29.390466946444676).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -21.367003503847553).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 21.411501958409097).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 23.630431840949722).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -23.32514520668868).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 14.918783495846942).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -14.725754104228761).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 24.532630846615117).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -24.574251816860045).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 22.909906334327353).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -22.902275713730617).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -11.88881622252751).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 11.792517331211629).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -34.93587030317863).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 34.899691840749924).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 13.66913916974463).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -13.714527436529053).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -19.300997501357458).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 18.86048377848551).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -20.26788411573081).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 20.30501302367152).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 14.928737337703097).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -14.836929415695444).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -2.1976740888018944).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 2.1899714261238103).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -14.040288749920572).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 14.043401833175738).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -12.39075098081413).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 12.360493259768578).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -12.10125113388289).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 12.22245467467503).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 10.936894386213037).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -10.923381665113125).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -2.8894238777188748).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 2.945465958360982).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -10.099134633961603).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 10.172407045184396).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 4.629400300977903).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -4.495173069424299).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -15.060126243969762).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 15.018682918719897).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -18.34652096929912).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 18.371336625384476).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 14.672761800851296).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -15.082666771277351).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -19.622795435376638).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 19.714281937389686).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -10.948360514830984).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 10.864241645468965).on(cirq.GridQubit(7, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.545844435173598, phi=0.5163254336997252).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5033136051987404, phi=0.5501439149572028).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5930079664614663, phi=0.5355369376884288).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.59182423935832, phi=-5.773664463980115).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5886126292316385, phi=0.4838919055156303).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.5862983338115253, phi=0.5200148508319427).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5286450573669954, phi=0.5113953905811602).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.4887741478969256, phi=0.7140224757490621).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.565622495548066, phi=0.5127256481964074).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5289739216684795, phi=0.5055240639761313).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5384796865621224, phi=0.5293381306162406).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.4727562833004122, phi=0.4552443293379814).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5346175385256955, phi=0.5131039467233695).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.558221035096814, phi=0.4293113178636455).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5169062231051558, phi=0.46319906116805815).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5705414623224259, phi=0.4791699064049766).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.2445075810671158, phi=0.36440873167184756).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5516764540193888, phi=0.505545707839895).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5699606675525557, phi=0.48292170263262457).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 12.801042465034786).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -12.897341356350665).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 34.236310550447435).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -34.27248901287614).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -13.19807055510896).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 13.152682288324536).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 19.96635603838931).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -20.40686976126126).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 19.13941426989393).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -19.102285361953214).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -15.32421457749417).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 15.416022499501823).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 2.7999079899133363).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -2.80761065259142).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 13.728027141659558).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -13.724914058404392).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 12.628337110122207).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -12.658594831167758).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 11.899075778124569).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -11.777872237332431).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -12.725823706766091).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 12.739336427866004).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 3.458829500938646).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -3.4027874202965385).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 9.817341949396608).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -9.744069538173814).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -4.8131453827247626).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 4.9473726142783665).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 15.12306271184396).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -15.164506037093826).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 20.160375777985994).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -20.13556012190064).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -15.382214923947213).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 14.972309953521158).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 19.481311792027203).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -19.389825290014155).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 11.660694186099983).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -11.744813055462004).on(cirq.GridQubit(7, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -13.561975624866065).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 13.608958427369807).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -42.731868884042235).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 42.73449728934477).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -42.48648555249982).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 42.46698886209646).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 26.894366769065044).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -27.18723236953133).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 17.629359127188117).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -17.570809626368614).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -36.89270806725978).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 36.93788826789848).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 22.299288476134443).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -22.274287607594637).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -33.74235236667582).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 33.78409086414407).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 16.787954522971983).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -16.834266520580062).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -33.970047663366486).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 34.00933588051398).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 27.913947788627098).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -27.915951171927734).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -17.533941989655233).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 17.554825603456727).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 7.441137480344476).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -7.338027941327417).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 12.963573798570843).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -13.250412392135269).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 12.021227495500458).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -12.30408433330133).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 18.97727945312479).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -18.902283551151342).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -39.89858281756901).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 39.97978278327343).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 10.306307418341955).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -10.407034178043412).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -43.46796252643921).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 43.46455172905698).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 13.104655903613988).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -13.137595034198322).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5454967174552687, phi=0.5074540278986153).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.5233234922971755, phi=0.6681144400379464).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5644541080112795, phi=0.5439498075085039).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5866139110090092, phi=0.5693597810559818).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.2947043217999283, phi=0.4859467238431821).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.541977006124425, phi=0.6073798124875975).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5573072833358306, phi=0.5415514987622351).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5345751514593928, phi=0.472462117170605).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.5138652502397498, phi=0.47710618607286504).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5849169442855044, phi=0.54346233613361).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5317226133698079, phi=0.6723463192657011).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4838884067961586, phi=0.5070681071136852).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5398075246432927, phi=0.5174515645943538).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4593314109380113, phi=0.5230636172671492).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.4902099797510393, phi=0.4552057582549894).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5376836849431186, phi=0.46265685930712236).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.555185434982808, phi=0.6056351386305033).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.4749003996237158, phi=0.4353609222411594).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5249018931362641, phi=0.7521905394129447).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.4908753240086248, phi=0.47848614251537785).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 13.17328751196916).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -13.126304709465419).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 43.08985605258596).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -43.08722764728342).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 42.51913905702814).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -42.53863574743151).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -26.279776080470445).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 25.98691048000416).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -17.442072351850854).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 17.500621852670356).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 37.46019981788182).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -37.415019617243125).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -22.114152260365234).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 22.13915312890504).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 32.9400450447035).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -32.89830654723525).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -17.306336273583675).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 17.260024275975592).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 34.09650884952739).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -34.057220632379895).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -27.214685929171196).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 27.21268254587056).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 16.629064422304193).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -16.6081808085027).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -8.211658529535743).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 8.3147680685528).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -12.993307215153958).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 12.706468621589535).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -10.31291350227552).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 10.030056664474653).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -19.012829891376892).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 19.08782579335034).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 40.77154083730092).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -40.690340871596504).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -10.745583222538006).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 10.644856462836547).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 43.358255473178396).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -43.361666270560626).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -12.0199486914998).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 11.987009560915467).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
            ]
        ),
    ]
)

