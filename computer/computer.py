"""
This should keep all things about the computer
"""

class Computer():
    program = []
    accumulator = 0
    i_pointer = 0
    running = False
    history_calls = []
    halt_reason = ""

    step_counter = 0

    debug = False

    def reset(self):
        self.accumulator = 0
        self.i_pointer = 0
        self.running = False
        self.history_calls = []
        self.step_counter = 0

    def hard_reset(self):
        self.reset()
        self.program = []
        self.debug = False

    def print_progcode(self):
        for k, line in enumerate(self.program):
            print("{:4}: {:5} {: 4d}".format(k, line[0], line[1]))

    def print_status(self):
        print("steps {:6}; i_pntr {:4}; accumulator {:5}".format(self.step_counter, self.i_pointer, self.accumulator))

    def load_program(self, _porg_array):
        for line in  _porg_array:
            opcode, _arg = line.split(" ")
            if opcode not in ["acc", "jmp", "nop"]:
                raise ValueError("Unexpected opcode")
            try:
                arg = int(_arg)
            except ValueError as value_error:
                print("Cannot convert the argument to int")
                raise value_error
            self.program.append([opcode, arg])

    def step(self):
        """
        acc increases or decreases a single global value called the accumulator
            by the value given in the argument. For example, acc +7 would increase
            the accumulator by 7. The accumulator starts at 0. After an acc instruction,
            the instruction immediately below it is executed next.
        jmp jumps to a new instruction relative to itself. The next instruction to
            execute is found using the argument as an offset from the jmp instruction;
            for example, jmp +2 would skip the next instruction, jmp +1 would continue
            to the instruction immediately below it, and jmp -20 would cause the instruction
            20 lines above to be executed next.
        nop stands for No OPeration - it does nothing.
            The instruction immediately below it is executed next.
        """
        opcode, arg  = self.program[self.i_pointer]
        if self.debug: 
            self.print_status()
            print("                                                 instr -- {:5} {: 4d}".format(opcode, arg))
        self.history_calls.append(self.i_pointer)
        self.step_counter += 1
        if opcode == 'nop':
            self.i_pointer += 1
        elif opcode == "jmp":
            self.i_pointer += arg
        elif opcode == "acc":
            self.accumulator += arg
            self.i_pointer += 1
        else:
            raise ValueError("Unexpected opcode")

    def run_once(self, silent = False):
        if self.debug:
            print("Start run_once")
        self.running = True
        self.halt_reason = ""
        while self.running:
            # keep steping while running
            self.step()
            # Break Conditions here
            if self.i_pointer in self.history_calls: 
                self.running = False
                self.halt_reason = "LOOP"
            if self.i_pointer >= len(self.program):
                self.running = False
                self.halt_reason = "FINISHED"
        if not silent:
            print("Finished run_once caused by {}".format(self.halt_reason))

    def run_day08_1(self):
        """
        return value before looping
        """
        self.run_once()
        return self.accumulator

    def run_day08_2(self):
        """
        fix program by swapping one jmp and nop operation instruction without changing arguments
        """
        self.debug = False
        for k, val in enumerate(self.program):
            op = val[0]
            old_op = op
            new_op = ""
            if op == "nop":
                new_op = "jmp"
            elif op == "jmp":
                new_op = "nop"
            else:
                continue
            print(k,end=" ")
            self.program[k][0] = new_op
            self.reset()
            self.run_once(silent=True)
            if self.halt_reason == "FINISHED":
                print()
                return self.accumulator
            # restore original program
            self.program[k][0] = old_op
