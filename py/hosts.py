hosts = {
    "jackson" : {
        "j_sh_1" :
            {
                "host":"10.31.107.17",
                "pass":"011109",
                "vnc" : "vncviewer.exe -config vnc_conf\j_shipping_1_17.vnc",
                "description" : "Jackson Shipping 1"
            },
        "j_in_1" :
            {
                "host":"10.31.107.18",
                "pass":"011111",
                "vnc" : "vncviewer.exe -config vnc_conf\j_inbound_1_18.vnc",
                "description" : "Jackson Inbound 1"
            },
        "j_in_2" :
            {
                "host":"10.31.107.20",
                "pass":"011195",
                "vnc" : "vncviewer.exe -config vnc_conf\j_inbound_2_20.vnc",
                "description" : "Jackson Inbound 2"
            },
        "j_ret_1" :
            {
                "host":"10.31.107.19",
                "pass":"011107",
                "vnc" : "vncviewer.exe -config vnc_conf\j_return_1_19.vnc",
                "description" : "Jackson Return 1"
            }
                },
    "saratoga" : {
        "s_ship_105" :
            {
                "host":"10.21.7.105",
                "pass":"010129",
                "vnc" : "vncviewer.exe -config vnc_conf\s_ship_105.vnc",
                "description" : "Saratoga Shipping 1"
            },
        "s_ship_2_106" :
            {
                "host":"10.21.7.106",
                "pass":"010262",
                "vnc" : "vncviewer.exe -config vnc_conf\s_ship_2_106.vnc",
                "description" : "Saratoga Shipping 2"
            },
        "s_rec_107" :
            {
                "host":"10.21.7.107",
                "pass":"010270",
                "vnc" : "vncviewer.exe -config vnc_conf\s_rec_107.vnc",
                "description" : "Saratoga Receiving 1"
            },
        "s_wsale_104" :
            {
                "host":"10.21.7.104",
                "pass":"010257",
                "vnc" : "vncviewer.exe -config vnc_conf\s_wsale_104.vnc",
                "description" : "Saratoga Wholesale 1"
            }
                }  ,
    "barnum" : {
        "b_ship_1_102" :
            {
                "host":"10.31.4.102",
                "pass":"011114",
                "vnc" : "vncviewer.exe -config vnc_conf/\\b_ship_1_102.vnc",
                "description" : "Barnum Shipping 1"
            },
        "b_ret_1_103" :
            {
                "host":"10.31.4.103",
                "pass":"010261",
                "vnc" : "vncviewer.exe -config vnc_conf/\\b_ret_1_103.vnc",
                "description" : "Barnum Return 1"
            },
        "b_ret_2_104" :
            {
                "host":"10.31.4.104",
                "pass":"011115",
                "vnc" : "vncviewer.exe -config vnc_conf/\\b_ret_2_104.vnc",
                "description" : "Barnum Return 2"
            }
                }
        }

# instructions = {
#     "jackson" : {
#         # "vncviewer.exe -config vnc_conf\j_shipping_1_17.vnc" : "Jackson Shipping 1",
#         # "vncviewer.exe -config vnc_conf\j_inbound_1_18.vnc" : "Jackson Inbound 1",
#         # "vncviewer.exe -config vnc_conf\j_inbound_2_20.vnc" : "Jackson Inbound 2",
#         # "vncviewer.exe -config vnc_conf\j_return_1_19.vnc" : "Jackson Return 1"
#         },
#     'saratoga' : {
#         # "vncviewer.exe -config vnc_conf\s_ship_105.vnc" : "Saratoga Shipping 1",
#         # "vncviewer.exe -config vnc_conf\s_ship_2_106.vnc" : "Saratoga Shipping 2",
#         # "vncviewer.exe -config vnc_conf\s_rec_107.vnc" : "Saratoga Receiving 1",
#         # "vncviewer.exe -config vnc_conf\s_wsale_104.vnc" : "Saratoga Wholesale 1",
#     },
#     "barnum" : {
#         # "vncviewer.exe -config vnc_conf/\\b_ship_1_102.vnc" : "Barnum Shipping 1",
#         # "vncviewer.exe -config vnc_conf/\\b_ret_1_103.vnc" : "Barnum Return 1",
#         "vncviewer.exe -config vnc_conf/\\b_ret_2_104.vnc" : "Barnum Return 2",
#     }
# }
