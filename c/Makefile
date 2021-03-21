# -------------------------------------------------------
# c/cpp Make file
# BIN: binary file name
# DEBUG: include debug symbols when the value is 1
CC = gcc
CXX = g++

LIBS =

CFLAGS = 
CXXFLAGS = 
LDFLAGS = 

DEBUG =

BIN = main

C_SRC = $(wildcard *.c)
CXX_SRC =$(wildcard *.cc *.cpp)
# rebuild if header files changed
DEPS = $(wildcard *.h *.hh *.hpp)

# Run pkg-config when LIBS is not empty
ifneq (,$(LIBS))
	_CFLAGS = $(shell pkg-config --cflags $(LIBS))
	_LDFLAGS = $(shell pkg-config --libs $(LIBS))
endif
# Add -lstdc++ to gcc LDFLAGS when any cpp source file appears
ifneq (,$(CXX_SRC))
	_LDFLAGS += -lstdc++
endif
# Include debug symbols
ifeq ($(DEBUG), 1)
	_CFLAGS += -g
endif
# Compile as shared library and change binary name to lib$(BIN).so
ifneq (,$(findstring -shared, $(LDFLAGS)))
	BIN := lib$(BIN).so
endif

CFLAGS += $(_CFLAGS) -I.
CXXFLAGS += $(_CFLAGS)
LDFLAGS += $(_LDFLAGS)

OBJ = $(filter %.o, $(C_SRC:.c=.o) $(CXX_SRC:.cpp=.o) $(CXX_SRC:.cc=.o))

PHONY = run clean

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

%.o: %.cc %.cpp $(DEPS)
	$(CXX) -c -o $@ $< $(CFLAGS)

$(BIN): $(OBJ)
	$(CC) -o $@ $^ $(LDFLAGS)

run: $(BIN)
	./main

# create compile_commands.json for auto completion
compile_commands:
	bear -- make -j$(shell nproc) -B

clean:
	rm -rf *.o lib$(BIN).so $(BIN)

.PHONY: $(PHONY)
# -------------------------------------------------------
