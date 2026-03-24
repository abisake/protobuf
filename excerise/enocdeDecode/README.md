To use --encode & --decode, we need to do few more changes.
1. Create a text file with inputs for the defined proto
2. Convert the inputs file using encoding, instead of standard conversion
    you can use cat combined with pipe
    Eg: cat <input_file> | protoc -I<path_for_output_dir> --encode=<message_name> <proto_file> > <output_file_name>
    cat input_file | protoc -I. --encode=Course sameLevel.proto > course.bin

    Imp: If the message is defined under package, use the fully defined package name
3. This will convert the standard input to serialized binary
4. Now we can convert the serialized binary into standard input, which should match with the input
5. There might be some mismatch, like after lecture ":" wont be there, but that wont cause any issue
    Imp: The order of repeated field or map, is not ensured that by protobuf
6. To decode it, you can use cat combined with pipe
    Eg: cat <binary_file> | protoc -I<path_for_output> --decode=<message_name> <proto_file>
    cat course.bin | protoc -I. --decode=Course sameLevel.proto