batter_stats_headers = [
    "CID",
    "position",
    "full_title",
    "bats",
    "throws",
    "ovr",
    "con",
    "gap",
    "pow",
    "eye",
    "avk",
    "babip",
    "conVL",
    "gapVL",
    "powVL",
    "eyeVL",
    "avkVL",
    "babipVL",
    "conVR",
    "gapVR",
    "powVR",
    "eyeVR",
    "avkVR",
    "babipVR",
    "ifrng",
    "ifarm",
    "tdp",
    "iferr",
    "ofrng",
    "ofarm",
    "oferr",
    "carm",
    "cabi",
    "cx",
    "1bx",
    "2bx",
    "3bx",
    "ssx",
    "lfx",
    "cfx",
    "rfx",
    "spe",
    "ste",
    "run",
    "cDefense",
    "1bDefense",
    "2bDefense",
    "3bDefense",
    "ssDefense",
    "lfDefense",
    "cfDefense",
    "rfDefense",
    "pa",
    "avg",
    "obp",
    "ops",
    "woba",
    "bsr_600_pa",
    "zr_600_pa",
    "batr_600_pa",
    "war_600_pa",
]
batter_stats_freeze_col = "con"
batter_stats_hidden_columns = [
    ["con", "rfDefense"]
]
ovr_batters_stats_headers = batter_stats_headers + [
    "batr_600_pa_ft",
    "batr_600_pa_vr",
    "batr_600_pa_vl",
    "war_600_pa_ft",
    "war_600_pa_vr",
    "war_600_pa_vl",
]

sp_stats_headers = [
    "CID",
    "position",
    "full_title",
    "bats",
    "throws",
    "ovr",
    "stu",
    "mov",
    "ctl",
    "stuVL",
    "movVL",
    "ctlVL",
    "stuVR",
    "movVR",
    "ctlVR",
    "gbpct",
    "velo",
    "stam",
    "hold",
    "px",
    "sp_bf",
    "sp_ip",
    "sp_k_per_9",
    "sp_bb_with_hbp_per_9",
    "sp_hr_per_9",
    "sp_whip",
    "sp_fip",
    "sp_era",
    "ip_per_gamesstarted",
    "sp_war_per_220_ip",
]
sp_stats_freeze_col = "stu"
sp_stats_hidden_columns = [
    ["gbpct", "px"]
]

rp_stats_headers = [
    "CID",
    "position",
    "full_title",
    "bats",
    "throws",
    "ovr",
    "stu",
    "mov",
    "ctl",
    "stuVL",
    "movVL",
    "ctlVL",
    "stuVR",
    "movVR",
    "ctlVR",
    "gbpct",
    "velo",
    "stam",
    "hold",
    "px",
    "rp_bf",
    "rp_ip",
    "rp_k_per_9",
    "rp_bb_with_hbp_per_9",
    "rp_hr_per_9",
    "rp_whip",
    "rp_fip",
    "rp_era",
    "ip_per_gamesrelieved",
    "leverage",
    "rp_war_per_100_ip",
]
rp_stats_freeze_col = "stu"
rp_stats_hidden_columns = [
    ["gbpct", "px"]
]