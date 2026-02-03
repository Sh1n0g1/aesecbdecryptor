CC ?= clang
CFLAGS ?= -Wall -Wextra -Werror -O2 -std=c17
LDFLAGS ?=

TARGET := neoshinobot
SRC := src/main.c

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET) $(LDFLAGS)

clean:
	rm -f $(TARGET)
