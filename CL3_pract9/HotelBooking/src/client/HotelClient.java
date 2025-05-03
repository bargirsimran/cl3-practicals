package client;

import interfaces.HotelBookingInterface;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1100);
            HotelBookingInterface booking = (HotelBookingInterface) registry.lookup("HotelService");

            Scanner sc = new Scanner(System.in);
            while (true) {
                System.out.println("\n1. Book Room\n2. Cancel Booking\n3. Exit");
                System.out.print("Enter choice: ");
                int choice = sc.nextInt();
                sc.nextLine(); // consume newline

                if (choice == 1) {
                    System.out.print("Enter guest name: ");
                    String name = sc.nextLine();
                    System.out.println(booking.bookRoom(name));
                } else if (choice == 2) {
                    System.out.print("Enter guest name to cancel: ");
                    String name = sc.nextLine();
                    System.out.println(booking.cancelBooking(name));
                } else {
                    break;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
