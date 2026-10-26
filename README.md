# Register Allocator

A Python implementation of a register allocator that maps virtual registers to a limited number of physical registers.

## Features
- Analyzes virtual register usage and live ranges
- Assigns available physical registers
- Implements register spilling when registers are exhausted
- Inserts memory load/store instructions for spilled values
- Rewrites instructions using allocated registers

## Usage
```bash
python3 alloc.py <register_count> <input_file> <output_file>
```

## Purpose
Explores compiler design concepts, register allocation, instruction rewriting, and memory management at the assembly level.
