package server;

import interfaces.HotelBookingInterface;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;


public class HotelServer {
    public static void main(String[] args) {
        try {
            HotelBookingInterface booking = new HotelBookingImpl();
            Registry registry = LocateRegistry.createRegistry(1100);
            registry.rebind("HotelService", booking);
            System.out.println("Hotel Booking Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
