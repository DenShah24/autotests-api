import glob


def fix_grpc_imports():
    # Найти все _pb2_grpc.py
    files = glob.glob("*_pb2_grpc.py")
    for filename in files:
        with open(filename, 'r') as f:
            content = f.read()

        # Заменить import → from . import
        new_content = content.replace(
            "import ", "from . import "
        )

        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"✅ Исправлен: {filename}")


if __name__ == '__main__':
    fix_grpc_imports()