import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


seg_map = {
    0: 63,
    1: 6,
    2: 91,
    3: 79,
    4: 102,
    5: 109,
    6: 124,
    7: 7,
    8: 127,
    9: 103
}

segments = [seg_map[0], seg_map[9], seg_map[9],  seg_map[1], seg_map[5], seg_map[3], seg_map[4], seg_map[2], seg_map[0]]

@cocotb.test()
async def test_7seg(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    
    dut._log.info("reset")
    dut.rst.value = 1
    dut.seed.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0

    dut._log.info("check all segments")
    for i in range(9):
        dut._log.info("check segment {}".format(i))
        await ClockCycles(dut.clk, 100)
        dut._log.info("segment_value={}, assert {}".format(int(dut.segments.value), segments[i]))
        assert int(dut.segments.value) == segments[i]
