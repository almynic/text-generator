from enum import Enum


class Color(Enum):
    BLACK = 0,
    CYAN = 1,
    YELLOW = 2,
    MAGENTA = 3,
    GREY = 4,
    INVALID = 4,


class ProductType(Enum):
    INK = 0,
    TONER = 1,
    DRUM = 2,
    INVALID = 3,


class BundleType(Enum):
    SINGLE = 0,
    SET = 1


class Classifier():

    def __init__(self) -> None:
        pass

    @staticmethod
    def classify(**kwargs):
        result = []
        for key, value in kwargs.items():
            result.append(classifcation(key)(value))
        print(result)


def ink():
    return ProductType.INK


def drum():
    return ProductType.DRUM


def toner():
    return ProductType.TONER


def f_default(value):
    return "invalid value: {}".format(value)


def classifcation(case):
    return {
        "product_type": determine_product_type,
        "colors": determine_colors,
        "scope_of_delivery": determine_bundle_type,
        "has_chip": has_chip
    }.get(case, f_default)


def determine_product_type(type):
    determine_type = {
        "Tinte": ink,
        "Toner": toner,
        "Bildtrommel": drum
    }
    return determine_type.get(type)()


def determine_colors(colors):
    found_colors = []
    for data in Color:
        if data.name in colors.upper():
            found_colors.append(data)
    return found_colors


def determine_bundle_type(scope_of_delivery):
    return scope_of_delivery


def has_chip(text):
    return text


if __name__ == "__main__":

    Classifier.classify(
        product_type="Tinte",
        colors="Black, Cyan, Yellow, Magenta",
        scope_of_delivery="1x Black, 1x Cyan, 1x Yellow, 1x Magenta",
        has_chip="Kein Chip",
    )

    Classifier.classify(
        product_type="Tinte",
        colors="Black, Cyan, Yellow, Magenta",
    )
