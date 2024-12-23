def field(items, *args):
    assert len(args) > 0
    result = []
    dict_count = 0
    for item in items:
        result.append(dict())
        for key in item.keys():
            if key in args and item[key] is not None:
                result[dict_count].update({key: item[key]})
        dict_count += 1
    return [x[args[0]] for x in result]


def test():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    print(field(goods, 'title'))

#test()