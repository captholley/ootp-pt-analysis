data_headers = [
    "t_CID",
    "CID",
    "type",
    "position",
    "first_name",
    "last_name",
    "team",
    "year",
    "tier",
    "ovr",
    "orig_ovr",
    "short_title",
    "height",
    "bats",
    "throws",
    "full_title",
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
    "bun",
    "bfh",
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
    "ifrng",
    "ifarm",
    "tdp",
    "iferr",
    "ofrng",
    "ofarm",
    "oferr",
    "carm",
    "cabi",
    "px",
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
    "HBP_vL",
    "BB_vL",
    "K_vL",
    "HR_vL",
    "singles_vL",
    "doubles_vL",
    "triples_vL",
    "AVG_vL",
    "OBP_vL",
    "OPS_vL",
    "wOBA_vL",
    "HBP_vR",
    "BB_vR",
    "K_vR",
    "HR_vR",
    "singles_vR",
    "doubles_vR",
    "triples_vR",
    "AVG_vR",
    "OBP_vR",
    "OPS_vR",
    "wOBA_vR",
    "wOBA_ft_starter",
    "wOBA_vR_starter",
    "wOBA_vL_starter",
    "C_expected_zr",
    "1B_expected_zr",
    "2B_expected_zr",
    "3B_expected_zr",
    "SS_expected_zr",
    "LF_expected_zr",
    "CF_expected_zr",
    "RF_expected_zr",
    "C_expected_outs_above_avg",
    "1B_expected_outs_above_avg",
    "2B_expected_outs_above_avg",
    "3B_expected_outs_above_avg",
    "SS_expected_outs_above_avg",
    "LF_expected_outs_above_avg",
    "CF_expected_outs_above_avg",
    "RF_expected_outs_above_avg",
    "cera_effect_runs_saved",
    "expected_rto_above_avg",
    "expected_steals_given_up_above_avg",
    "steal_attempts",
    "caught_stealing",
    "ubr",
]
data_freeze_col = "orig_ovr"
data_hidden_columns = []

pitcher_headers = [
    "t_CID",
    "type",
    "position",
    "first_name",
    "last_name",
    "team",
    "year",
    "tier",
    "ovr",
    "bats",
    "throws",
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
]
pitcher_freeze_col = "bats"
pitcher_hidden_columns = [
    ["t_CID", "t_CID"],
    ["gbpct", "px"]
]

batter_headers = [
    "t_CID",
    "type",
    "position",
    "first_name",
    "last_name",
    "team",
    "year",
    "tier",
    "ovr",
    "bats",
    "throws",
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
    "bun",
    "bfh",
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
    "wOBA_vL",
    "wOBA_vR",
    "wOBA_ft_starter",
    "wOBA_vR_starter",
    "wOBA_vL_starter",
]
batter_freeze_col = "bats"
batter_hidden_columns = [
    ["t_CID", "t_CID"],
    ["bun", "run"]
]