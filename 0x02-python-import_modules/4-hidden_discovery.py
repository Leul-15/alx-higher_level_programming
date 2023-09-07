#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for n in range(0, len(name)):
        if "__" != name[n][:2]:
            print(name[n])
