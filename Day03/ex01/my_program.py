from path import Path


def main():
    try:
        Path.makedirs("interesting_folder")
    except FileExistsError as e:
        print(e)
    f = Path("interesting_folder/magic_file")
    f.write_text("Hello, this is magic box. You can open it only with the magic stick!")
    print(f.read_text())


if __name__ == '__main__':
    main()