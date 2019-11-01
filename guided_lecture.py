PRINT_ZACH = 0b01
HALT = 0b10
PRINT_NUM = 0b11
NUM_TO_PRINT = 10
SAVE = 0b100
ADD = 0b101
PRINT_REGISTER = 0b110

memory = [
    PRINT_ZACH,
    PRINT_ZACH,
    
    PRINT_NUM,
    NUM_TO_PRINT,
    
    PRINT_ZACH,
    PRINT_ZACH,
    SAVE,
    0b1111,
    0b10,
    SAVE,
    0b1111,
    0b11,
    ADD,
    0b10,
    0b11,
    PRINT_REGISTER,
    0b10,
    HALT,
]

# represents a small amount of available space to store data
registers = [0] * 8
running = True
pc = 0
    
while running:
    print(pc)
    print(len(memory))
    command = memory[pc] 

    if command == PRINT_ZACH:
        print("Zach Is The Man")
        
        pc += 1
    
    elif command == PRINT_NUM:
        number_to_print = memory[pc + 1]
        print(number_to_print)
        
        pc += 2
    
    elif command == HALT:
        running = False
    
    elif command == SAVE:
        num = memory[pc + 1]
        register = memory[pc + 2]
        registers[register] = num
        
        pc += 3
        
    elif command == ADD:
        first_register = memory[pc + 1]
        second_register = memory[pc + 2]
        
        first_num = registers[first_register]
        second_num = registers[second_register]
        
        total = first_num + second_num
        
        registers[first_register] = total
        
        pc += 3
    
    elif command == PRINT_REGISTER:
        register_address = memory[pc + 1]
        
        value_to_print = registers[register_address]
        print(value_to_print)
        
        pc += 2
        
    else:
        print("I don't know whats going on")
        running = False