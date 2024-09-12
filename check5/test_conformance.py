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
            # 使用日志框架执行一致性检查
            log_skeleton = pm4py.discover_log_skeleton(BPIC13_cp, noise_threshold=0.1, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC13_cp, log_skeleton, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
        elif param == "BPIC13_i":
            log_skeleton = pm4py.discover_log_skeleton(BPIC13_i, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name',
                                                       timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC13_i, log_skeleton, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
        elif param == "BPIC15_1f":
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_1f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name',
                                                       timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC15_1f, log_skeleton, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
        elif param == "BPIC15_2f":
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_2f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name',
                                                       timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC15_2f, log_skeleton, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
        elif param == "BPIC15_4f":
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_4f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name',
                                                       timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC15_4f, log_skeleton, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
        elif param == "BPIC15_5f":
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_5f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name',
                                                       timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC15_5f, log_skeleton, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
    else:
        print("没有提供任何命令行参数")


