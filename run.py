from core.attack_engine import simulate_credential_dump, simulate_reverse_shell
from core.log_simulator import generate_log
from core.exporter import export_to_csv
from core.evtx_generator import generate_evtx_script


def main():
    print("[*] Launching HADES Simulator")
    print("[1] Simulate Credential Dump (Mimikatz)")
    print("[2] Simulate Reverse Shell (Obfuscated)")

    choice = input("Select attack to simulate [1/2]: ").strip()

    if choice == "1":
        event = simulate_credential_dump()
    elif choice == "2":
        event = simulate_reverse_shell()
    else:
        print("Invalid choice.")
        return

    generate_log(event)
    export_to_csv(event)
    generate_evtx_script(event)

if __name__ == "__main__":
    main()
