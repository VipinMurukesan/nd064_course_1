FROM golang:alpine

WORKDIR /go/src/app

COPY ./go-helloworld .

RUN go build -o helloworld

CMD ["helloworld"]