import argparse
from utils.network import get_available_networks, switch_to_network

def interactive_mode():
    while True:
        print("\n1. List available networks")
        print("2. Switch to a network")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            networks = get_available_networks()
            if not networks:
                print("No networks found.")
            else:
                for i, network in enumerate(networks):
                    print(f"{i + 1}. {network['name']} (Signal strength: {network['signal_strength']})")
        elif choice == '2':
            network_name = input("Enter the network name to switch to: ")
            switch_to_network(network_name)
            print(f"Switched to network {network_name}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    parser = argparse.ArgumentParser(description="Network switcher script")
    parser.add_argument('-interface', action='store_true', help="Run in interactive mode")
    args = parser.parse_args()

    if args.interface:
        interactive_mode()
    else:
        networks = get_available_networks()
        if not networks:
            print("No networks found.")
            return

        best_network = max(networks, key=lambda x: x['signal_strength'])
        print(f"Switching to the best network: {best_network['name']} with signal strength {best_network['signal_strength']}")
        switch_to_network(best_network['name'])

if __name__ == "__main__":
    main()