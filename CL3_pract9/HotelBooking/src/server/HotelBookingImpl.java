package server;

import interfaces.HotelBookingInterface;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.util.*;

public class HotelBookingImpl extends UnicastRemoteObject implements HotelBookingInterface {
    private Map<String, String> bookings;

    public HotelBookingImpl() throws RemoteException {
        bookings = new HashMap<>();
    }

    public synchronized String bookRoom(String guestName) throws RemoteException {
        if (bookings.containsKey(guestName)) {
            return "Room already booked for " + guestName;
        }
        String roomNumber = "R" + (bookings.size() + 101); // Example: R101, R102...
        bookings.put(guestName, roomNumber);
        return "Room " + roomNumber + " booked for " + guestName;
    }

    public synchronized String cancelBooking(String guestName) throws RemoteException {
        if (bookings.containsKey(guestName)) {
            bookings.remove(guestName);
            return "Booking cancelled for " + guestName;
        } else {
            return "No booking found for " + guestName;
        }
    }
}
