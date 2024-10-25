def mcMap(MapId: "int", Slot: "int") -> str:
    return f'{{Count:1b,Slot:{Slot}b,id:"minecraft:filled_map",tag:{{map:{MapId}}}}}'


def mcShulker(Item: "list", Text: "str", Slot: "int" = -1) -> str:
    return f'{{Count:1b,{"" if Slot == -1 else f"Slot:{Slot}b,"}id:"minecraft:white_shulker_box",tag:{{BlockEntityTag:{{Items:{Item},id:"minecraft:shulker_box"}},display:{{Name:\'{{"Italic":false,"extra":[{{"text":""}},{{"Bold":true,"color":"white","text":"{Text}"}}],"text":""}}\'}}}}}}'


def mcBox(Item: "list", Text: "str") -> str:
    return f'{{Count:1b,id:"minecraft:chest",tag:{{BlockEntityTag:{{Items:{Item},id:"minecraft:chest"}},display:{{Name:\'{{"Italic":false,"extra":[{{"text":""}},{{"bold":true,"color":"white","text":"{Text}"}}],"text":""}}\'}}}}}}'


if __name__ == "__main__":
    print(mcBox([mcShulker([mcMap(1, 1)], "6", 1)], "7"))
