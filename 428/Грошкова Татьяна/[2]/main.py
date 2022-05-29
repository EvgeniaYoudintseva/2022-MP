import generator_simple.py
import generator_complex.py
import analyzer.py
import circut.py
print("Variant: 1")
from generator_simple import Generator_simple
from generator_complex import Generator_complex
from analyzer import Analyzer
from circuit import Circuit

fr=0.1
fr_0=5
time=500
Ampl=1
t_s=250
A=Generator_simple(fr,fr_0,time,Ampl)
y_new=[*A.signal_harm_generator(t_s)]
An=Analyzer(y_new,t_s,fr_0)
An.Graph(2)
An.Spectr()
An.Reverse_Fourier(1)
Am=Generator_complex(fr,y_new,time,fr_0,Ampl)
y_new=Am.envel()
An=Analyzer(y_new,t_s,fr_0)
An.Graph(3)
An.Disper(1)
An.Average(1)
An.Median(1)
An.Max(1)
An.Min(1)
An.Scope(1)
An.Spectr()
An.Reverse_Fourier(1)
Cir=Circuit(y_new,t_s,fr_0)
An=Analyzer(Cir.convol(),t_s,fr_0)
An.Graph(4)
An.Spectr()
y_nn=A.CreateSignal_saw(t_s)
An=Analyzer(y_nn,t_s,fr_0)
An.Graph(5)
An.Spectr()
An.Reverse_Fourier(1)
Am=Generator_complex(fr,y_nn,t_s,fr_0,Ampl)
y_nn=Am.envelope()
An=Analyzer(y_nn,t_s,fr_0)
An.Graph(6)
An.Disper(1)
An.Average(1)
An.Median(1)
An.Max(1)
An.Min(1)
An.Scope(1)
An.Spectr()
An.Reverse_Fourier(1)
y_nnn=A.Signal_triag(t_s)
An=Analyzer(y_nnn,t_s,fr_0)
An.Graph(7)
An.Spectr()
y_nnnn=A.Signal_SHIM(t_s,30)
An=Analyzer(y_nnnn,t_s,fr_0)
An.Graph(8)
An.Spectr()
print(Am.get_sample_time(10), " Am.get_sample_time")
print(Am.get_sample_n(10), " Am.get_sample_n")
print([*(A.generator(30))], "A.generator")
print([*(Am.generator(30))], "Am.generator")
print(*Cir.Return_Gener(), "=cir.return_gener")