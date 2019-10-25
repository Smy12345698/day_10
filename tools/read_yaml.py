import yaml
def read_yaml(filename):
    with open("./data/"+filename,"r",encoding="utf-8")as f:
        return yaml.load(f)

if __name__ == '__main__':
    print(read_yaml("login.yaml"))
    print("--"*50)
    arr = []
    for data in read_yaml("login.yaml").values():
        arr.append((data.get("phone"),
                    data.get("pwd"),
                    data.get("nickname"),
                    data.get("msg"),
                    data.get("toast"),
                    data.get("clickable")))
    print(arr)