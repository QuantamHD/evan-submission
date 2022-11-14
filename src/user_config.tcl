set ::env(DESIGN_NAME) xor_shift32_quantamhd
set ::env(VERILOG_FILES) "\
    $::env(DESIGN_DIR)/counter.v \
    $::env(DESIGN_DIR)/decoder.v"
