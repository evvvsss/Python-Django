import requests
import sys
import json
import dewiki


def response(page: str):
    try:
        resp = requests.get(f"https://en.wikipedia.org/w/api.php?action=parse&page={page}&prop=wikitext&format=json&redirects=true")
        resp.raise_for_status() # returns an HTTPError object if an error has occurred during the process
    except requests.HTTPError as e:
        raise e
    try:
        text = json.loads(resp.text)
    except json.decoder.JSONDecodeError as e:
        raise e
    if text.get("error") is not None:
        raise Exception(text["error"]["info"])
    return(dewiki.from_string(text["parse"]["wikitext"]["*"]))


def main():
    if (len(sys.argv) == 2):
        try:
            a = response(sys.argv[1])
        except Exception as e:
            print(e)
            return
        try:
            with open("{}.wiki".format(sys.argv[1]), "w") as file:
                file.write(a)
        except Exception as e:
            print(e)
            return
    else:
        print("Wrong number of parameters")


if __name__ == '__main__':
    main()