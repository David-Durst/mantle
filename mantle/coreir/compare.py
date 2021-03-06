from magma import *
from magma.bit_vector import BitVector 
from .arith import declare_binop, get_length
from .logic import not_, XOr
import operator


def DefineCoreirEq(width):
    def simulate(self, value_store, state_store):
        in0 = BitVector(value_store.get_value(self.in0))
        in1 = BitVector(value_store.get_value(self.in1))
        out = operator.eq(in0, in1).as_bool_list()[0]
        value_store.set_value(self.out, out)
    if width is None:
        circ = DefineCircuit('corebit_eq', 'in0', In(Bit), 'in1', In(Bit), 'out', Out(Bit))
        wire(circ.out, not_(XOr(2, None)(circ.in0, circ.in1)))
        EndDefine()
        return circ
    else:
        T = Bits(width)
        return DeclareCircuit("coreir_eq_{}".format(width),
                              'in0', In(T), 'in1', In(T),
                              'out', Out(Bit),
                              stateful=False,
                              simulate=simulate,
                              verilog_name="coreir_eq",
                              coreir_name="eq",
                              coreir_lib = "coreir",
                              coreir_genargs={"width": width})


@cache_definition
def DefineEQ(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("EQ{}".format(n), *IO)
    coreir_eq = DefineCoreirEq(n)()
    wire(circ.I0, coreir_eq.in0)
    wire(circ.I1, coreir_eq.in1)
    wire(coreir_eq.out, circ.O)
    EndDefine()
    return circ

def EQ(n, **kwargs):
    return DefineEQ(n)(**kwargs)


DefineCoreirNeq = declare_binop("neq", operator.ne, out_type=Bit)

@cache_definition
def DefineNE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    circ = DefineCircuit("NE{}".format(n),
        "I0", In(T), "I1", In(T), "O", Out(Bit))
    eq = EQ(n)
    out = not_(eq(circ.I0, circ.I1))
    wire(out, circ.O)
    EndDefine()
    return circ

def NE(n, **kwargs):
    return DefineNE(n)(**kwargs)


DefineCoreirUlt = declare_binop("ult", operator.lt, out_type=Bit)


@cache_definition
def DefineULT(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("ULT{}".format(n), *IO)
    coreir_ult = DefineCoreirUlt(n, Bits)()
    wire(circ.I0, coreir_ult.in0)
    wire(circ.I1, coreir_ult.in1)
    wire(coreir_ult.out, circ.O)
    EndDefine()
    return circ

def ULT(n, **kwargs):
    return DefineULT(n)(**kwargs)


DefineCoreirUle = declare_binop("ule", operator.le, out_type=Bit)


@cache_definition
def DefineULE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("ULE{}".format(n), *IO)
    coreir_ule = DefineCoreirUle(n, Bits)()
    wire(circ.I0, coreir_ule.in0)
    wire(circ.I1, coreir_ule.in1)
    wire(coreir_ule.out, circ.O)
    EndDefine()
    return circ

def ULE(n, **kwargs):
    return DefineULE(n)(**kwargs)


DefineCoreirUgt = declare_binop("ugt", operator.lt, out_type=Bit)


@cache_definition
def DefineUGT(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("UGT{}".format(n), *IO)
    coreir_ugt = DefineCoreirUgt(n, Bits)()
    wire(circ.I0, coreir_ugt.in0)
    wire(circ.I1, coreir_ugt.in1)
    wire(coreir_ugt.out, circ.O)
    EndDefine()
    return circ

def UGT(n, **kwargs):
    return DefineUGT(n)(**kwargs)


DefineCoreirUge = declare_binop("uge", operator.le, out_type=Bit)


@cache_definition
def DefineUGE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("UGE{}".format(n), *IO)
    coreir_uge = DefineCoreirUge(n, Bits)()
    wire(circ.I0, coreir_uge.in0)
    wire(circ.I1, coreir_uge.in1)
    wire(coreir_uge.out, circ.O)
    EndDefine()
    return circ

def UGE(n, **kwargs):
    return DefineUGE(n)(**kwargs)


DefineCoreirSlt = declare_binop("slt", operator.lt, out_type=Bit)


@cache_definition
def DefineSLT(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("SLT{}".format(n), *IO)
    coreir_slt = DefineCoreirSlt(n, Bits)()
    wire(circ.I0, coreir_slt.in0)
    wire(circ.I1, coreir_slt.in1)
    wire(coreir_slt.out, circ.O)
    EndDefine()
    return circ

def SLT(n, **kwargs):
    return DefineSLT(n)(**kwargs)


DefineCoreirSle = declare_binop("sle", operator.le, out_type=Bit)


@cache_definition
def DefineSLE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("SLE{}".format(n), *IO)
    coreir_sle = DefineCoreirSle(n, Bits)()
    wire(circ.I0, coreir_sle.in0)
    wire(circ.I1, coreir_sle.in1)
    wire(coreir_sle.out, circ.O)
    EndDefine()
    return circ

def SLE(n, **kwargs):
    return DefineSLE(n)(**kwargs)


DefineCoreirSgt = declare_binop("sgt", operator.lt, out_type=Bit)


@cache_definition
def DefineSGT(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("SGT{}".format(n), *IO)
    coreir_sgt = DefineCoreirSgt(n, Bits)()
    wire(circ.I0, coreir_sgt.in0)
    wire(circ.I1, coreir_sgt.in1)
    wire(coreir_sgt.out, circ.O)
    EndDefine()
    return circ

def SGT(n, **kwargs):
    return DefineSGT(n)(**kwargs)


DefineCoreirSge = declare_binop("sge", operator.le, out_type=Bit)


@cache_definition
def DefineSGE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("SGE{}".format(n), *IO)
    coreir_sge = DefineCoreirSge(n, Bits)()
    wire(circ.I0, coreir_sge.in0)
    wire(circ.I1, coreir_sge.in1)
    wire(coreir_sge.out, circ.O)
    EndDefine()
    return circ

def SGE(n, **kwargs):
    return DefineSGE(n)(**kwargs)
