# Musicpack - Generator

> Version 0.1.1
>
> Minecraft 可以通过资源包的方式添加声音资源, 本项目会帮你完成打包的大部分工作。



## 功能

* 音乐格式自动转换为 `.ogg`
* 音乐名自动转合法
* 根据信息生成描述
* 自动生成 `sounds.json`



## 使用方法

* 修改 `make.py` 文件中的变量，默认请将音乐文件放在`raw/$packName` 目录下

* 描述会自动生成，内容包括：

  > $packName - $package
  >
  > %d songs in the pack

* 如果希望音乐包有图标，请将 `pack.png` 放在同级目录下，程序会自动复制进包内，`pack.png` 的要求：

  > 如果未指定图标，则包旁边将显示圆石图标。任何图像都可以在此处使用，只要它名为`pack.png`。`pack.png`文件必须为64 x 64像素，才能正确渲染自定义图像。
  >
  > 来自 [MinecraftWiki](https://minecraft-zh.gamepedia.com/%E6%95%99%E7%A8%8B/%E5%88%B6%E4%BD%9C%E8%B5%84%E6%BA%90%E5%8C%85)



* 运行 `make.py`

* 处理好的资源包会放在 `$output_path` 下面



## 配置

#### packName

资源包的名字

#### path

存放音乐文件的地方，默认为 `raw`

#### convert_path

如果音乐文件中有需要转换的音乐，其转换结果会被放在此目录，默认为 `convert`

#### output_path

输出目录，默认为 `build/$packName`

#### package

包名，或者是命名空间，用于在游戏内分离

#### pack_format

> 来自 [MinecraftWiki](https://minecraft-zh.gamepedia.com/%E6%95%99%E7%A8%8B/%E5%88%B6%E4%BD%9C%E8%B5%84%E6%BA%90%E5%8C%85)

- [Java版1.6](https://minecraft-zh.gamepedia.com/1.6)至[Java版1.8](https://minecraft-zh.gamepedia.com/1.8)为`1`
- [Java版1.9](https://minecraft-zh.gamepedia.com/1.9)至[Java版1.10](https://minecraft-zh.gamepedia.com/1.10)为`2`
- [Java版1.11](https://minecraft-zh.gamepedia.com/1.11)至[Java版1.12](https://minecraft-zh.gamepedia.com/1.12)为`3`
- [Java版1.13](https://minecraft-zh.gamepedia.com/1.13)至[Java版1.14](https://minecraft-zh.gamepedia.com/1.14)为`4`
- [Java版1.15](https://minecraft-zh.gamepedia.com/1.15)需要`5`

#### description

如果要修改描述，将 `description` 变量改为非 `"auto"` 的值即可



## 计划

- [ ] 无头模式
- [ ] 自动删除原文件
- [ ] 自动打压缩包