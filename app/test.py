import json

# data = {
#     "devices": [
#         {
#             "name": "Battery-19",
#             "type": "Battery",
#             "startVertex": [10.075952990301687, -202.11723853801857],
#             "endVertex": [112.07595299030169, -202.11723853801857],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 9,
#                 "isFlammable": True,
#                 "isMetallic": False,
#                 "batteryType": "normal",
#                 "internalResistance": 0.0001,
#             },
#         },
#         {
#             "name": "Switch-20",
#             "type": "Switch",
#             "startVertex": [-238.4827586206896, -199.88274725552264],
#             "endVertex": [-126.4827586206896, -199.88274725552264],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": -9,
#                 "isFlammable": False,
#                 "isMetallic": False,
#                 "resistance": 1000000000,
#                 "isClosed": False,
#             },
#         },
#         {
#             "name": "Wire-21",
#             "type": "Wire",
#             "startVertex": [-126.4827586206896, -199.88274725552264],
#             "endVertex": [10.075952990301687, -202.11723853801857],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": True,
#                 "resistance": 1.3657699172315022e-8,
#                 "length": 0.06828849586157511,
#                 "resistivity": 1e-10,
#             },
#         },
#         {
#             "name": "Wire-22",
#             "type": "Wire",
#             "startVertex": [112.07595299030169, -202.11723853801857],
#             "endVertex": [269.72419475686945, -202.8621257913524],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": True,
#                 "resistance": 1.5765000155125398e-8,
#                 "length": 0.07882500077562699,
#                 "resistivity": 1e-10,
#             },
#         },
#         {
#             "name": "Wire-23",
#             "type": "Wire",
#             "startVertex": [-335.26895273142844, -199.1379026215652],
#             "endVertex": [-238.4827586206896, -199.88274725552264],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": True,
#                 "resistance": 9.678906014612577e-9,
#                 "length": 0.04839453007306289,
#                 "resistivity": 1e-10,
#             },
#         },
#         {
#             "name": "Wire-24",
#             "type": "Wire",
#             "startVertex": [-337.50342980746564, 140.50345111715376],
#             "endVertex": [-335.26895273142844, -199.1379026215652],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": True,
#                 "resistance": 3.396487038945872e-8,
#                 "length": 0.1698243519472936,
#                 "resistivity": 1e-10,
#             },
#         },
#         {
#             "name": "Wire-25",
#             "type": "Wire",
#             "startVertex": [-337.50342980746564, 140.50345111715376],
#             "endVertex": [-170.46898256499196, 136.03439751986792],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": True,
#                 "resistance": 1.670942219397611e-8,
#                 "length": 0.08354711096988054,
#                 "resistivity": 1e-10,
#             },
#         },
#         {
#             "name": "Resistor-26",
#             "type": "Resistor",
#             "startVertex": [-170.46898256499196, 136.03439751986792],
#             "endVertex": [-60.46898256499185, 136.03439751986792],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": True,
#                 "isMetallic": False,
#                 "resistance": 10,
#                 "powerDissipated": 0,
#             },
#         },
#         {
#             "name": "Wire-27",
#             "type": "Wire",
#             "startVertex": [-60.46898256499185, 136.03439751986792],
#             "endVertex": [132.67585070379857, 133.8000625084186],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": True,
#                 "resistance": 1.9315775643595635e-8,
#                 "length": 0.09657887821797817,
#                 "resistivity": 1e-10,
#             },
#         },
#         {
#             "name": "LightBulb-28",
#             "type": "LightBulb",
#             "startVertex": [132.67585070379857, 133.8000625084186],
#             "endVertex": [158.13169482651426, 108.34421838570287],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": False,
#                 "resistance": 10,
#                 "isReal": False,
#                 "isExtreme": False,
#                 "brightness": 0,
#                 "isLit": False,
#             },
#         },
#         {
#             "name": "Wire-29",
#             "type": "Wire",
#             "startVertex": [269.72419475686945, -202.8621257913524],
#             "endVertex": [280.8966085499728, 106.24139351680356],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": True,
#                 "resistance": 3.093053644517855e-8,
#                 "length": 0.15465268222589276,
#                 "resistivity": 1e-10,
#             },
#         },
#         {
#             "name": "Wire-30",
#             "type": "Wire",
#             "startVertex": [158.13169482651426, 108.34421838570287],
#             "endVertex": [280.8966085499728, 106.24139351680356],
#             "properties": {
#                 "current": 0,
#                 "currentSense": "UNSPECIFIED",
#                 "voltage": 0,
#                 "isFlammable": False,
#                 "isMetallic": True,
#                 "resistance": 1.2278292191488803e-8,
#                 "length": 0.06139146095744401,
#                 "resistivity": 1e-10,
#             },
#         },
#     ],
#     "connections": [
#         ["Battery-19.startvertex", "Wire-21.endvertex"],
#         ["Battery-19.endvertex", "Wire-22.startvertex"],
#         ["Switch-20.startvertex", "Wire-23.endvertex"],
#         ["Switch-20.endvertex", "Wire-21.startvertex"],
#         ["Wire-22.endvertex", "Wire-29.startvertex"],
#         ["Wire-23.startvertex", "Wire-24.endvertex"],
#         ["Wire-24.startvertex", "Wire-25.startvertex"],
#         ["Wire-25.endvertex", "Resistor-26.startvertex"],
#         ["Resistor-26.endvertex", "Wire-27.startvertex"],
#         ["Wire-27.endvertex", "LightBulb-28.startvertex"],
#         ["LightBulb-28.endvertex", "Wire-30.startvertex"],
#         ["Wire-29.endvertex", "Wire-30.endvertex"],
#     ],
# }

