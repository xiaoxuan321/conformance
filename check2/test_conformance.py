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
            net_inductive, im_inductive, fm_inductive = pm4py.discover_petri_net_inductive(BPIC13_cp,
                                                                                                    activity_key='concept:name',
                                                                                                    case_id_key='case:concept:name',
                                                                                                    timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC13_cp, net_inductive,
                                                                                 im_inductive, fm_inductive,
                                                                                 activity_key='concept:name',
                                                                                 case_id_key='case:concept:name',
                                                                                 timestamp_key='time:timestamp')

        elif param == "BPIC13_i":
            net_inductive, im_inductive, fm_inductive = pm4py.discover_petri_net_inductive(BPIC13_i,
                                                                                           activity_key='concept:name',
                                                                                           case_id_key='case:concept:name',
                                                                                           timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC13_i, net_inductive,
                                                                                 im_inductive, fm_inductive,
                                                                                 activity_key='concept:name',
                                                                                 case_id_key='case:concept:name',
                                                                                 timestamp_key='time:timestamp')
        elif param == "BPIC15_1f":
            net_inductive, im_inductive, fm_inductive = pm4py.discover_petri_net_inductive(BPIC15_1f,
                                                                                                    activity_key='concept:name',
                                                                                                    case_id_key='case:concept:name',
                                                                                                    timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_1f, net_inductive,
                                                                                 im_inductive, fm_inductive,
                                                                                 activity_key='concept:name',
                                                                                 case_id_key='case:concept:name',
                                                                                 timestamp_key='time:timestamp')
        elif param == "BPIC15_2f":
            net_inductive, im_inductive, fm_inductive = pm4py.discover_petri_net_inductive(BPIC15_2f,
                                                                                                    activity_key='concept:name',
                                                                                                    case_id_key='case:concept:name',
                                                                                                    timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_2f, net_inductive,
                                                                                 im_inductive, fm_inductive,
                                                                                 activity_key='concept:name',
                                                                                 case_id_key='case:concept:name',
                                                                                 timestamp_key='time:timestamp')
        elif param == "BPIC15_4f":
            net_inductive, im_inductive, fm_inductive = pm4py.discover_petri_net_inductive(BPIC15_4f,
                                                                                                    activity_key='concept:name',
                                                                                                    case_id_key='case:concept:name',
                                                                                                    timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_4f, net_inductive,
                                                                                 im_inductive, fm_inductive,
                                                                                 activity_key='concept:name',
                                                                                 case_id_key='case:concept:name',
                                                                                 timestamp_key='time:timestamp')
        elif param == "BPIC15_5f":
            net_inductive, im_inductive, fm_inductive = pm4py.discover_petri_net_inductive(BPIC15_5f,
                                                                                                    activity_key='concept:name',
                                                                                                    case_id_key='case:concept:name',
                                                                                                    timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_5f, net_inductive,
                                                                                 im_inductive, fm_inductive,
                                                                                 activity_key='concept:name',
                                                                                 case_id_key='case:concept:name',
                                                                                 timestamp_key='time:timestamp')
    else:
        print("没有提供任何命令行参数")


