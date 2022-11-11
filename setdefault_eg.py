# setdefault operation example

def usual_dict(dict_data):
    new_data = {}
    for k, v in dict_data:
        if k in new_data:
            new_data[k].append(v)
        else:
            new_data[k] = [v]
    return new_data 

def setdefault_dict(dict_data):
    new_data = {}
    for k, v in dict_data:
        new_data.setdefault(k, []).append(v)
    return new_data

def test(module_name="this module"):
    test_dict_data = (
        ("key1", "value1"),
        ("key1", "value2"),
        ("key2", "value3"),
        ("key2", "value4"),
        ("key2", "value5")
    )

    print(usual_dict(test_dict_data))
    print(setdefault_dict(test_dict_data))
    name=module_name
    con="Passed"
    print(f"Tests in {name} in have {con}")

if __name__ == "__main__":
    test()