import subprocess

def run_step(name, command):
    print(f"\n--- Running {name} ---")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise Exception(f"{name} failed")
    print(f"{name} completed successfully")


if __name__ == "__main__":
    run_step("Ingestion", "python scripts/ingest.py")
    run_step("Transformation", "python scripts/transform.py")
    run_step("Load to Database", "python scripts/load.py")

    print("\nPipeline executed successfully 🚀")