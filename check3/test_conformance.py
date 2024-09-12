import pm4py
import sys
if __name__ == "__main__":
    # 加载 .xes 文件
    BPIC13_cp = pm4py.read_xes('BPIC13_cp.xes')
    BPIC13_i = pm4py.read_xes('BPIC13_i.xes')
    BPIC15_1f = pm4py.read_xes("BPIC15_1f.xes")
    BPIC15_2f = pm4py.read_xes("BPIC15_2f.xes")
    BPIC15_4f = pm4py.read_xes("BPIC15_4f.xes")
    BPIC15_5f = pm4py.read_xes("BPIC15_5f.xes")


    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "BPIC13_cp":
            declare_model = pm4py.discover_declare(BPIC13_cp)
            conf_result = pm4py.conformance_declare(BPIC13_cp, declare_model)
        elif param == "BPIC13_i":
            declare_model = pm4py.discover_declare(BPIC13_i)
            conf_result = pm4py.conformance_declare(BPIC13_i, declare_model)
        elif param == "BPIC15_1f":
            declare_model = pm4py.discover_declare(BPIC15_1f)
            conf_result = pm4py.conformance_declare(BPIC15_1f, declare_model)
        elif param == "BPIC15_2f":
            declare_model = pm4py.discover_declare(BPIC15_2f)
            conf_result = pm4py.conformance_declare(BPIC15_2f, declare_model)
        elif param == "BPIC15_4f":
            declare_model = pm4py.discover_declare(BPIC15_4f)
            conf_result = pm4py.conformance_declare(BPIC15_4f, declare_model)
        elif param == "BPIC15_5f":
            declare_model = pm4py.discover_declare(BPIC15_5f)
            conf_result = pm4py.conformance_declare(BPIC15_5f, declare_model)
    else:
        print("没有提供任何命令行参数")


