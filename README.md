# 高熵合金混炉确权、提货与补足

中试炉的原料交接、化验结果和实际过磅按炉次与货主编号交接。

《委托熔炼交换》说明在 [交换约定](docs/exchange.md)。`fixtures/exchange.json` 是本机联调使用的合成记录。项目当前可读取这些交换文件，回放对接方回执，并验证资料之间的引用。

运行环境为 Python 3.11.2，只依赖标准库。执行 `python3 -m unittest -v` 检查交换资料。执行 `python3 partner.py` 后，可通过回环地址的 8087 端口查询回执，`GET /health` 返回服务状态。如需模拟查询暂时失败，启动时传入 `--unavailable`。