data = {
    "devices": [
        {
            "name": "Battery-19",
            "type": "Battery",
            "start": [-104.62764871531516, -126.1448048558729],
            "end": [-2.6276487153151606, -126.1448048558729],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 9,
                "isFlammable": True,
                "isMetallic": False,
                "batteryType": "normal",
                "internalResistance": 0.0001,
            },
        },
        {
            "name": "Resistor-20",
            "type": "Resistor",
            "start": [-247.38224081522253, 54.71396268231527],
            "end": [-247.05794268488677, -55.285559274476256],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": True,
                "isMetallic": False,
                "resistance": 10,
                "powerDissipated": 0,
            },
        },
        {
            "name": "Wire-21",
            "type": "Wire",
            "start": [-246.63449412378765, -124.65518662025187],
            "end": [-104.62764871531516, -126.1448048558729],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": True,
                "resistance": 1.4201465806512264e-8,
                "length": 0.07100732903256132,
                "resistivity": 1e-10,
            },
        },
        {
            "name": "Wire-22",
            "type": "Wire",
            "start": [-247.05794268488677, -55.285559274476256],
            "end": [-246.63449412378765, -124.65518662025187],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": True,
                "resistance": 6.937091974866469e-9,
                "length": 0.034685459874332344,
                "resistivity": 1e-10,
            },
        },
        {
            "name": "Wire-24",
            "type": "Wire",
            "start": [-247.37929613836866, 141.24825313173477],
            "end": [-247.38224081522253, 54.71396268231527],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": True,
                "resistance": 8.653429049952172e-9,
                "length": 0.043267145249760865,
                "resistivity": 1e-10,
            },
        },
        {
            "name": "Wire-25",
            "type": "Wire",
            "start": [-247.37929613836866, 141.24825313173477],
            "end": [-140.67585070379846, 141.2482815446524],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": True,
                "resistance": 1.0670344543457399e-8,
                "length": 0.053351722717287,
                "resistivity": 1e-10,
            },
        },
        {
            "name": "Switch-26",
            "type": "Switch",
            "start": [-140.67585070379846, 141.2482815446524],
            "end": [-28.67585070379846, 141.2482815446524],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 9,
                "isFlammable": False,
                "isMetallic": False,
                "resistance": 1000000000,
                "isClosed": False,
            },
        },
        {
            "name": "Resistor-27",
            "type": "Resistor",
            "start": [-28.67585070379846, 141.2482815446524],
            "end": [81.32414929620154, 141.2482815446524],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": True,
                "isMetallic": False,
                "resistance": 10,
                "powerDissipated": 0,
            },
        },
        {
            "name": "Wire-28",
            "type": "Wire",
            "start": [81.32414929620154, 141.2482815446524],
            "end": [199.71039028825442, 141.2482815446524],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": True,
                "resistance": 1.1838624099205288e-8,
                "length": 0.05919312049602644,
                "resistivity": 1e-10,
            },
        },
        {
            "name": "Wire-29",
            "type": "Wire",
            "start": [199.71039028825442, 141.2482815446524],
            "end": [202.68971199824898, 56.33798217773432],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": True,
                "resistance": 8.496255231824956e-9,
                "length": 0.04248127615912478,
                "resistivity": 1e-10,
            },
        },
        {
            "name": "LightBulb-30",
            "type": "LightBulb",
            "start": [202.68971199824898, 56.33798217773432],
            "end": [228.14555612096467, 30.8821380550186],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": False,
                "resistance": 10,
                "isReal": False,
                "isExtreme": False,
                "brightness": 0,
                "isLit": False,
            },
        },
        {
            "name": "Wire-31",
            "type": "Wire",
            "start": [-2.6276487153151606, -126.1448048558729],
            "end": [227.2689882475754, -125.39997442837424],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": True,
                "resistance": 2.2989784352884398e-8,
                "length": 0.11494892176442198,
                "resistivity": 1e-10,
            },
        },
        {
            "name": "Wire-32",
            "type": "Wire",
            "start": [227.2689882475754, -125.39997442837424],
            "end": [228.14555612096467, 30.8821380550186],
            "properties": {
                "current": 0,
                "currentSense": "UNSPECIFIED",
                "voltage": 0,
                "isFlammable": False,
                "isMetallic": True,
                "resistance": 1.5628457074679033e-8,
                "length": 0.07814228537339517,
                "resistivity": 1e-10,
            },
        },
    ],
    "connections": [
        ["Battery-19.start", "Wire-21.end"],
        ["Battery-19.end", "Wire-31.start"],
        ["Resistor-20.start", "Wire-24.end"],
        ["Resistor-20.end", "Wire-22.start"],
        ["Wire-21.start", "Wire-22.end"],
        ["Wire-24.start", "Wire-25.start"],
        ["Wire-25.end", "Switch-26.start"],
        ["Switch-26.end", "Resistor-27.start"],
        ["Resistor-27.end", "Wire-28.start"],
        ["Wire-28.end", "Wire-29.start"],
        ["Wire-29.end", "LightBulb-30.start"],
        ["LightBulb-30.end", "Wire-32.end"],
        ["Wire-31.end", "Wire-32.start"],
    ],
}

