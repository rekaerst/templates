# -------------------------------------------------------
# c/cpp Make file
# BIN: binary file name
# DEBUG: include debug symbols when the value is 1
CC = gcc
CXX = g++

LIBS = gtk+-3.0

CFLAGS = 
CXXFLAGS = 

LDFLAGS =
LDLIBS =

DEBUG =

BIN = main

C_SRC = $(wildcard *.c)
CXX_SRC =$(wildcard *.cc *.cpp)
# rebuild if header files changed
DEPS = $(wildcard *.h *.hh *.hpp)

# Run pkg-config when LIBS is not empty
ifneq ($(strip $(LIBS)),)
	CFLAGS += $(shell pkg-config --cflags $(LIBS))
	LDLIBS += $(shell pkg-config --libs $(LIBS))
endif
# Add -lstdc++ to gcc LDFLAGS when any cpp source file appears
ifneq ($(strip $(CXX_SRC)),)
	LDLIBS += -lstdc++
endif
# Include debug symbols
ifeq ($(strip $(DEBUG)), 1)
	CFLAGS += -g
endif
# Compile as shared library and change binary name to lib$(BIN).so
ifneq (,$(findstring -shared, $(LDFLAGS)))
	BIN := lib$(BIN).so
endif

CFLAGS +=  -I.
CXXFLAGS += $(CFLAGS)

OBJ = $(filter %.o, $(C_SRC:.c=.o) $(CXX_SRC:.cpp=.o) $(CXX_SRC:.cc=.o))

PHONY = run clean

$(BIN): $(OBJ)
	$(CC) $(LDFLAGS) -o $(BIN) $(OBJ) $(LDLIBS)

%.o: %.c $(DEPS)
	$(CC) -c $< $(CFLAGS) -o $@

%.o: %.cc %.cpp $(DEPS)
	$(CXX) -c $< $(CXXFLAGS) -o $@


run: $(BIN)
	./$(BIN)

# create compile_commands.json for auto completion
compile_commands:
	bear -- make -j$(shell nproc) -B

clean:
	rm -f *.o lib$(BIN).so $(BIN)

.PHONY: $(PHONY)
# -------------------------------------------------------
