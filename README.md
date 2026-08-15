# 启海号 QIHAI · 邮轮目的地化展示

围绕"邮轮目的地化"命题的竞赛展示项目：**单页 3D 交互网站 + 5 张 SVG 设计展板**。
以数字游民和青少年研学群体为主要服务对象，将邮轮从传统交通与旅游载体转变为可停留、可交流、可持续运营的海上生活空间。

## 快速开始

```bash
python app.py          # 推荐: 启动本地服务器并自动打开浏览器(标准库, 零依赖)
```

或双击 `启动预览.bat`，或手动：

```bash
python -m http.server 8791 --bind 127.0.0.1
# 浏览器打开 http://127.0.0.1:8791/web/index.html
```

> 不能直接双击 `web/index.html` —— ES Module + fetch 限制，必须走 http://。

线上版：<https://lizhong0525.github.io/threejsDEMO/>（GitHub Pages，main 分支根目录）

## 展示内容

- **3D 主视图**：360m 邮轮实时渲染（three.js r164，全部本地化，无外部网络依赖）
  - **航行态 / 靠港态**切换：六边形模块甲板重构动画、船尾折叠舞台展开、C 字港场景
  - **六个时段**：06:20 日出 → 星夜，夜间舷侧泛光照明
  - **三种视图**：环绕 / 甲板拆解 / 中纵剖视
  - **金色标记 ①–④** 四大创新点 · **品红标记 ⑤–⑩** 六种船上设施（点击直达剖视特写）
- **航线**：上海/广东/香港出发，停靠吉隆坡与新加坡，南洋风情航线
- **甲板场景**：日出瑜伽、海上温泉、儿童水乐园、六边形舱书吧、观星台、火塘酒廊
- **船上设施**：轮机与保障层 / 海景与阳台客舱 / 主餐厅与中央剧院 / 中庭商业接待 / 健身水疗 / 驾驶台与研学观测
- **设计图纸**：`boards/` 5 张 SVG 展板（总布置剖面、双态对比、六边形模块、航线、服务与数字化）

## URL 参数（直达状态/机位）

| 参数 | 示例 | 说明 |
|---|---|---|
| `?t=` | `night` | 时段：day / dusk / golden / night / yoga / onsen / fire |
| `?state=` | `port` | 靠港态（默认 sail 航行态） |
| `?view=` | `section` | 视图：orbit / explode / section |
| `?facil=` | `0..5` | 设施剖视特写 |
| `?scene=` | `0..5` | 甲板场景直达 |
| `?cam=` | `x,y,z&tgt=x,y,z` | 任意相机机位（验证截图用） |

## 目录结构

```
app.py                 本地预览入口(标准库, 零依赖)
启动预览.bat            Windows 一键预览
web/                   成品网站
  index.html           唯一页面(场景/交互/舱内设施全在里面)
  ship2.glb            船体模型(生成物, 勿手改)
  model_meta.json      模型元数据(甲板层高/模块区/舞台锚点)
  vendor/              three.js r164 本地化
  boards/              网站引用的展板 SVG
boards/                展板源文件(SVG + PNG)
process_stl.py         模型管道: assets/cruise.stl → web/ship2.glb
gen_boards.py / gen_board2..5.py   展板生成脚本
boards_common.py       展板公共样式/组件
cdp_shot.py            无头验证截图工具
assets/                原始模型与图纸数据(cruise.stl / deck_data.json / DWG 备份)
```

## 重新生成模型（可选）

```bash
pip install -r requirements.txt
python process_stl.py     # 重写 web/ship2.glb + web/model_meta.json
```

模型约定：舷侧装饰一律**船体面片直染**（蜡染彩绘 / 舷窗玻璃带），不贴几何体；
救生艇、泳池、雷达桅等细节由脚本一并烧进 GLB。

## 技术栈

three.js r164（WebGL，本地化）· 原生 ES Module，无构建步骤 ·
Python 模型管道（trimesh / fast_simplification / scipy / shapely）
