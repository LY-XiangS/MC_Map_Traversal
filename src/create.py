from math import ceil, log


def mcMap(MapId: "int", Slot: "int") -> str:
    return f'{{Count:1b,Slot:{Slot}b,id:"minecraft:filled_map",tag:{{map:{MapId}}}}}'


def mcShulker(Item: "list[str]", Text: "str", Slot: "int" = -1) -> str:
    return f'{{Count:1b,{"" if Slot == -1 else f"Slot:{Slot}b,"}id:"minecraft:white_shulker_box",tag:{{BlockEntityTag:{{Items:[{",".join(Item)}],id:"minecraft:shulker_box"}},display:{{Name:\'{{"Italic":false,"extra":[{{"text":""}},{{"Bold":true,"color":"white","text":"{Text}"}}],"text":""}}\'}}}}}}'


def mcBox(Item: "list[str]", Text: "str", Slot: "int" = -1) -> str:
    return f'{{Count:1b,{"" if Slot == -1 else f"Slot:{Slot}b,"}id:"minecraft:chest",tag:{{BlockEntityTag:{{Items:[{",".join(Item)}],id:"minecraft:chest"}},display:{{Name:\'{{"Italic":false,"extra":[{{"text":""}},{{"bold":true,"color":"white","text":"{Text}"}}],"text":""}}\'}}}}}}'


def iterator(start: "int", end: "int"):
    step = 27 ** ceil(log(end - start, 27) - 1) if end - start > 1 else 1
    if step > 1:
        sequence = list(range(start, end, step)) + [end]
        sequence = tuple(
            (sequence[i], sequence[i + 1]) for i in range(len(sequence) - 1)
        )
    pass


if __name__ == "__main__":
    print(mcBox([mcShulker([mcMap(1, 1)], "6", 1)], "7"))
    print(iterator(0, 1))
