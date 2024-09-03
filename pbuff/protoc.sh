PROTO_DIR=proto/
protoc --proto_path=$PROTO_DIR --python_out=./ $PROTO_DIR/*.proto
