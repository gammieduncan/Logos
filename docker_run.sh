docker run \
--mount src="$(pwd)"/app/static,target=/usr/src/app/static,type=bind,readonly \
--mount src="$(pwd)"/app/templates,target=/usr/src/app/templates,type=bind,readonly \
logos:latest
