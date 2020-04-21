## 简介

用来生成rss总的rss的代码。

结果样例：
- https://git.zeekling.cn/rss.xml

## 使用

- 安装依赖
  ```sh
  pip3 install -r requirement.txt
  ```

- 打开gen_rss.py 修改
  ```python
  # 需要保存的rss位置
  file_path = "./rss.xml"
  # 自己gitea的url
  code_url='https://git.zeekling.cn/'
  ```
- 执行下面脚本即可
  ```sh
  ./gen_rss.py
  ```

