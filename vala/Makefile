# -------------------------------------------------------
# c/cpp Make file
# BIN: binary file name
# DEBUG: include debug symbols when the value is 1
VALAC = valac

VALAFLAGS =

DEBUG =

BIN = main

VALA_SRC = $(wildcard *.vala)

# Include debug symbols
ifeq ($(strip $(DEBUG)), 1)
	VALAFLAGS += -g
endif
# Compile as shared library and change binary name to lib$(BIN).so
ifneq (,$(findstring -shared, $(LDFLAGS)))
	BIN := lib$(BIN).so
endif


OBJ = $(filter %.o, $(C_SRC:.c=.o) $(VALA_SRC:=.o))

PHONY = run clean

$(BIN): $(VALA_SRC)
	$(VALAC) -o $(BIN) $(VALA_SRC) $(VALAFLAGS)

run: $(BIN)
	./$(BIN)

# create compile_commands.json for auto completion
clean:
	rm -f *.o lib$(BIN).so $(BIN)

.PHONY: $(PHONY)
# -------------------------------------------------------