experiment_id = 2
sql_lines = []
devices_json = data["devices"]
connections_json = data["connections"]

"""DEVICE"""
device_types = {}
device_id_counter = 1
device_sql = "INSERT INTO device (id, type) VALUES \n"
device_sql_list = []
for i, device_json in enumerate(devices_json):
    dtype = device_json["type"]
    if dtype not in device_types:
        device_types[dtype] = device_id_counter
        device_sql_list.append(f" ({device_id_counter}, '{dtype}')")
        device_id_counter += 1
device_sql += ",\n".join(device_sql_list) + ";"
print(device_sql)
print("---------------------------------------------")

"""EXPERIMENT - DEVICE"""
exp_dev_ids = {}
exp_dev_counter = 13
exp_dev_sql = "INSERT INTO experiment_device (id, experiment_id, device_id, device_name, properties) VALUES \n"
exp_dev_sql_list = []

for device_json in devices_json:
    device_id = device_types[device_json["type"]]
    exp_dev_ids[device_json["name"]] = exp_dev_counter

    # Chuyển properties sang JSON chuẩn
    props_json = json.dumps(device_json["properties"], ensure_ascii=False)

    exp_dev_sql_list.append(
        f" ({exp_dev_counter}, {experiment_id}, {device_id}, '{device_json['name']}', '{props_json}'::jsonb)"
    )
    exp_dev_counter += 1

exp_dev_sql += ",\n".join(exp_dev_sql_list) + ";"
print(exp_dev_sql)
print("---------------------------------------------")


"""VERTEX"""
# ----- STEP 3: INSERT VERTEX -----
vertex_ids = {}
vertex_counter = 25
vertex_sql = "INSERT INTO vertex (id, x, y, type, experiment_device_id) VALUES \n"
vertex_sql_list = []
for device_json in devices_json:
    for vtype in ["start", "end"]:
        coords = device_json[vtype]
        short_type = "start" if vtype.lower().startswith("start") else "end"
        vertex_ids[f"{device_json['name']}.{short_type}"] = vertex_counter
        vertex_sql_list.append(
            f" ({vertex_counter}, {coords[0]}, {coords[1]}, '{short_type}', {exp_dev_ids[device_json['name']]})"
        )
        vertex_counter += 1
vertex_sql += ",\n".join(vertex_sql_list) + ";"
print(vertex_sql)
print("---------------------------------------------")

"""CONNECTION"""
connection_sql = "INSERT INTO connection (vertex_1_id, vertex_2_id) VALUES \n"
connection_sql_list = []
for c in connections_json:
    v1 = c[0].replace("startvertex", "start").replace("endvertex", "end")
    v2 = c[1].replace("startvertex", "start").replace("endvertex", "end")
    v1_id = vertex_ids[v1]
    v2_id = vertex_ids[v2]
    connection_sql_list.append(f" ({v1_id}, {v2_id})")
connection_sql += ",\n".join(connection_sql_list) + ";"
print(connection_sql)
