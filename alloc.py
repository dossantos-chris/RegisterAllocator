import sys
import re

reg_num = int(sys.argv[1])
input_file = open(sys.argv[2], "r")
lines = input_file.readlines()
output_file = open(sys.argv[3], "w")


allocator = {}
max_lives = {}
spilling_address = 1020
physical_registers = []
feasible_registers = []
memory = []
new_lines = []

for i in range(0, reg_num-1):
    physical_registers.append("z" + str(i))
feasible_registers.append("z" + str(reg_num-1))
#Finding out the max lives of the virtual registers
line_num = 0
for line in lines:
    line_num += 1
    if "=>" in line:
        pattern = r"r\d+"
        regs = re.findall(pattern, line)
        keys = list(max_lives.keys())

        for reg in regs:
            if reg not in keys:
                max_lives.update({reg: (line_num, line_num)})
            else:
                max_lives.update({reg: (max_lives.get(reg)[0], line_num)})
print(max_lives)
line_num = 0
for line in lines:
    line_num += 1
    if "=>" in line:
        pattern = r"r\d+"
        regs = re.findall(pattern, line)
        print(regs)
        for reg in regs:
            values = list(allocator.values())
            keys = list(allocator.keys())
            #Check if the register is loaded in the allocator
            if reg not in values:
                #Check if there are any free registers
                if len(keys) < reg_num-1:
                    allocator.update({physical_registers[len(keys)]: reg})

                #If not, you need to replace one
                else:
                    replaced = False
                    spilled = False
                    replace = -1
                    i = -1
                    #If a virtual register is finished, replace it
                    for value in values:
                        i += 1
                        if max_lives.get(value)[1] < line_num:
                            replaced = True
                            replace = i
                            allocator.update({physical_registers[replace]: reg})
                            break

                    #If no virtual registers are finished, spill the register whose last use is farthest in the future
                    if not replaced:
                        i = -1
                        furthest = "temp"
                        for value in values:
                            i += 1
                            if value not in regs:
                                furthest = values[i]
                                break
                        replace = i
                        print(values)
                        print(furthest)
                        print(i)
                        for value in values[i+1:]:
                            i += 1
                            if value not in regs:
                                if max_lives.get(furthest)[1] <= max_lives.get(value)[1]:
                                    print(value)
                                    furthest = value
                                    replace = i
                        #Insert spill code
                        print(replace)
                        new_lines.append("loadI " + str(spilling_address) + " => " + feasible_registers[0] + "\n")
                        new_lines.append("store " + physical_registers[replace] + " => " + feasible_registers[0] + "\n")
                        allocator.update({physical_registers[replace]: reg})
                        spilled = True
                        print("spilled " + keys[replace] + " " + values[replace])

                    #Check if the register needs to be loaded from memory
                    for mem in memory:
                        if reg == mem[0]:
                            #Insert load code
                            new_lines.append("loadI " + str(mem[1])+ " => " + feasible_registers[0] + "\n")
                            new_lines.append("load " + feasible_registers[0] + " => " + physical_registers[replace] + "\n")
                            memory.remove(mem)
                            print("load " + reg)
                            break 
                    
                    if spilled:
                        memory.append((furthest, spilling_address))
                        spilling_address -= 4

        #Replace the virtual registers with the assigned physical registers
        new_line = line
        keys = list(allocator.keys())
        print(allocator)
        print(line)
        for key in keys:
            if allocator.get(key) in line:
                new_line = re.sub(f"{allocator.get(key)}(?=\\s|\\n|,)", key, new_line)
        new_lines.append(new_line)
        print(new_line)
    else:
        new_lines.append(line)

for line in new_lines:
    new_line = line
    for reg in physical_registers:
        new_line = re.sub(f"{reg}(?=\\s|\\n|,)", "r" + str(physical_registers.index(reg)), new_line)
    for reg in feasible_registers:
        if reg in line:
            new_line = new_line.replace(reg, "r" + str(reg_num-1 + feasible_registers.index(reg)))
    output_file.write(new_line)
