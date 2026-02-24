import os
import shutil
import xml.etree.ElementTree as ET
from tqdm import tqdm

# ==================== 配置区域 ====================
# 1. XML 标签文件夹路径
XML_DIR = r'F:\Paper_Project2026.1.8\code\Garbage_Detection\data_xml\labels'

# 2. 图片文件夹路径 (必须填对，否则只能移走XML，留下一堆没标签的图片)
IMG_DIR = r'F:\Paper_Project2026.1.8\code\Garbage_Detection\data_xml\images'  # 假设图片在这个位置，请修改为你真实的图片路径！

# 3. 隔离区路径 (把筛选出来的 pet 数据移到这里，万一以后要用还能找回来)
QUARANTINE_DIR = r'F:\Paper_Project2026.1.8\第15批方案B训练数据(标注)2021.8.25'

# 4. 要剔除的目标类别名称
TARGET_CLASS = 'pet'


# ====================================================

def move_file(src_path, dst_folder):
    if os.path.exists(src_path):
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)
        shutil.move(src_path, os.path.join(dst_folder, os.path.basename(src_path)))
        return True
    return False


if __name__ == '__main__':
    # 确保隔离目录存在
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)

    xml_files = [f for f in os.listdir(XML_DIR) if f.endswith('.xml')]
    print(f"正在扫描 {len(xml_files)} 个文件...")

    moved_count = 0

    for xml_file in tqdm(xml_files):
        xml_path = os.path.join(XML_DIR, xml_file)

        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()

            has_target = False
            # 检查该文件里是否包含 pet
            for obj in root.findall('object'):
                name = obj.find('name').text
                if name == TARGET_CLASS:
                    has_target = True
                    break

            # 如果包含 pet，就把 xml 和对应的图片都移走
            if has_target:
                # 1. 移动 XML
                move_file(xml_path, QUARANTINE_DIR)

                # 2. 移动对应的图片 (尝试多种后缀)
                img_name_base = os.path.splitext(xml_file)[0]
                extensions = ['.jpg', '.jpeg', '.png', '.bmp']
                found_img = False
                for ext in extensions:
                    img_path = os.path.join(IMG_DIR, img_name_base + ext)
                    if move_file(img_path, QUARANTINE_DIR):
                        found_img = True
                        break

                if not found_img:
                    print(f"警告：移动了 XML 但未找到对应图片 -> {xml_file}")

                moved_count += 1

        except Exception as e:
            print(f"解析错误: {xml_file}, {e}")

    print(f"\n清洗完成！")
    print(f"共移除了 {moved_count} 组包含 '{TARGET_CLASS}' 的数据。")
    print(f"它们被安全保存在: {QUARANTINE_DIR}")