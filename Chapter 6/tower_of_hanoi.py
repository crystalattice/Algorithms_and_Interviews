def hanoi_tower(n, from_peg, to_peg, temp_peg):
    if n == 1:
        print(f"Move disk 1 from {from_peg} to {to_peg}")
        return
    hanoi_tower(n - 1, from_peg, temp_peg, to_peg)
    print(f"Move disk {n} from {from_peg} to {to_peg}")
    hanoi_tower(n - 1, temp_peg, to_peg, from_peg)


if __name__ == "__main__":
    discs = 4
    hanoi_tower(discs, 'Peg A', 'Peg Via', 'Peg B')
