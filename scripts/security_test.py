import subprocess

def test_security():
    print("Running security test...")
    cmd = "sudo nmap -sS -sV localhost"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
