import hashlib
import time


def calculate_hash(index: int, timestamp: float, data: str, previous_hash: str, nonce: int) -> str:
    payload = f"{index}{timestamp}{data}{previous_hash}{nonce}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def mine_block(index: int, data: str, previous_hash: str, difficulty: int = 4) -> dict:
    prefix = "0" * difficulty
    nonce = 0
    timestamp = time.time()

    start = time.time()
    while True:
        block_hash = calculate_hash(index, timestamp, data, previous_hash, nonce)
        if block_hash.startswith(prefix):
            elapsed = time.time() - start
            return {
                "index": index,
                "timestamp": timestamp,
                "data": data,
                "previous_hash": previous_hash,
                "nonce": nonce,
                "hash": block_hash,
                "difficulty": difficulty,
                "elapsed_seconds": elapsed,
            }
        nonce += 1


def is_block_valid(block: dict, previous_block: dict | None = None) -> bool:
    expected_hash = calculate_hash(
        block["index"],
        block["timestamp"],
        block["data"],
        block["previous_hash"],
        block["nonce"],
    )
    if block["hash"] != expected_hash:
        return False

    if not block["hash"].startswith("0" * block["difficulty"]):
        return False

    if previous_block is not None:
        if block["index"] != previous_block["index"] + 1:
            return False
        if block["previous_hash"] != previous_block["hash"]:
            return False

    return True


def is_chain_valid(chain: list[dict]) -> bool:
    if not chain:
        return False

    if not is_block_valid(chain[0], None):
        return False

    for i in range(1, len(chain)):
        if not is_block_valid(chain[i], chain[i - 1]):
            return False

    return True


def main() -> None:
    print("Mini blockchain PoW (estilo Bitcoin)\n")
    print("Minando 3 bloques con dificultad 4...\n")

    difficulty = 4
    chain: list[dict] = []

    genesis_block = mine_block(
        index=0,
        data="Bloque génesis",
        previous_hash="0" * 64,
        difficulty=difficulty,
    )
    chain.append(genesis_block)

    block_1 = mine_block(
        index=1,
        data="Alice paga 0.1 BTC a Bob",
        previous_hash=chain[-1]["hash"],
        difficulty=difficulty,
    )
    chain.append(block_1)

    block_2 = mine_block(
        index=2,
        data="Bob paga 0.05 BTC a Carol",
        previous_hash=chain[-1]["hash"],
        difficulty=difficulty,
    )
    chain.append(block_2)

    for block in chain:
        print(f"Bloque {block['index']}:")
        print(f"- Data: {block['data']}")
        print(f"- Nonce: {block['nonce']}")
        print(f"- Hash: {block['hash']}")
        print(f"- Previous: {block['previous_hash']}")
        print(f"- Tiempo de minado: {block['elapsed_seconds']:.4f} s\n")

    print(f"Cadena válida: {is_chain_valid(chain)}")


if __name__ == "__main__":
    main()
