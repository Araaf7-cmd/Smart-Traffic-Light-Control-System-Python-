import time
import random

class Road:
    """Class to represent a road connected to an intersection."""
    def __init__(self, name):
        self.name = name
        self.vehicle_count = 0
        self.green_time = 0
        self.total_cleared = 0

    def detect_traffic(self):
        """Simulate AI-based vehicle detection using random numbers."""
        self.vehicle_count = random.randint(5, 30)

    def calculate_green_time(self):
        """Adjust green light duration based on number of vehicles."""
        if self.vehicle_count > 25:
            self.green_time = 25
        elif self.vehicle_count > 15:
            self.green_time = 20
        elif self.vehicle_count > 8:
            self.green_time = 15
        else:
            self.green_time = 10

    def clear_vehicles(self):
        """Simulate vehicles cleared when green light is ON."""
        cleared = min(self.vehicle_count, self.green_time)
        self.total_cleared += cleared
        self.vehicle_count = max(0, self.vehicle_count - cleared)


class SmartTrafficSystem:
    """Main system controlling all roads and lights."""
    def __init__(self):

        self.roads = [
            Road("North"),
            Road("East"),
            Road("South"),
            Road("West")
        ]

    def detect_and_calculate(self):
        """AI module: detect vehicle density and compute green times."""
        print("\n📷 Detecting vehicle density on each road...\n")
        for road in self.roads:
            road.detect_traffic()
            road.calculate_green_time()
            print(f"{road.name} Road → Vehicles: {road.vehicle_count} | Green time: {road.green_time}s")
        print("\n AI has calculated optimized green times based on traffic load.\n")
        time.sleep(1)

    def display_signal_status(self, active_road):
        """Show which road is currently green and others red."""
        print("\n--------------------------------------------")
        for road in self.roads:
            if road == active_road:
                print(f"🟢 {road.name} Road: GREEN ({road.green_time}s)")
            else:
                print(f"🔴 {road.name} Road: RED")
        print("--------------------------------------------\n")

    def run_cycle(self, cycle_number):
        """Run one full cycle through all roads."""
        print(f"\n================= 🚦 CYCLE {cycle_number} START 🚦 =================\n")
        self.detect_and_calculate()

        # Prioritize roads with more vehicles
        self.roads.sort(key=lambda r: r.vehicle_count, reverse=True)


        for road in self.roads:
            self.display_signal_status(road)
            print(f"{road.name} road is now GREEN. Vehicles waiting: {road.vehicle_count}")
            print(f"Green light active for {road.green_time} seconds...\n")

            for remaining in range(road.green_time, 0, -1):
                print(f"  {road.name} road: {remaining:02d}s remaining", end="\r")
                time.sleep(0.2)  # fast simulation
            print("\n")

            road.clear_vehicles()
            print(f"🔴 {road.name} road turned RED. Vehicles cleared this cycle: {road.total_cleared}\n")
            time.sleep(0.5)

        print(f" CYCLE {cycle_number} COMPLETED ")
        print("=================================================================\n")
        time.sleep(1)

    def show_final_report(self):
        """Display summary after all cycles."""
        print("\n================= FINAL REPORT =================\n")
        for road in self.roads:
            print(f"{road.name} Road → Total Vehicles Cleared: {road.total_cleared}")
        print("\nSimulation complete. 🚦 System shutting down...\n")

    def run_system(self, total_cycles=4):
        """Run the entire system for a fixed number of cycles."""
        print("SMART TRAFFIC LIGHT CONTROL SYSTEM USING AI")
        print("--------------------------------------------")
        print("This system dynamically adjusts signal times using AI-based logic.\n")
        time.sleep(1)

        for cycle in range(1, total_cycles + 1):
            self.run_cycle(cycle)

        self.show_final_report()


# MAIN PROGRAM

if __name__ == "__main__":
    system = SmartTrafficSystem()
    system.run_system(total_cycles=4)
