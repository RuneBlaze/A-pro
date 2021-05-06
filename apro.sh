#!/bin/bash
p=$(dirname "$0")
java -jar -D"java.library.path=$p/ASTRAL-MP/lib" "$p/ASTRAL-MP/astral.1.1.5.jar" -i "$1" -e "$2" -o "$3" -t 0