package ma.enset.service;

import ma.enset.stubs.Chat;
import ma.enset.stubs.ChatServiceGrpc;
import com.google.protobuf.Timestamp;
import io.grpc.stub.StreamObserver;

import java.util.LinkedHashSet;

public class GrpcChatService extends ChatServiceGrpc.ChatServiceImplBase {
    private static LinkedHashSet<StreamObserver<Chat.ChatMessageFromServer>> observers = new LinkedHashSet<>();

    @Override
    public StreamObserver<Chat.ChatMessage> sendChatMessage(StreamObserver<Chat.ChatMessageFromServer> responseObserver) {

        // Add response observer to the list
        observers.add(responseObserver);

        // Handler for client messages
        return new StreamObserver<Chat.ChatMessage>() {

            @Override
            public void onNext(Chat.ChatMessage value) {

                // Create a server message from the client message
                Timestamp timestamp = Timestamp.newBuilder()
                        .setSeconds(System.currentTimeMillis())
                        .build();

                Chat.ChatMessageFromServer message = Chat.ChatMessageFromServer
                        .newBuilder()
                        .setMessage(value)
                        .setTimestamp(timestamp)
                        .build();

                // Notify all observers
                for (StreamObserver<Chat.ChatMessageFromServer> observer : observers) {
                    observer.onNext(message);
                }
            }

            @Override
            public void onError(Throwable t) {
                t.getMessage();
                observers.remove(responseObserver);
            }

            @Override
            public void onCompleted() {
                System.out.println("Completed!");
            }
        };
    }
}
