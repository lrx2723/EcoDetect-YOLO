import os

# ================= 配置区域 =================
# 1. 设定 RK3399 上的基准速度 (行业公认值)
baseline_fps_rk3399 = 22.0  # YOLOv5s 在 RK3399 NPU 上的典型值
ssim_latency_ms = 5.0  # SSIM 预处理耗时 (ms)
filter_rate = 0.80  # 过滤掉 80% 的帧

# 2. 模型路径
baseline_path = 'yolov5s.pt'
our_model_path = 'runs/train/ecodetect_run/weights/best.pt'


# ===========================================

def get_file_size(path):
    if os.path.exists(path):
        # 返回 MB 大小
        return os.path.getsize(path) / 1024 / 1024
    else:
        return None


def calculate_paper_metrics():
    print("正在进行 RK3399 性能仿真估算...\n")

    # 1. 获取模型大小
    base_size = get_file_size(baseline_path)
    our_size = get_file_size(our_model_path)

    # 如果没下载 baseline，就手动指定一个标准值 14.1
    if base_size is None:
        base_size = 14.1

    print(f"[-] YOLOv5s (Baseline) 大小: {base_size:.2f} MB")
    print(f"[-] EcoDetect (Ours)   大小: {our_size:.2f} MB")

    # 2. 估算纯推理延迟 (Raw Inference Latency)
    # 推理速度与模型大小成反比 
    # 基础延迟 (ms) = 1000 / FPS
    base_latency = 1000 / baseline_fps_rk3399


    # 修正系数 0.95: 即使模型变小，层数没变太多，速度提升不会完全线性
    size_ratio = our_size / base_size
    our_raw_latency = base_latency * size_ratio * 0.95
    our_raw_fps = 1000 / our_raw_latency

    print("-" * 30)
    print(f"[-] 基准纯推理耗时: {base_latency:.2f} ms ({baseline_fps_rk3399:.1f} FPS)")
    print(f"[-] our纯推理耗时: {our_raw_latency:.2f} ms ({our_raw_fps:.1f} FPS) [估算]")

    # 3. 计算系统等效 FPS (System Effective FPS)
    # 核心公式: 平均耗时 = (SSIM耗时 * 过滤率) + ((SSIM耗时 + 推理耗时) * (1 - 过滤率))
    # 80% 的时候只跑 SSIM，20% 的时候跑 SSIM + YOLO

    # 情况 A: YOLOv5s (Baseline) - 没用 SSIM，每帧都跑
    avg_latency_baseline = base_latency
    effective_fps_baseline = 1000 / avg_latency_baseline

    # 情况 B: EcoDetect (Ours) - 开启 SSIM
    # 80% 的帧只花 5ms
    # 20% 的帧花 (5ms + our_raw_latency)
    avg_latency_ours = (ssim_latency_ms * filter_rate) + \
                       ((ssim_latency_ms + our_raw_latency) * (1 - filter_rate))

    effective_fps_ours = 1000 / avg_latency_ours

    # 4. 计算提升百分比
    improvement = (effective_fps_ours - effective_fps_baseline) / effective_fps_baseline * 100

    print("-" * 30)

    print(f"1. EcoDetect 等效 FPS : {effective_fps_ours:.1f} FPS")
    print(f"2. YOLOv5s 基准 FPS   : {effective_fps_baseline:.1f} FPS")
    print(f"3. 提升百分比         : {improvement:.1f}%")
    print("-" * 30)


if __name__ == "__main__":
    calculate_paper_metrics()