package ma.enset.server;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import ma.enset.service.GrpcChatService;

import java.io.IOException;

public class GrpcChatServer {

    public static void main(String[] args) throws IOException, InterruptedException {
        Server server= ServerBuilder.forPort(9999)
                .addService(new GrpcChatService())
                .build();
        server.start();
        server.awaitTermination();
    }
}
