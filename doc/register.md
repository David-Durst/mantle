### Registers and Flip-Flops

### Registers

Like all state-ful circuits,
registers have optional inputs that control the state.
These inputs incude the clock (`CLK:In(Clock)`),
the clock enable (`CE:In(Bit)`),
the reset (`RESET:In(Bit)`),
and
the set (`SET:In(Bit)`),
The clock enable, reset and set are optional,
and are controlled by the flags
`has_ce`, `has_reset`, and `has_set`.

Returns an n-bit register of type `T`.
```
# Register :: I:In(T(n)), O:Out(T(n))
Register(n, init=0, has_ce=False, has_reset=False, has_set=False, T=Bits)
```

### Flip-Flops

Mantle includes many of the standard types of flip-flops.

```
# DFF :: I:In(Bit), O:Out(Bit)
DFF(init=0, has_ce=False, has_reset=False, has_set=False)
```

Set-Reset Flip-Flop
```
# SRFF :: S:In(Bit), R:In(Bit), O:Out(Bit)
SRFF(init=0, has_ce=False)
```

Reset-Set Flip-Flop
```
# RSFF :: R:In(Bit), S:In(Bit), O:Out(Bit)
RSFF(init=0, has_ce=False)
```

JK Flip-Flop
```
# JKFF :: J:In(Bit), K:In(Bit), O:Out(Bit)
JKFF(init=0, has_ce=False, has_reset=False, has_set=False)
```

Toggle Flip-Flop
```
# TFF :: I:In(Bit), O:Out(Bit)
TFF(init=0, has_ce=False, has_reset=False, has_set=False)
```
If `I` is true, toggle the flip-flop.


There is also a utility function to create a list of n `DFF`s

```
FFs(n, init=0, has_ce=False, has_reset=False, has_set=False)
```



